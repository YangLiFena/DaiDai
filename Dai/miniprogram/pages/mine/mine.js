const APP_ID ='';//输入小程序appid  
const APP_SECRET ='';//输入小程序app_secret  
var app=getApp();
Page({
  data: {
    catelist:[
      {
        id:1,
        image_src: '/photo/w1.png'
      },
      {
        id:2,
        image_src: '/photo/w2.png'
      },
      {
        id:3,
        image_src: '/photo/w3.png'
      }
    ]
  },
  //获取openid 唯一标识用户
  getOpenIdTap:function(){  
    var that=this;  
    wx.login({  
      success:function(res){  
        wx.request({  
            //获取openid接口  
          url: 'https://api.weixin.qq.com/sns/jscode2session',  
          data:{  
            appid:"wxfeb8e7ad8ae25436",  
            secret:"df11ffc0b14db227fcdb368be46cfa38",  
            js_code:res.code,  
            grant_type:'authorization_code'  
          },  
          method:'GET',  
          success:function(res){
            console.log(res.data)  
            app.globalData.OPEN_ID = res.data.openid;//获取到的openid  
            app.globalData.SESSION_KEY = res.data.session_key;//获取到session_key  
          }  
        })  
      }  
    })  
  },
  onLoad: function (options){
  this.getOpenIdTap();
  var that = this;
  // 查看是否授权
  wx.getSetting({
  success(res) {
  if (res.authSetting['scope.userInfo']) {
  // 已经授权，可以直接调用 getUserInfo 获取头像昵称
  wx.getUserInfo({
  success: function (res) {
  console.log(res)
  // console.log(res.userInfo)
  that.setData({
  nickName: res.userInfo.nickName, //昵称
  avatarUrl: res.userInfo.avatarUrl //头像
  })
  }
  })
  }else{
  wx.redirectTo({
  url: '/pages/login_/login_', //跳转到授权页面
  })
  }
  }
  })
  }
})

