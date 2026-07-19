<template>
  <div class="container">
    <h1>Vue 3 - Reactive List & Filter UI</h1>

    <input
      v-model="search"
      type="text"
      placeholder="Search products..."
      class="search-box"
    />

    <ul>
      <li v-for="item in filteredItems" :key="item.id">
        {{ item.name }} - ₹{{ item.price }}
      </li>
    </ul>

    <p v-if="filteredItems.length === 0">
      No matching products found.
    </p>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

const search = ref("");

const items = ref([
  { id: 1, name: "Laptop", price: 65000 },
  { id: 2, name: "Mouse", price: 800 },
  { id: 3, name: "Keyboard", price: 1500 },
  { id: 4, name: "Monitor", price: 12000 },
  { id: 5, name: "Headphones", price: 2500 },
  { id: 6, name: "Webcam", price: 3200 },
]);

const filteredItems = computed(() => {
  return items.value.filter((item) =>
    item.name.toLowerCase().includes(search.value.toLowerCase())
  );
});
</script>

<style scoped>
.container {
  max-width: 500px;
  margin: 40px auto;
  font-family: Arial, sans-serif;
  text-align: center;
}

.search-box {
  width: 100%;
  padding: 10px;
  margin: 20px 0;
  font-size: 16px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  background: #f4f4f4;
  margin: 8px 0;
  padding: 12px;
  border-radius: 6px;
  font-size: 16px;
}

p {
  color: red;
  font-weight: bold;
}
</style>
