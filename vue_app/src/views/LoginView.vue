<template>
  <div class="login full-height">
    <div class="columns is-mobile grid-xl">
      <div class="column is-flex is-flex-direction-column is-align-items-center">
        <div class="is-size-4 has-text-weight-bold">Login</div>
        <form @submit.prevent="submitLoginForm" class="is-flex is-flex-direction-column is-align-items-center mt-4">
          <div class="field">
            <label class="label">Username</label>
            <div class="control">
              <input class="input" type="text" v-model="formData.username" placeholder="Enter your username" required />
            </div>
          </div>
          <div class="field">
            <label class="label">Password</label>
            <div class="control">
              <input class="input" type="password" v-model="formData.password" placeholder="Enter your password" required />
            </div>
          </div>
          <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
          <div class="field is-flex is-justify-content-center">
            <button class="button is-primary" type="submit" :disabled="loading">
              {{ loading ? "Logging in..." : "Login" }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapMutations } from "vuex";

export default {
  data() {
    return {
      formData: {
        username: "",
        password: ""
      },
      errorMessage: "",
      loading: false
    };
  },
  methods: {
    ...mapMutations(["setToken"]), // ✅ Use Vuex mutation

    async submitLoginForm() {
      this.errorMessage = "";
      this.loading = true;

      try {
        axios.defaults.headers.common["Authorization"] = "";
        localStorage.removeItem("token");

        const response = await axios.post("http://localhost:8000/api/v1/token/login/", this.formData);
        const token = response.data.auth_token; // ✅ Ensure the correct key is used

        this.setToken(token); // ✅ Store in Vuex
        axios.defaults.headers.common["Authorization"] = "Token " + token;

        this.$router.push("/"); // ✅ Redirect to home page
      } catch (error) {
        this.errorMessage = "Invalid username or password";
        console.error("Login error:", error.response?.data || error);
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
.error {
  color: red;
  font-size: 14px;
}
</style>
