---
layout: ncolumns
titleText: "Cross Validation: 10M Training Images"
columns: 3
images:
  - sym/10m/10m-training-01.svg
  - sym/10m/10m-validation-01.svg
  - sym/10m/10m-atom-01.svg
titles:
  - "Training"
  - "Validation"
  - "Cross Validation"
titleClicks: [0, 1, 2]
columnWidths: [1,1,1]
textboxHeight: 15
mainHeight: 60
---

<template #col0-text>
<div class="text-center text-sm">
  Training data is used to fit the model parameters
</div>
</template>

<template #col1-text>
<div class="text-center text-sm">
  Validation data helps tune hyperparameters and prevent overfitting
</div>
</template>

<template #col2-text>
<div class="text-center text-sm">
  K-fold cross validation provides more robust performance estimates
</div>
</template>

<template #text>
<div class="text-left">
  <ul class="list-disc pl-4">
    <li>Cross Validation</li>
  </ul>
</div>
</template>
