Page({
  success:function(options){
    wx.navigateTo({
        url: '../fabu/fabu',
      })
    wx.showToast({
      title: '发布成功',
      icon: 'success',
      duration: 2000//持续的时间
    })
    }
  })