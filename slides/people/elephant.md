---
layout: center
---
<div class="flex flex-col items-center justify-center">
  <h2 class="text-2xl mb-4">Make a photorealistic image of an empty room with absolutely no elephant in the room</h2>
  <img v-click="1" src="/public/elephant.png" class="h-[400px] object-contain" alt="Elephant" />
</div>

---
layout: center
---
<div class="flex flex-col items-center justify-center">
  <img src="/public/mordac.jpg" class="h-[400px] object-contain" alt="Mordac" />
</div>

---
layout: ncolumns
titleText: "DataFed Infrastructure"
columns: 2
images:
  - null
  - null
titles:
  - null
  -null
columnWidths: [1,1]
textboxHeight: 30
mainHeight: 65
<!-- showBorders: true -->
spacerHeight: 0
headingRowHeight: 0
---

<template #col0>
<div v-click="0" class="grid grid-rows-3 gap-4">
  <div class="flex flex-col items-center justify-center">
```mermaid
graph LR
    A[Can I get a Static IP with open ports?] --> B[Submit a ticket]
    B --> C[Denial]
```
  </div>

  <div v-click="1" class="flex flex-col items-center justify-center">
```mermaid
graph LR
    A[Can I get administrative access for setting up endpoints?] --> B[Submit a ticket]
    B --> C[Denial]
```
  </div>

  <div v-click="2" class="flex flex-col items-center justify-center">
```mermaid
graph LR
    A[Can I publicly share open research data as part of my NSF grant?] --> B[Research data is institutional data, thus you need approval to share it]
    B --> C[No response]
```
  </div>
</div>
</template>

<template #col1>
<div class="grid grid-rows-3 gap-4">
<div v-click="3"  class="flex flex-col items-center justify-center">
```mermaid
graph LR
  A[Can I get jumbo frames and an exclusion for the border firewall?] --> B[No, that would violate our cybersecurity insurance contract]
```
</div>

<div v-click="4"  class="flex flex-col items-center justify-center">
```mermaid
graph LR
  A[Can I share or contribute to an open source package on Github as part of my funded research?] --> B[No, you need approval from the Office of Sponsored Research]
```
</div>

<div v-click="5"  class="flex flex-col items-center justify-center">
```mermaid
graph LR
  A[Can I use federated third party services like DataFed?] --> B[Please submit the very Higher Education Community Vendor Assessment Form]
  B --> C[No response]
```
</div>
</div>
</template>

<template #text>
<div class="text-left">
  <ul class="list-disc pl-4">
    <li v-click="6">University IT folks appear believe their policies supersede federal grant contracts <span v-click="7"> -> even though the grant contract is a legal document</span></li>
    <li v-click="8">This creates friction between researchers, IT folks, and administrators</li>
  </ul>
</div>
</template>
