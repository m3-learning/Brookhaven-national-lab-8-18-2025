---
layout: main-custom-layout
titleText: "Ferroelectric Thin Films: Using Pulsed Laser Deposition"
mainHeight: 70
textboxHeight: 0
---

<style scoped>
.crossfade-container {
  position: relative;
  width: 100%;
  height: 500px;
}
.crossfade-chart {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 1s ease-in-out;
  pointer-events: none;
}
.crossfade-chart.active {
  opacity: 1;
  z-index: 2;
  pointer-events: auto;
}
</style>

<v-clicks>
<div class="crossfade-container">
  <!-- First Diagram -->
  <div :class="[$clicks >= 0 ? 'crossfade-chart active' : 'crossfade-chart']">
    <v-clicks>
```mermaid
flowchart TD
  A[Start] --> B[Step 1]
  B --> C[Step 2]
  C --> D[Final Step]
```
    </v-clicks>
  </div>

  <!-- Second Diagram -->
  <div :class="[$clicks >= 1 ? 'crossfade-chart active' : 'crossfade-chart']">
    <v-clicks>
```mermaid
flowchart TD
  A[Start] --> B[Step 1]
  B --> C[Step 2]
  C --> D[Final Step]
```
    </v-clicks>
  </div>
</div>
</v-clicks>
