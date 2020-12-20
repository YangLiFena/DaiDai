Page({
  data: {
    catelist:[
      {
        id:1,
        image_src: '/photo/w1.png',
        add:"/pages/appraise/appraise"
      },
      {
        id:2,
        image_src: '/photo/w2.png',
        add:"/pages/complaint/complaint"
      },
      {
        id:3,
        image_src: '/photo/w3.png',
        add:"/pages/feedback/feedback"
      }
    ]
  },
  onLoad: function (options)
{
  
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

