---
layout: main-custom-layout
titleText: "Ferroelectric Thin Films"
mainHeight: 80
textboxHeight: 0
---

<script setup>
import { computed } from 'vue'
const clicks = computed(() => $slidev.nav.clicks)
</script>

<!-- Invisible divs for click increments -->
<v-click><div /></v-click>
<v-click><div /></v-click>
<v-click><div /></v-click>

<div class="relative w-full h-full">
  <!-- Image 1: Visible on click 1, hidden after click 2 -->
  <img
    src="/pld-schematic/PLD-Schematic-All-m2.svg"
    class="absolute inset-0 m-auto max-w-full max-h-full object-contain transition-opacity duration-500"
    :class="clicks >= 1 && clicks < 2 ? 'opacity-100' : 'opacity-0'"
  />

  <!-- Image 2: Visible on click 2, hidden after click 3 -->
  <img
    src="/pld-schematic/PLD-Schematic-All-m1.svg"
    class="absolute inset-0 m-auto max-w-full max-h-full object-contain transition-opacity duration-500"
    :class="clicks >= 2 && clicks < 3 ? 'opacity-100' : 'opacity-0'"
  />

  <!-- Image 3: Visible from click 3 onwards -->
  <img
    src="/pld-schematic/PLD-Schematic-All.svg"
    class="absolute inset-0 m-auto max-w-full max-h-full object-contain transition-opacity duration-500"
    :class="clicks >= 3 ? 'opacity-100' : 'opacity-0'"
  />
</div>
