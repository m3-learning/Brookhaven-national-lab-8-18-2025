// slidev.config.ts
import { defineConfig } from 'slidev/config'

export default defineConfig({
  mermaid: {
    theme: 'neutral',       // 'default', 'forest', 'dark', etc.
    startOnLoad: true,
    flowchart: {
      useMaxWidth: false,   // prevents oversized layout width
      nodeSpacing: 20,      // decrease for tighter node packing
      rankSpacing: 300,      // vertical or horizontal spacing between layers
      padding: 5,           // inner node padding
    },
    securityLevel: 'loose', // allows use of HTML inside nodes
  },
})
