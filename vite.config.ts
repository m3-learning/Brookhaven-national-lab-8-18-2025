// vite.config.ts
import { defineConfig } from 'vite'

const repo = process.env.REPO || ''  // from CI env

export default defineConfig({
  base: repo ? `/${repo}/` : '/',
})
