// Pure i18n routing logic (CONTRACT-001). No dependencies: Next.js imports it from
// proxy.ts and app/[lang]/, and `node --test` exercises it directly.

export const LOCALES = Object.freeze(["en", "es"]);
export const DEFAULT_LOCALE = "en";

const MAX_HEADER = 4096;
const RANGE = /^(\*|[a-z]{1,8}(-[a-z0-9]{1,8})*)$/;
const QUALITY = /^q=(0(\.\d{0,3})?|1(\.0{0,3})?)$/;

export function isLocale(value) {
  return typeof value === "string" && LOCALES.includes(value);
}

// Parses an Accept-Language header into ranges ordered by quality, then by position.
// Malformed entries are ignored; q=0 entries are returned so callers can exclude them.
export function parseAcceptLanguage(header) {
  if (typeof header !== "string" || header.length > MAX_HEADER) return [];
  const ranges = [];
  header.split(",").forEach((part, index) => {
    const [tag, ...params] = part.split(";").map((piece) => piece.trim().toLowerCase());
    if (!RANGE.test(tag)) return;
    let q = 1;
    for (const param of params) {
      const compact = param.replace(/\s+/g, "");
      if (!compact.startsWith("q=")) continue;
      const match = QUALITY.exec(compact);
      if (!match) return;
      q = Number(match[1]);
    }
    ranges.push({ range: tag, q, index });
  });
  return ranges
    .sort((a, b) => b.q - a.q || a.index - b.index)
    .map(({ range, q }) => ({ range, q }));
}

// Chooses the best supported locale: exact tag, then primary subtag (es-MX -> es),
// then the default. Locales the visitor refused with q=0 are never chosen for "*".
export function negotiateLocale(header, locales = LOCALES, fallback = DEFAULT_LOCALE) {
  const ranges = parseAcceptLanguage(header);
  const refused = new Set(ranges.filter(({ q }) => q === 0).map(({ range }) => range));
  for (const { range, q } of ranges) {
    if (q === 0) continue;
    if (range === "*") {
      return [fallback, ...locales].find((locale) => !refused.has(locale)) ?? fallback;
    }
    const exact = locales.find((locale) => locale === range);
    if (exact) return exact;
    const primary = range.split("-")[0];
    const partial = locales.find((locale) => locale === primary && !refused.has(locale));
    if (partial) return partial;
  }
  return fallback;
}

// Splits "/es/about" into { locale: "es", rest: "/about" }; unprefixed paths have locale null.
export function splitLocale(pathname) {
  const match = /^\/([^/]+)(\/.*)?$/.exec(pathname);
  if (match && isLocale(match[1])) return { locale: match[1], rest: match[2] ?? "/" };
  return { locale: null, rest: pathname };
}

// Builds the language-prefixed path. Leading slashes collapse to one, so "//host"
// can never become a protocol-relative URL.
export function localizedPath(locale, path = "/") {
  if (!isLocale(locale)) throw new RangeError(`Unsupported locale: ${locale}`);
  if (typeof path !== "string" || !path.startsWith("/")) throw new RangeError(`Path must start with "/": ${path}`);
  const clean = path.replace(/^\/+/, "/");
  return clean === "/" ? `/${locale}` : `/${locale}${clean}`;
}

// Where an unprefixed request must go, or null when it already carries a locale.
export function redirectTarget(pathname, acceptLanguage) {
  if (splitLocale(pathname).locale) return null;
  return localizedPath(negotiateLocale(acceptLanguage), pathname);
}

// Canonical URL for the page's own language plus one alternate per language and
// x-default, in the shape of Next.js Metadata `alternates`.
export function pageAlternates(origin, locale, path = "/") {
  const base = new URL(origin);
  if (!["http:", "https:"].includes(base.protocol) || base.pathname !== "/" || base.search || base.hash) {
    throw new RangeError(`Origin must be a bare http(s) origin: ${origin}`);
  }
  const url = (target) => new URL(localizedPath(target, path), base).href;
  const languages = Object.fromEntries(LOCALES.map((target) => [target, url(target)]));
  languages["x-default"] = url(DEFAULT_LOCALE);
  return { canonical: url(locale), languages };
}
