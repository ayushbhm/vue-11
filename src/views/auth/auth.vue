<template>
  <div class="auth-container">
    <h1>Login</h1>
    <form @submit.prevent="login">
      <div>
        <label for="username">Username:</label>
        <input type="text" v-model="username" id="username" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" id="password" required />
      </div>
      <button type="submit">Login</button>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script>
import authService from '/mad 2 housing/frontend/src/services/authService'; 
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  name: 'Auth',
  setup() {
    const username = ref('');
    const password = ref('');
    const errorMessage = ref('');
    const router = useRouter();

    const login = async () => {
      try {
        const { access_token } = await authService.login(username.value, password.value);
        localStorage.setItem('token', access_token); 
        console.log(access_token) 
      } catch (error) {
        errorMessage.value = error.message; 
      }
    };

    return {
      username,
      password,
      errorMessage,
      login,
    };
  },
};
</script>

<style scoped>
.auth-container {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
}

.error {
  color: red;
  text-align: center;
}
</style>
