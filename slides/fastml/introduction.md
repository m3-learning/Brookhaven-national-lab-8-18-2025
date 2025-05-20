---
layout: main-custom-layout
titleText: "Timing is Everything"
mainHeight: 75
textboxHeight: 0
---

<CrossfadeImages :images="[
    'fastml/superbowl-superbowllii.gif',
    'fastml/saquon-saquon-barkley.gif',
    ]" class="w-[200%] h-[200%] object-cover" />

---
layout: main-custom-layout
titleText: "Compact Muon Solenoid at the Large Hadron Collider"
mainHeight: 75
textboxHeight: 0
references: Slide Courtesy Nhan Tran FermiLab
---

<CrossfadeImages :images="[
    'fastml/CMS-m1.png',
    'fastml/CMS.png',
    ]"/>

---
layout: main-custom-layout
titleText: "HLS4ML : Real-Time ML on FPGAs"
mainHeight: 55
textboxHeight: 0
---

<CrossfadeImages :images="[
    'fastml/hls4ml.jpg',
    ]"/>

<template #text>
  <div class="text-left">
    <ul class="list-disc pl-4">
      <li>Accessible/usable codesign workflow; open-source, targets multiple devices</li>
      <li>Support for reduced precision and pruning</li>
      <li>Spatial dataflow architectures for low latency</li>
    </ul>
  </div>
</template>

---
layout: main-custom-layout
titleText: "From Static to Dynamic Control"
mainHeight: 55
textboxHeight: 0
reference: Slide Courtesy Nhan Tran FermiLab
---
<!-- references: "Google Deep Mind: Degrave, J., Felici, F., Buchli, J. et al. Magnetic control of tokamak plasmas through deep reinforcement learning. Nature 602, 414–419 (2022). https://doi.org/10.1038/s41586-021-04301-9" -->

<CrossfadeImages :images="[
    'fastml/plasma-control.gif',
    ]"/>

<template #text>
  <div class="text-left">
    <ul class="list-disc pl-4">
      <li> We need ML control systems to control dynamic non-equilibrium processes in materials manufacturing</li>
    </ul>
  </div>
</template>