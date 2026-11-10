// TEST-002 — FEATURE-001 criteria 1–4 against CONTRACT-001 (lib/i18n.mjs).
import { test } from "node:test";
import assert from "node:assert/strict";
import {
  DEFAULT_LOCALE, LOCALES, localizedPath, negotiateLocale, pageAlternates, parseAcceptLanguage,
  redirectTarget, splitLocale,
} from "../lib/i18n.mjs";

test("supports en and es with en as default", () => {
  assert.deepEqual([...LOCALES], ["en", "es"]);
  assert.equal(DEFAULT_LOCALE, "en");
});

test("parses ranges by quality, then by position", () => {
  assert.deepEqual(parseAcceptLanguage("en;q=0.5, es-MX, fr;q=0.8"), [
    { range: "es-mx", q: 1 }, { range: "fr", q: 0.8 }, { range: "en", q: 0.5 },
  ]);
});

test("ignores malformed entries and oversized headers", () => {
  assert.deepEqual(parseAcceptLanguage("es;q=2, <script>, en;q=0.4"), [{ range: "en", q: 0.4 }]);
  assert.deepEqual(parseAcceptLanguage("es,".repeat(2000)), []);
  assert.deepEqual(parseAcceptLanguage(null), []);
});

test("negotiates exact tag, then primary subtag", () => {
  assert.equal(negotiateLocale("es"), "es");
  assert.equal(negotiateLocale("es-MX,es;q=0.9,en;q=0.8"), "es");
  assert.equal(negotiateLocale("fr-CA, en-GB;q=0.7"), "en");
  assert.equal(negotiateLocale("fr, es;q=0.3"), "es");
});

test("falls back to the default language", () => {
  assert.equal(negotiateLocale(undefined), "en");
  assert.equal(negotiateLocale(""), "en");
  assert.equal(negotiateLocale("de, fr;q=0.9"), "en");
});

test("never chooses a language refused with q=0", () => {
  assert.equal(negotiateLocale("en;q=0, *"), "es");
  assert.equal(negotiateLocale("es;q=0, es-MX"), "en");
});

test("splits the locale prefix from the path", () => {
  assert.deepEqual(splitLocale("/es/about"), { locale: "es", rest: "/about" });
  assert.deepEqual(splitLocale("/en"), { locale: "en", rest: "/" });
  assert.deepEqual(splitLocale("/fr/about"), { locale: null, rest: "/fr/about" });
  assert.deepEqual(splitLocale("/"), { locale: null, rest: "/" });
});

test("builds language-prefixed paths and rejects unsupported locales", () => {
  assert.equal(localizedPath("es", "/"), "/es");
  assert.equal(localizedPath("en", "/contact"), "/en/contact");
  assert.throws(() => localizedPath("fr", "/"), RangeError);
  assert.throws(() => localizedPath("en", "contact"), RangeError);
});

test("redirects unprefixed paths by Accept-Language and leaves prefixed ones", () => {
  assert.equal(redirectTarget("/", "es-ES,es;q=0.9"), "/es");
  assert.equal(redirectTarget("/", "de"), "/en");
  assert.equal(redirectTarget("/contact", "es"), "/es/contact");
  assert.equal(redirectTarget("/es/contact", "en"), null);
  assert.equal(redirectTarget("/en", "es"), null);
});

test("redirect targets stay on the same site", () => {
  assert.equal(redirectTarget("//evil.example.com/path", "es"), "/es/evil.example.com/path");
  assert.ok(!redirectTarget("///x", "en").startsWith("//"));
});

test("declares canonical and reciprocal hreflang alternates per language", () => {
  const es = pageAlternates("https://example.com", "es", "/");
  assert.deepEqual(es, {
    canonical: "https://example.com/es",
    languages: { en: "https://example.com/en", es: "https://example.com/es", "x-default": "https://example.com/en" },
  });
  const en = pageAlternates("https://example.com", "en", "/contact");
  assert.equal(en.canonical, "https://example.com/en/contact");
  assert.equal(en.languages.es, "https://example.com/es/contact");
});

test("rejects origins that are not bare http(s) origins", () => {
  assert.throws(() => pageAlternates("ftp://example.com", "en"), RangeError);
  assert.throws(() => pageAlternates("https://example.com/blog", "en"), RangeError);
  assert.throws(() => pageAlternates("not a url", "en"), TypeError);
});
