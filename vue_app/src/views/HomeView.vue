<template>
  <div class="home">
    
    <div class="columns is-mobile grid-xl">
      <div class="column is-flex is-flex-direction-column is-align-items-center">
        <div class="is-size-4 has-text-weight-bold">{{ formatDate(object.date) }}</div>
        <figure class="image is-3by2"><img :src="`${object.image}`"></figure>
        <img :src="`${object.image}`" class="image is-3by2 mt-4">
        <div v-if="object.inference === 'YOU PROBABLY DO NOT HAVE PNEUMONIA'" class="text-centered mt-6 is-size-4 has-text-weight-bold notification is-success">{{ object.inference }}</div>
        <div v-else class="text-centered mt-6 is-size-4 has-text-weight-bold notification is-danger">{{ object.inference }}</div>
      </div>
      <div class="column is-flex is-flex-direction-column is-align-items-center">
        <div class="is-size-4 has-text-weight-bold">TODAY</div>
        <form @submit.prevent="submitForm" class="is-flex is-flex-direction-column is-align-items-center mt-4">
          <div class="file-input-container p-5">
          <div class="file-input-text">
            DRAG HERE <br> OR <br> CLICK TO SEND
          </div>
          <input type="file" @change="onFileChange" required />
        </div>
      </form>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return {
      object: {},
      formData: {
        image: null, // For storing the selected image
      },
    };
  },
  created() {
    this.fetchData(); // Fetch data when component is created
  },
  methods: {
    onFileChange(event) {
      this.formData.image = event.target.files[0]; // Store the file in formData
      this.submitForm();
    },
    async fetchData() {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/get-form/');
        this.object = response.data; // Store data in the objects array
        console.log(this.objects);
        
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    async submitForm() {
      const formData = new FormData(); // Create FormData object
      formData.append('image', this.formData.image); // Append the image file

      try {
        const response = await axios.post('http://localhost:8000/api/v1/predict/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data', // Set multipart header
          },
        });
        console.log('Form submitted successfully:', response.data);
        location.reload();
      } catch (error) {
        console.error('Error submitting the form:', error.response.data);
      }
    },

    formatDate(dateString) {
      const date = new Date(dateString);
      const day = String(date.getDate()).padStart(2, '0');
      const month = String(date.getMonth() + 1).padStart(2, '0'); 
      const year = date.getFullYear();
      return `${day}-${month}-${year}`;
    },

  },
};
</script>

<style scoped>
    .file-input-container {
      position: relative;
      width: 100%;
      aspect-ratio: 3 / 2; 
      border: 3px dashed #3a4252;
      display: flex;
      justify-content: center;
      align-items: center;
      color: white;
      text-align: center;
    }

    .file-input-container input[type="file"] {
      opacity: 0;
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      cursor: pointer;
    }

    .file-input-text {
      font-size: 1.5rem;
      line-height: 1.5;
      pointer-events: none;
    }
</style>
