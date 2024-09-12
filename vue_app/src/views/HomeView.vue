<template>
  <div class="home">
    
    <div class="columns is-mobile grid-xl">
      <div class="column is-flex is-flex-direction-column is-align-items-center">
        <div class="">{{ formatDate(object.date) }}</div>
        <figure class="image is-3by2"><img :src="`${object.image}`"></figure>
        <div class="text-centered">inference</div>
      </div>
      <img :src="`${object.image}`">
      <div class="column is-flex is-flex-direction-column is-align-items-center">
        <div class="">TODAY</div>
        <form @submit.prevent="submitForm">
        <input type="file" @change="onFileChange" required />
        <button class="button is-active" type="submit">Submit</button>
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
        const response = await axios.post('http://localhost:8000/api/v1/submit-form/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data', // Set multipart header
          },
        });
        console.log('Form submitted successfully:', response.data);
      } catch (error) {
        console.error('Error submitting the form:', error.response.data);
      }
    },

    formatDate(dateString) {
      const date = new Date(dateString);
      const day = String(date.getDate()).padStart(2, '0');
      const month = String(date.getMonth() + 1).padStart(2, '0'); // Months are zero-based
      const year = date.getFullYear();
      return `${day}-${month}-${year}`;
    },

  },
};
</script>
