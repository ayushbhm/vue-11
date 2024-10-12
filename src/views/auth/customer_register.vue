<template>
  <div class="register-container">
    <h1>Customer Registration</h1>
    <form @submit.prevent="register" class="registration-form">
      <div>
        <label for="username">Username:</label>
        <input type="text" v-model="username" id="username" required />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" id="email" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" id="password" required />
      </div>
      <div>
        <label for="phone">Phone:</label>
        <input type="text" v-model="phone" id="phone" required />
      </div>
      <div>
        <label for="address">Address:</label>
        <input type="text" v-model="address" id="address" />
      </div>
      <div>
        <label for="pincode">Pincode:</label>
        <input type="text" v-model="pincode" id="pincode" />
      </div>
      <button type="submit">Register</button>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      <p v-if="successMessage" class="success">{{ successMessage }}</p>
    </form>
  </div>
</template>

<script>
import authService from '../../services/authService'; 
import { ref } from 'vue';

export default {
  name: 'CustomerRegister',
  setup() {
    const username = ref('');
    const email = ref('');
    const password = ref('');
    const phone = ref('');
    const address = ref('');
    const pincode = ref('');
    const errorMessage = ref('');
    const successMessage = ref('');

    const register = async () => {
      try {
        const response = await authService.register({
          username: username.value,
          email: email.value,
          password: password.value,
          phone: phone.value,
          address: address.value,
          pincode: pincode.value,
        });
        successMessage.value = response.message; 
      } catch (error) {
        errorMessage.value = error.message; 
        successMessage.value = ''; 
      }
    };

    return {
      username,
      email,
      password,
      phone,
      address,
      pincode,
      errorMessage,
      successMessage,
      register,
    };
  },
};
</script>

<style>
html, body {
  background-color: black;
  height: 100%;
  margin: 0;
  padding: 0;
}

.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;  
  height: 100%; 
  padding: 20px; 
  border-radius: 0; 
  background-color: rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 20px 5px rgb(144, 86, 221);
}
</style>
