<template>
  <div>
    <input v-model="tipo" placeholder="Tipo do item" />
    <input v-model.number="dano" placeholder="Dano" />
    <input v-model.number="resistencia" placeholder="Resistência" />
    <button @click="simular">Simular Combate</button>
    <div v-if="resultado">
      <p>Tipo: {{ tipo }}</p>
      <p>Dano: {{ dano }}</p>
      <p>Resistência: {{ resistencia }}</p>
      <p>Dano em combate: {{ resultado }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const tipo = ref('')
const dano = ref(0)
const resistencia = ref(0)
const resultado = ref(null)

function simular() {
  resultado.value = tipo.value.toLowerCase() === 'arma' ? dano.value * 2 : dano.value
}
</script>
