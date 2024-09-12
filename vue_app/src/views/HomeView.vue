<template>
  <div class="home">
    
    <div class="columns is-mobile grid-xl">
      <div class="column is-flex is-flex-direction-column is-align-items-center">
        <div class="">29.09.2022</div>
        <figure class="image is-3by2"><img src="" alt=""></figure>
        <div class="text-centered">inference</div>
      </div>
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
      formData: {
        image: null, // For storing the selected image
      },
    };
  },
  methods: {
    onFileChange(event) {
      this.formData.image = event.target.files[0]; // Store the file in formData
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
  },
};
</script>
