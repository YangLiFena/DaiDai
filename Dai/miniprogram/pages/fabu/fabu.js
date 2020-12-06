// pages/identity/identity.js
const db = wx.cloud.database()
Page({
  data: {
    
  },

  jmpDaiFanPage:function(options){ 
    //console.log(1);
    wx.navigateTo({
      url: '../daifan/daifan'
    })
  },
  jmpDaiRenPage:function(options){ 
    //console.log(1);
    wx.navigateTo({
      url: '../dairen/dairen'
    })
  },
  jmpDaiDYPage:function(options){ 
    //console.log(1);
    wx.navigateTo({
      url: '../daying/daying'
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },
  send: function() {
    wx.requestSubscribeMessage({
      tmplIds: ['RD1ESmvxwfPh4hS_If6EQuLFcC5W4Yn9j2ndfy4ZqN0', 'sEX6_fydKEFlqrHXh3j2H0fJAGc3wSqjMK25ABVxOmo'],
      success (res) { }
    })
    wx.cloud.callFunction({
      name: "cancel_order",
      data: {}
    }).then(res => {
      console.log("推送消息成功", res)
    }).catch(res => {
      console.log("推送消息失败", res)
    })
  }
})