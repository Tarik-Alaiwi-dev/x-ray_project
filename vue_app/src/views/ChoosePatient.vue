<template>
    <!-- Patient Grid -->
    <div class="container mt-6 has-text-centered full-height">
      <div class="tile is-ancestor is-justify-content-center">
        <div class="tile is-parent" v-for="patient in patients" :key="patient.id">
          <article class="tile is-child box">
            <p class="title has-text-grey-dark">{{ patient.name }}</p>
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
    width: 200px; /* Adjust width as needed */
    min-height: 120px; /* Ensures all tiles have the same height */
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #f5f5f5;
  }

  .full-height {
  min-height: 50vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
  </style>
  
  
  
  
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
        patients: [
          { id: 1, name: "John Doe" },
          { id: 2, name: "Jane Smith" },
          { id: 3, name: "Michael Johnson" },
          { id: 4, name: "Emily Brown" }
        ],
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
  