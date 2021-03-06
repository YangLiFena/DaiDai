var app=getApp() 
Page({
  data: {
    catelist:[
      {
        id:1,
        image_src: '/photo/我的评价.png',
        add:"/pages/pingjia/pingjia",
        text: "我的评价"
      },
      {
        id:2,
        image_src: '/photo/投诉.png',
        add:"/pages/tousu/tousu",
        text: "投诉"
      },
      {
        id:3,
        image_src: '/photo/意见反馈.png',
        add:"/pages/feedback/feedback",
        text: "意见反馈"
      },
      {
        id:4,
        image_src: '/photo/任务单.png',
        add:"/pages/renwuhuo/renwuhuo",
        text: "任务单"
      }
    ],
      ne:[],
  },
  onLoad: function (options) {
    var that=this
    const db = wx.cloud.database();
    const users = db.collection("Users")
    wx.login({  
      success:function(res){  
        wx.request({  
            //获取openid接口  
          url: 'https://api.weixin.qq.com/sns/jscode2session',  
          data:{  
            appid:"wx4184fe0dc5886089",  
            secret:"cc2bd71e5125bbb08b79751045e3da32",  
            js_code:res.code,  
            grant_type:'authorization_code'  
          },  
          method:'GET',  
          success:function(res){
            app.globalData.OPEN_ID = res.data.openid;//获取到的openid  
            app.globalData.SESSION_KEY = res.data.session_key;//获取到session_key  
            users.where({
              _openid: res.data.openid
            }).get({
              success: res => {
                if (res.data.length == 0) {
                  wx.redirectTo({
                    url: '../login_/login_',
                  })
                }
              }
            })
            var myid=app.globalData.OPEN_ID
            db.collection('Users').where({
              _openid:myid
            }).get({
             success:res =>{     
               that.setData({
                ne:res.data
               })
               console.log(that.data.ne)
             }
             })   
          }  
        })  
      }  
    })  
    wx.getSetting({
      success (res){
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称
          wx.getUserInfo({
            success: function(res) {
              app.globalData.AVATAR = res.userInfo.avatarUrl;
              app.globalData.NICKNAME = res.userInfo.nickName;
            }
          })
        }
      }
    })
  },
})

