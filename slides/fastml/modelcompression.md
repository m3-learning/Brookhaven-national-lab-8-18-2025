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
mainHeight: 55
reference: "Colab: Jane Greenberg (Drexel University)"
roundedEdges: false
---

::col1::
## What Does DataFed TorchFlow Do?

- Preserves script with a checksum.
- Maintains a copy or reference to the training data.
- Extracts the neural network model graph.
- Extracts the optimizer state and hyperparameters.
- Records the Python and hardware environment.
- Allows the addition of any custom metadata.

::text::
- Pip installable python package `pip install datafed_torchflow`
- With a single instantiation provides a drag-and-drop replacement for `model.save()` in PyTorch

---
layout: main-custom-layout
titleText: "Use Case #1 → Model Checkpoints"
mainHeight: 60
textboxHeight: 0
---

<CrossfadeImages :images="[
  'fastml/torchlogger/model-checkpoints.png',
]"/>

::text::
- Model checkpoints and metadata saved as a searchable and indexed graph
  
---
layout: main-custom-layout
titleText: "Use Case #2 --> Training Provenance"
mainHeight: 60
textboxHeight: 0
---

<CrossfadeImages :images="[
  'fastml/torchlogger/model-training-provenance.png',
]"/>

::text::
- Monitoring training and regularization scheduling

---
layout: main-custom-layout
titleText: "Use Case 3 --> Hyperparameter Search"
mainHeight: 60
textboxHeight: 0
---

<CrossfadeImages :images="[
  'fastml/torchlogger/neural-arc-search.png',
]"/>

::text::
- Tracking past training and hyperparameter search

---
layout: main-custom-layout
titleText: "Future Activities: Dose Control in Electron Microscopy"
mainHeight: 70
reference: "Colab: Seda Ogrenci (Northwestern), David Flannigan (Minnesota)"
textboxHeight: 0
---

<CrossfadeImages :images="[
  'fastml/EM.png',
]"/>

