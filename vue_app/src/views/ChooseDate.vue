<template>
  <!-- Date and Diagnosis Grid -->
  <div class="container mt-6 has-text-centered full-height">
    <div class="tile is-ancestor is-justify-content-center">
      <div class="tile is-parent" v-for="record in records" :key="record.id">
        <article class="tile is-child box" :class="{'has-background-danger': record.diagnosis === 'pneumonic', 'has-background-success': record.diagnosis === 'non-pneumonic'}">
          <p class="title has-text-white">{{ record.date }}</p>
          <p class="subtitle has-text-white">{{ record.diagnosis }}</p>
        </article>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  justify-content: center;
}
.tile.is-ancestor {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 1rem;
}
.tile .box {
  cursor: pointer;
  width: 220px;
  min-height: 140px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  border-radius: 8px;
}
.full-height {
  min-height: 50vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

<script>
export default {
  name: 'ChooseDate',
  data() {
    return {
      records: [
        { id: 1, date: "01-01-2024", diagnosis: "pneumonic" },
        { id: 2, date: "28-01-2024", diagnosis: "non-pneumonic" },
        { id: 3, date: "15-02-2024", diagnosis: "non-pneumonic" },
        { id: 4, date: "14-04-2024", diagnosis: "non-pneumonic" }
      ]
    };
  }
};
</script>
