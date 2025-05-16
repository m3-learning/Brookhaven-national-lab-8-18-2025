---
layout: main-custom-layout
titleText: "Pulsed Laser Deposition Reproducibility"
mainHeight: 75
textboxHeight: 0
---

<CrossfadeImages :images="[
  'plume-dynamics/plume-dynamics.png',
]" />

---
layout: ncolumns
titleText: "Structural Characterization"
columns: 2
images:
  - plume-dynamics/surface-topography.svg
  - plume-dynamics/2_RSM_Analysis.png
titles:
 - Surface Topography
 - Crystal Structure
titleClicks: [0, 1]
columnWidths: [1, 1]
textboxHeight: 0
mainHeight: 80
reference: "Colab: R. Ramesh, Lane Martin (Rice), John Heron (Michigan)" 
roundedEdges: false
---

---
layout: main-custom-layout
titleText: "Full-Frame Plume Dynamics Imaging"
mainHeight: 75
textboxHeight: 0
---

<div class="h-[80vh] overflow-y-auto overflow-x-hidden p-4">
  <div class="flex flex-col items-center justify-center gap-4">
    <img
      src="/public/plume-dynamics/example-images.svg"
      class="max-w-full"
      id="zoomable-image"
      style="transform-origin: top center; transition: transform 0.2s;"
    />
  </div>
</div>

---
layout: ncolumns
titleText: "Plume Dynamics Metrics"
columns: 2
images:
  - plume-dynamics/4-Plume_metrics.png
  - null
titles:
 - Averaged Plume Metrics
 - null
titleClicks: [0, 1]
columnWidths: [1, 1]
textboxHeight: 0
mainHeight: 65
reference: "Colab: R. Ramesh, Lane Martin (Rice), John Heron (Michigan)" 
roundedEdges: false
---