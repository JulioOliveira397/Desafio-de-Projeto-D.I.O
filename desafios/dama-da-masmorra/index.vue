<template>
  <div>
    <input v-model.number="golpes" placeholder="Quantidade de golpes" />
    <button @click="minerar">Minerar</button>
    <ul>
      <li v-for="(mineral, index) in resultados" :key="index">
        {{ index + 1 }}: {{ mineral }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const golpes = ref(0)
const resultados = ref([])

const minerais = ["", "Carvao", "Ferro", "Diamante", "Pedra"]
function minerar() {
  resultados.value = []
  for (let i = 1; i <= golpes.value; i++) {
    let index = i % 4 || 4
    resultados.value.push(minerais[index])
  }
}
</script>
