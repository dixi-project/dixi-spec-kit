// Illustrative root layout: the document language comes from the URL prefix.
import type { ReactNode } from "react";
import { notFound } from "next/navigation";
import { LOCALES, isLocale } from "../../lib/i18n.mjs";

export const dynamicParams = false;

export function generateStaticParams() {
  return LOCALES.map((lang) => ({ lang }));
}

type Props = { children: ReactNode; params: Promise<{ lang: string }> };

export default async function LocaleLayout({ children, params }: Props) {
  const { lang } = await params;
  if (!isLocale(lang)) notFound();
  return (
    <html lang={lang}>
      <body>{children}</body>
    </html>
  );
}
