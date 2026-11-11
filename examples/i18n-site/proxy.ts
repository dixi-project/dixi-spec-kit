// Illustrative Next.js 16 proxy (FEATURE-001, criteria 1–2). All decisions live in
// lib/i18n.mjs, which `node --test` covers; this file only adapts them to Next.js.
import { NextResponse, type NextRequest } from "next/server";
import { redirectTarget } from "./lib/i18n.mjs";

export function proxy(request: NextRequest) {
  const target = redirectTarget(request.nextUrl.pathname, request.headers.get("accept-language"));
  if (target === null) return NextResponse.next();
  const response = NextResponse.redirect(new URL(target, request.url), 307);
  // The redirect depends on the visitor's language: shared caches must not reuse it.
  response.headers.set("Vary", "Accept-Language");
  response.headers.set("Cache-Control", "private, no-store");
  return response;
}

export const config = {
  matcher: ["/((?!_next/|api/|.*\\..*).*)"],
};
