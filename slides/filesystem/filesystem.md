---
layout: main-custom-layout
titleText: "Typical File System Archive"
mainHeight: 80
textboxHeight: 0
---

<script setup>
import filetree from './filetree.json'
</script>

<div class="w-full h-full">
<RecursiveFileTree :node="filetree" />
</div>
