---
layout: main-custom-layout
titleText: "To Sand or Not to Sand, That is the Question"
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
titleClicks: [1, 2]
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

<div class="h-full w-full flex items-center justify-center">
  <video controls class="max-w-full max-h-full">
    <source src="/plume-dynamics/t5_plume_video.mp4" type="video/mp4">
  </video>
</div>

---
layout: main-custom-layout
titleText: "Full-Frame Plume Dynamics Imaging"
mainHeight: 75
textboxHeight: 0
---

<CrossfadeImages :images="[
  'plume-dynamics/example-images.png',
]" />

<!-- <div class="h-[80vh] overflow-y-auto overflow-x-hidden p-4">
  <div class="flex flex-col items-center justify-center gap-4">
    <img
      src="/plume-dynamics/2_RSM_Analysis.png"
      class="max-w-full"
      id="zoomable-image"
      style="transform-origin: top center; transition: transform 0.2s;"
      alt="Example of Plume Dynamics"
    />
  </div>
</div> -->

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
titleClicks: [1, 2]
columnWidths: [1, 1]
textboxHeight: 0
mainHeight: 65
reference: "Colab: R. Ramesh, Lane Martin (Rice), John Heron (Michigan)" 
roundedEdges: false
---

<template #col1>
<div v-click="2" class="text-left gap-4 flex-1">
    <ul class="list-disc pl-4">
      <li>Computer Vision can be used to characterize the quantify the plume dynamics</li> 
      <li>There are no clear statistically significant trends in the average plume dynamics metrics</li>
    </ul>
  </div>
</template>

---
layout: main-custom-layout
titleText: "Statistical Analysis of Plume Dynamics"
mainHeight: 55
textboxHeight: 10
---

<CrossfadeImages :images="[
  'plume-dynamics/5-Plume_metrics_violinplot.svg',
]" />

::text::
- Statistical distribution of the plume dynamics are bimodal, and heavy tailed for first growths

---
layout: main-custom-layout
titleText: "Heatmap of Plume Area"
mainHeight: 55
textboxHeight: 10
---

<CrossfadeImages :images="[
  'plume-dynamics/5_Plume_Area_Heatmap.png',
]" />

::text::
- Heatmaps of plume area show anomalous behavior close to edge of the target