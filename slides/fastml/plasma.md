---
layout: main-custom-layout
titleText: "From Static to Dynamic Control"
mainHeight: 55
textboxHeight: 0
reference: "Google Deep Mind: Degrave, J., Felici, F., Buchli, J. et al. Magnetic control of tokamak plasmas through deep reinforcement learning. Nature 602, 414–419 (2022). https://doi.org/10.1038/s41586-021-04301-9"
---

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

---
layout: main-custom-layout
titleText: "From Static to Dynamic Control"
mainHeight: 40
textboxHeight: 0
reference: "Collab: Nhan Tran (FermiLabs), Giuseppe Di Guglielmo, Michael E Mauel, Gerald A Navratil (Columbia)"
---

<CrossfadeImages :images="[
  'fastml/plasma/GPU-version.png',
]"/>

<!-- Use two newlines to force a paragraph block -->
  
::text::
- Inference latency too high ($\mathcal{O}$(100 $\mu$s))
- Non-deterministic inference latency
- At least two PCIe hops ($\mathcal{O}$(1ms)) 
- Low power efficiency for remote inference

---
layout: main-custom-layout
titleText: "Experimental Setup"
mainHeight: 55
textboxHeight: 0
reference: "Collab: Nhan Tran (FermiLabs), Giuseppe Di Guglielmo, Michael E Mauel, Gerald A Navratil (Columbia)"
---

<CrossfadeImages :images="[
  'fastml/plasma/camera-setup.png',
]"/>

::text::
- Two Phantom Vision cameras capable of 100,000 fps
- Direct optical imaging of tokamak plasma

---
layout: main-custom-layout
titleText: "FPGA Block Diagram"
mainHeight: 55
textboxHeight: 0
reference: "Collab: Nhan Tran (FermiLabs), Giuseppe Di Guglielmo, Michael E Mauel, Gerald A Navratil (Columbia)"
---

<CrossfadeImages :images="[
  'fastml/plasma/camera-setup-2.png',
]"/>

::text::
- Data is aquired over CoaXPress --> Custom Logic ML Inference --> FPGA --> Control Signals

---
layout: ncolumns
titleText: "Timing and Synchronization"
columns: 2
images:
  - fastml/plasma/tokamak-plasma-timing.png
  - null
titleClicks: [1, 2]
columnWidths: [1, 1]
textboxHeight: 0
mainHeight: 70
reference: "Collab: Nhan Tran (FermiLabs), Giuseppe Di Guglielmo, Michael E Mauel, Gerald A Navratil (Columbia)"
roundedEdges: false
---

::col1::
1. 0.3 ns single CPU clock cycle
2. 0.1-0.2 μs reading 1 MB block from RAM 
3. 0.1-0.5 μs PCIe hop
4. 100 μs – 1 ms reading 1 MB block from NVMe
5. 0.1 ms – 1 ms local network ping
6. 10 ms – 20 ms reading 1 MB block from spinning disk 

---
layout: main-custom-layout
titleText: "FPGA Block Diagram"
mainHeight: 60
textboxHeight: 0
---

<CrossfadeImages :images="[
  'fastml/plasma/pareto.svg',
]"/>

::text::
- How do you efficiently achieve a good tradeoff between latency (power), and accuracy?


