import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "NIBBI Dealer Page · V2 Prototype",
  description: "NIBBI Racing Become a Dealer discussion prototype and delivery workflow.",
  robots: { index: false, follow: false },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="zh-CN"><body>{children}</body></html>;
}
