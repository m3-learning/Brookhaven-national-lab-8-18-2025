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
layout: main
titleText: Research Philosophy
---

<div style="position: relative; width: 600px; height: 600px; margin: auto;">

  <!-- Circle 1: Epitaxial Complex Oxide Synthesis -->
  <div style="
    position: absolute;
    top: 0;
    left: 50px;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    background: url('/path/to/oxide.jpg') center/cover no-repeat;
    border: 2px solid black;
    opacity: 0.8;
  ">
    <div style="
      position: absolute;
      top: 20px;
      width: 100%;
      text-align: center;
      font-weight: bold;
    ">
      <h2 style="font-size: 24px;">Epitaxial Complex<br>Oxide Synthesis</h2>
    </div>
  </div>

  <!-- Circle 2: Multidimensional Spectroscopy -->
  <div style="
    position: absolute;
    top: 0;
    left: 250px;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    background: url('/path/to/spectroscopy.jpg') center/cover no-repeat;
    border: 2px solid black;
    opacity: 0.8;
  ">
    <div style="
      position: absolute;
      top: 120px;
      width: 100%;
      text-align: center;
      font-weight: bold;
      color: black;
    ">
      Multidimensional<br>Spectroscopy
    </div>
  </div>

  <!-- Circle 3: Machine Learning -->
  <div style="
    position: absolute;
    top: 150px;
    left: 50px;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    background: url('/path/to/ml.jpg') center/cover no-repeat;
    border: 2px solid black;
    opacity: 0.8;
  ">
    <div style="
      position: absolute;
      top: 120px;
      width: 100%;
      text-align: center;
      font-weight: bold;
      color: black;
    ">
      Machine Learning
    </div>
  </div>

  <!-- Circle 4: Heterogeneous Computing -->
  <div style="
    position: absolute;
    top: 150px;
    left: 250px;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    background: url('/path/to/computing.jpg') center/cover no-repeat;
    border: 2px solid black;
    opacity: 0.8;
  ">
    <div style="
      position: absolute;
      top: 120px;
      width: 100%;
      text-align: center;
      font-weight: bold;
      color: black;
    ">
      Heterogeneous<br>Computing
    </div>
  </div>

</div>
