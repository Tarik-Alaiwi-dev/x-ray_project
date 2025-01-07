<template>
    <div class="login">
      <div class="columns is-mobile grid-xl">
        <div class="column is-flex is-flex-direction-column is-align-items-center">
          <div class="is-size-4 has-text-weight-bold">Login</div>
          <form @submit.prevent="submitLoginForm" class="is-flex is-flex-direction-column is-align-items-center mt-4">
            <div class="field">
              <label class="label">Username</label>
              <div class="control">
                <input 
                  class="input" 
                  type="username" 
                  v-model="formData.username" 
                  placeholder="Enter your username" 
                  required />
              </div>
            </div>
            <div class="field">
              <label class="label">Password</label>
              <div class="control">
                <input 
                  class="input" 
                  type="password" 
                  v-model="formData.password" 
                  placeholder="Enter your password" 
                  required />
              </div>
            </div>
            <div class="field is-flex is-justify-content-center">
              <button class="button is-primary" type="submit">Login</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "LoginView",
    data() {
      return {
        formData: {
          email: "",
          password: ""
        },
      };
    },
    methods: {
      async submitLoginForm() {
        axios.defaults.headers.common['Authorization'] = "";
        localStorage.removeItem('token');

        const formData = {
            username: this.formData.username,
            password: this.formData.password
        }

        await axios
                .post("http://localhost:8000/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)
                    
                    axios.defaults.headers.common["Authorization"] = "Token " + token

                    localStorage.setItem("token", token)

                    const toPath = this.$route.query.to || '/'

                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            // this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        // this.errors.push('Something went wrong. Please try again')
                        
                        console.log(JSON.stringify(error))
                    }
                })

      },
    },
  };
  </script>
  
  <style scoped>
  .login {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .field {
    margin-bottom: 1rem;
  }
  
  .input {
    width: 300px;
  }
  
  .button {
    width: 100%;
  }
  </style>
  