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

