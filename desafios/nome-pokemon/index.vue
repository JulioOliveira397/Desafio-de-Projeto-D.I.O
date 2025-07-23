<template>
  <div>
    <input v-model="prefixo" placeholder="Prefixo do Pokémon" />
    <button @click="gerarNome">Gerar</button>
    <p v-if="resultado">Nome completo: {{ resultado }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const prefixo = ref('')
const resultado = ref('')

function gerarNome() {
  resultado.value = prefixo.value + 'saur'
}
</script>
