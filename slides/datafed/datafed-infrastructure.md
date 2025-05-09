---
layout: ncolumns
titleText: "DataFed Infrastructure"
columns: 2
images:
  - facilities/lehigh-cluster.png
  - null
titles:
  - null
  - "Ideal Computational Infrastructure"
titleClicks: [0, 1]
columnWidths: [1.5, 2]
textboxHeight: 0
mainHeight: 75
---

<template #col0>
**DataFed** is a federated research data management platform. This column shows a text-only explanation.
</template>

<template #col1>
<div v-click="1"  class="flex flex-col h-full">
  <div v-click="1" class="text-left gap-4 flex-1">
    <ul class="list-disc pl-4">
      <li>Distributed storage across facilities</li> 
      <li>At least moderate performance</li>
      <li>Globus Connect Server</li>
      <li>Open ports 50000-51000</li>
    </ul>
  </div>
  <div v-click="2" class="flex-1 flex justify-center items-center">
    <div class="flex flex-col items-center">
      <img src="/public/icon/storj.svg" class="h-[100px] object-contain" alt="Lehigh Cluster" />
      <h3>StorJ</h3>
    </div>
  </div>
</div>

</template>