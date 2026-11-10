// Illustrative home page (FEATURE-001, criteria 3–5). Rendered on the server for each
// locale; every visible string comes from locales/<lang>.json through translate().
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { LOCALES, isLocale, localizedPath, pageAlternates } from "../../lib/i18n.mjs";
import { getCatalog, translate } from "../../lib/catalog.mjs";

const ORIGIN = process.env.SITE_ORIGIN ?? "https://example.com";

type Props = { params: Promise<{ lang: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { lang } = await params;
  if (!isLocale(lang)) notFound();
  const catalog = getCatalog(lang);
  return {
    title: translate(catalog, "meta.title"),
    description: translate(catalog, "meta.description"),
    // Next.js renders this as <link rel="canonical"> and one <link rel="alternate" hreflang>.
    alternates: pageAlternates(ORIGIN, lang, "/"),
  };
}

export default async function HomePage({ params }: Props) {
  const { lang } = await params;
  if (!isLocale(lang)) notFound();
  const catalog = getCatalog(lang);
  return (
    <main>
      <h1>{translate(catalog, "home.heading")}</h1>
      <p>{translate(catalog, "home.intro")}</p>
      <nav aria-label={translate(catalog, "nav.languages")}>
        <ul>
          {LOCALES.map((target) => (
            <li key={target}>
              <a href={localizedPath(target, "/")} hrefLang={target} lang={target}>
                {translate(catalog, `language.${target}`)}
              </a>
            </li>
          ))}
        </ul>
      </nav>
    </main>
  );
}
