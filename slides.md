---
# You can also start simply with 'default'
theme: ./slide-dev-template/slidev/theme
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
title: Add Title Here
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
---

# 🧠🔩 Chem-AIstry in Motion: Fast Science, Faster Learning – Beyond Equilibrium Synthesis, Powered by ML, FPGAs, and Kubernetes

## Joshua C. Agar

## Drexel University

## Department of Mechanical Engineering and Mechanics

## {{ new Date().toLocaleDateString() }}

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
src: ./slides/datafed/datafed-infrastructure.md
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
layout: main-custom-layout
titleText: "Pulsed Laser Deposition GUI"
mainHeight: 70
textboxHeight: 0
---

<iframe src="/file.html" height="100%" style="aspect-ratio: 1/1;"></iframe>

---
src: ./slides/phys-ml-introduction/phys-ml.md
---

---
src: ./slides/4dstem/4dstem.md
---