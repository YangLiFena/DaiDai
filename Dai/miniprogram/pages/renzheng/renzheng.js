// pages/renzheng/renzheng.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    loading: false,
    contact: '',
    content: ''
  },

  onclick: function()
  {
    wx.navigateTo({
      url: '/pages/identity/identity',
    })
  }
})