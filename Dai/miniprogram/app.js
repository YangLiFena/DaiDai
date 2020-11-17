//app.js
App({
  globalData:{
    APP_ID :'',//输入小程序appid  
    APP_SECRET:'',//输入小程序app_secret  
    OPEN_ID:'',//储存获取到openid  
    SESSION_KEY:''//储存获取到session_key  
  },
  onLaunch: function () {
    
    if (!wx.cloud) {
      console.error('请使用 2.2.3 或以上的基础库以使用云能力')
    } else {
      wx.cloud.init({
        env: "sedai-ztfg5",
        traceUser: true,
      })
    }
    this.globalData = {}
    
  },

  

})

