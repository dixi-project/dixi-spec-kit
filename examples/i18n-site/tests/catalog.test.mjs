// TEST-003 — FEATURE-001 criterion 5 against CONTRACT-001 (lib/catalog.mjs, locales/).
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { LOCALES } from "../lib/i18n.mjs";
import { getCatalog, translate } from "../lib/catalog.mjs";

const page = readFileSync(new URL("../app/[lang]/page.tsx", import.meta.url), "utf8");

test("every language has the same keys with non-empty text", () => {
  const reference = Object.keys(getCatalog("en")).sort();
  for (const locale of LOCALES) {
    const catalog = getCatalog(locale);
    assert.deepEqual(Object.keys(catalog).sort(), reference, locale);
    for (const [key, value] of Object.entries(catalog)) {
      assert.equal(typeof value, "string", `${locale}:${key}`);
      assert.notEqual(value.trim(), "", `${locale}:${key}`);
    }
  }
});

test("catalogs are translated, not copied", () => {
  assert.notEqual(translate(getCatalog("es"), "home.heading"), translate(getCatalog("en"), "home.heading"));
});

test("a missing key throws instead of showing the raw key", () => {
  assert.throws(() => translate(getCatalog("en"), "home.missing"), /Missing translation: home\.missing/);
  assert.throws(() => translate(getCatalog("en"), "toString"), /Missing translation/);
});

test("an unsupported locale has no catalog", () => {
  assert.throws(() => getCatalog("fr"), RangeError);
});

test("every key the page uses exists in every catalog", () => {
  const keys = [...page.matchAll(/translate\(catalog, "([^"]+)"\)/g)].map((match) => match[1]);
  keys.push(...LOCALES.map((locale) => `language.${locale}`));
  assert.ok(keys.length >= 4);
  for (const locale of LOCALES) {
    for (const key of keys) assert.doesNotThrow(() => translate(getCatalog(locale), key), `${locale}:${key}`);
  }
});

test("the page hardcodes no catalog text", () => {
  for (const locale of LOCALES) {
    for (const value of Object.values(getCatalog(locale))) assert.ok(!page.includes(value), value);
  }
});
