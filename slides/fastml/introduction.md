---
layout: main-custom-layout
titleText: "Timing is Everything"
mainHeight: 80
textboxHeight: 0
---

<CrossfadeImages :images="[
    'fastml/superbowl-superbowllii.gif',
    'fastml/saquon-saquon-barkley.gif',
    ]" />

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
reference: "Fast Machine Learning Lab - https://fastmachinelearning.org/"
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

