import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://danmcspirit.com',
  output: 'static',
  vite: {
    ssr: {
      external: ['svgo']
    }
  }
});
