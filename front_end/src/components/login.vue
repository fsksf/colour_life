<template>
  <div class="login">
    <h1>请登录</h1>
    <el-row>
      <el-input v-model="code" placeholder="请输入账号"></el-input>
      <el-input v-model="password" placeholder="请输入账号" show-password></el-input>
      <el-button type="primary" @click="login()">登录</el-button>
      <el-button type="success">注册</el-button>
    </el-row>
  </div>
</template>

<script>
export default {
  data () {
    return {
      code: '',
      password: ''
    }
  },

  methods: {
    login () {
      let postData = {'password': this.password, 'code': this.code}
      console.log(postData)
      this.$axios.post('ServiceApi/login', 
      postData, 
      {headers: {'Content-Type': 'application/json'}}).then(response => {
        console.log('login success')
      })
    }
  }

}
</script>
