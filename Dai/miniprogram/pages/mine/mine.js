Page({
  data: {
    catelist:[
      {
        id:1,
        image_src: '/photo/w1.png',
        add:"/pages/pingjia/pingjia"
      },
      {
        id:2,
        image_src: '/photo/w2.png',
        add:"/pages/tousu/tousu"
      },
      {
        id:3,
        image_src: '/photo/w3.png',
        add:"/pages/feedback/feedback"
      }
    ],
      ne:[],
  },

  onLoad: function (options) {
    wx.cloud.init();
    const db = wx.cloud.database();
    const users = db.collection("Users")
    users.get({
      success: res => {
        if (res.data.length == 0) {
          wx.redirectTo({
            url: '../login_/login_',
          })
        }
      }
    })
    var _this = this;
    db.collection('Users').get({
      //如果查询成功的话
     success:res =>{     
       //这一步很重要，给ne赋值，没有这一步的话，前台就不会显示值
       this.setData({
        ne:res.data
       })
     }
     })   
  },
  
//   onLoad: function (options)
// {
  
//   var that = this;
//   // 查看是否授权
//   wx.getSetting({
//   success(res) {
//   if (res.authSetting['scope.userInfo']) {
//   // 已经授权，可以直接调用 getUserInfo 获取头像昵称
//   wx.getUserInfo({
//   success: function (res) {
//   console.log(res)
//   // console.log(res.userInfo)
//   that.setData({
//   nickName: res.userInfo.nickName, //昵称
//   avatarUrl: res.userInfo.avatarUrl //头像
//   })
//   }
//   })
//   }else{
//   wx.redirectTo({
//   url: '/pages/login_/login_', //跳转到授权页面
//   })
//   }
//   }
//   })
//   }
})

