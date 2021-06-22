<template>
  <div class="logon">
    <h1>欢迎注册</h1>
    <el-row>
      <el-input v-model="code" placeholder="请输入账号"></el-input>
      <el-input v-model="password" placeholder="请输入密码" show-password></el-input>
    </el-row>
    <el-row>
      <el-button type="primary" @click="logon()">注册</el-button>
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
    //跳转页面
    login () {
      this.$router.push({path:'/login'})
    },
    logon () {
      let postData = {'password': this.password, 'code': this.code}
      console.log(postData)
      this.$axios.post('ServiceApi/login', postData, {headers: {'Content-Type': 'application/json'}}).then(response => {
        console.log('login success'),

      })
    }
  }
}
</script>
