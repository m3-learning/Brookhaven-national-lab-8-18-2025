---
layout: main-custom-layout
titleText: "Crossfade Mermaid"
mainHeight: 80
textboxHeight: 0
---

<script setup>

const diagrams = [
  `flowchart TD
     A[Start] --> B[Step 1]
     B --> C[Step 2]
     C --> D[Final Step]`,

  `flowchart TD
     A --> X
     X --> Y
     Y --> Z
     Z --> End`,

  `flowchart TD
     X1[Init] --> X2[Process]
     X2 --> X3[End]`
]
</script>

<CrossfadeMermaid :diagrams="diagrams" theme="neutral" />
