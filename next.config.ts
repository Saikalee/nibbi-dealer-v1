import type { NextConfig } from "next";

const isGitHubPages = process.env.GITHUB_PAGES === "true";

const nextConfig: NextConfig = {
  output: isGitHubPages ? "export" : undefined,
  basePath: isGitHubPages ? "/nibbi-dealer-v1" : "",
  assetPrefix: isGitHubPages ? "/nibbi-dealer-v1/" : "",
  images: { unoptimized: true },
  typescript: { ignoreBuildErrors: isGitHubPages },
};

export default nextConfig;
