import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "NIBBI Racing | Become a Dealer",
  description: "Apply to become a NIBBI Racing dealer and access product guidance, marketing support and structured growth opportunities.",
  robots: { index: false, follow: false },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
