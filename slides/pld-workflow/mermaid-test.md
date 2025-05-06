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
     A[First Box] --> X[Second Box]
     X --> Y[Third Box]
     Y --> Z[Fourth Box]
     Z --> End[Final Box]`,

  `flowchart TD
     X1[Initial State] --> X2[Processing State]
     X2 --> X3[Final State]`
]
</script>

<CrossfadeMermaid :diagrams="diagrams" theme="neutral" />
