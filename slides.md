---
# You can also start simply with 'default'
theme: ./slide-dev-template/slidev/theme
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
title: "Joshua C. Agar Brookhaven National Laboratory 8-18-2025"
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
# apply unocss classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: fade-out
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true

# open graph
# seoMeta:
#  ogImage: https://cover.sli.dev
layout: cover
---
# 🧠🔩 Chem-AIstry in Motion: Fast Science, Faster Learning – Beyond Equilibrium Synthesis, Powered by ML, FPGAs, and Kubernetes

## Prof. Joshua C. Agar

## {{ new Date().toLocaleDateString() }}

<QrGrid :items="[
  { title: 'Slides', url: 'https://m3-learning.github.io/Brookhaven-national-lab-8-18-2025/1' },
]" :columns="1" />

<!-- <div @click="$slidev.nav.next" class="mt-12 py-1" hover:bg="white op-10">
  Press Space for next page <carbon:arrow-right />
</div> -->

<div class="abs-br m-6 text-xl">
  <a href="https://github.com/m3-learning" target="_blank" class="slidev-icon-btn">
    <carbon:logo-github />
  </a>
</div>


---
src: ./slides/introduction/research-philosphy.md
---

---
src: ./slides/introduction/automated-lab-intro.md
--- 

---
src: ./slides/pld/schematic.md
---

---
src: ./slides/pld-workflow/pld-workflow-svg.md
---

---
src: ./slides/filesystem/filesystem.md
---

---
src: ./slides/pld-dataflow/pld-dataflow.md
---

---
src: ./slides/datafed/datafed.md
---

---
src: ./slides/datafed/datafed-workflow/datafed-workflow.md
---

---
src: ./slides/people/elephant.md
---

---
src: ./slides/pld-diagram2/pld-diagram2.md
---

---
src: ./slides/pld-ui.md
---

---
src: ./slides/microscopy-highlight/microscopy-highlight.md
---

---
src: ./slides/wallpaper-symmetry/order-periodicity-symmetry.md
---

---
src: ./slides/wallpaper-symmetry/wallpapergroups.md
---

---
src: ./slides/wallpaper-symmetry/cross-validation-10k.md
---

---
src: ./slides/wallpaper-symmetry/cross-validation-100k.md
---

---
src: ./slides/wallpaper-symmetry/cross-validation-10m.md
---

---
src: ./slides/wallpaper-symmetry/attention_map.md
---

---
src: ./slides/phys-ml-introduction/phys-ml.md
---

---
src: ./slides/4dstem/4dstem.md
---

---
src: ./slides/4dstem/cc-st-ae.md
---

---
src: ./slides/4dstem/simulated-data.md
---

---
src: ./slides/4dstem/noisy-results.md
---

---
src: ./slides/4dstem/mae.md
---

---
src: ./slides/4dstem/experiment.md
---

---
src: ./slides/pld-workflow/pld-workflow-rheed.md
---

---
src: ./slides/fastml-rheed/rheed-fastml.md
---

---
src: ./slides/fastml-rheed/high-speed-rheed.md
---

---
src: ./slides/plume-dynamics/plume-dynamics.md
---

---
src: ./slides/kubernettes/kubernettes.md
---

---
src: ./slides/fastml/introduction.md
---

---
src: ./slides/fastml/plasma.md
---

---
src: ./slides/fastml/modelcompression.md
---

---
layout: main-custom-layout
titleText: "Acknowledgements"
mainHeight: 83
textboxHeight: 0
---

<CrossfadeImages :images="[
  'people.png',
]"/>

---
layout: main-custom-layout
titleText: "Source Materials"
mainHeight: 83
textboxHeight: 0
---

<QrGrid :items="[
  { title: 'Slides', url: 'https://m3-learning.github.io/Brookhaven-national-lab-8-18-2025/1' },
  { title: 'DataFed', url: 'https://datafed.ornl.gov/ui/welcome' },
  { title: 'Learning Symmetries', url: 'https://github.com/yig319/Understanding-Experimental-Images-by-Identifying-Symmetries-with-Deep-Learning' },
  { title: 'RHEED Analysis', url: 'https://github.com/m3-learning/Predicting-Pulsed-Laser-Deposition-SrTiO3-Homoepitaxy-Growth-Dynamics-using-RHEED'},
  { title: 'Plume Dynamics', url: 'https://github.com/m3-learning/SrRuO3_Plume_Dynamics'},
  { title: 'Auto4DSTEM', url: 'https://github.com/m3-learning/Auto4DSTEM'},
  { title: 'Embedding Visualizer', url: 'https://github.com/chirayupatel9/embedding-be-lmdb'},
  { title: 'HLS4ML', url: 'https://fastmachinelearning.org/hls4ml/'},
  { title: 'FastML Tutorial Medium', url: 'https://medium.com/@forelliryan/deploying-neural-networks-for-in-situ-inference-on-frame-grabber-fpgas-in-high-speed-imaging-6201557fdabc'},
]" :columns="5" />
