// Translation catalogs (CONTRACT-001). One JSON file per language in locales/;
// pages read every user-facing string through translate().

import en from "../locales/en.json" with { type: "json" };
import es from "../locales/es.json" with { type: "json" };
import { isLocale } from "./i18n.mjs";

const CATALOGS = Object.freeze({ en, es });

export function getCatalog(locale) {
  if (!isLocale(locale)) throw new RangeError(`Unsupported locale: ${locale}`);
  return CATALOGS[locale];
}

// A missing key is a defect: it throws instead of showing the raw key to a visitor.
export function translate(catalog, key) {
  const value = Object.hasOwn(catalog, key) ? catalog[key] : undefined;
  if (typeof value !== "string" || value === "") throw new Error(`Missing translation: ${key}`);
  return value;
}
