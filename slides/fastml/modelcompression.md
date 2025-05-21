---
layout: main-custom-layout
titleText: "Neural Architecture Search for FastML on FPGAs"
mainHeight: 70
textboxHeight: 0
---

<CrossfadeImages :images="[
  'fastml/FastML-NAS.png',
]"/>

---
layout: ncolumns
titleText: "DataFed TorchFlow"
columns: 2
images:
  - /fastml/torchlogger/datafedTorchflow.png
  - null
titleClicks: [0, 1]
columnWidths: [1, 1]
textboxHeight: 0
mainHeight: 70
reference: "Colab: Jane Greenberg (Drexel University)"
roundedEdges: false
---

::col1::
## What Does DataFed TorchFlow Do?

- It preserves a copy of the script with a checksum.
- It maintains a copy or reference to the training data.
- It extracts the neural network model graph as a dictionary.
- It extracts the optimizer state and hyperparameters.
- It records the Python environment and computer hardware/state.
- It allows the addition of any custom metadata.

