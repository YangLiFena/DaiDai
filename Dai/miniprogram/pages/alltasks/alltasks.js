// miniprogram/pages/alltasks/alltasks.js
const db = wx.cloud.database();
Page({
  data: {
    array: ['默认', '发布时间', '完成时间', '赏金'],
    objectArray: [
      {
        id: 0,
        name: '默认'
      },
      {
        id: 1,
        name: '发布时间'
      },
      {
        id: 2,
        name: '完成时间'
      },
      {
        id: 3,
        name: '赏金'
      }
    ],
    index: 0,
    personal: true,
    "userInfo": null,
    quanbu: "border-bottom: 3px solid #EF4143;color:#EF4143;font-weight:bold",
    details:""
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var userInfo = wx.getStorageSync("userInfo");
    this.setData({
      "userInfo": userInfo
    })
    this.getMsg('getUserOrderList', 0);
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
  personal: function () {
    this.setData({
      personal: false
    })
  }, exit: function () {
    this.setData({
      personal: true
    })
  },
  preview: function () {
    var avatar = this.data.userInfo.avatarUrl;
    wx.previewImage({
      urls: [avatar]
    })
  },
  item: function (options) {
    this.getMsg('getUserOrderList', 0);
  },
  getMsg(xuanxiang, status) {
    console.log(xuanxiang + " --   -- " + status)
    var that = this;
    var userInfo = this.data.userInfo;
    db.collection('print').get({
      success: function(res) {
        // res.data 包含该记录的数据
        if (res.data.length > 0) {
          for (var i = 0; i < res.data.length; i++) {
            
          }
        } else {
          that.setData({ tishi: false });
        }
        that.setData({ data: res.data });
        console.log(res.data)
      }
    })
  },
  //订单详情
  detail: function (options) {
    var id = options.currentTarget.dataset.id;
    console.log(id);
    //TODO
  },
  takeOrder: function (options) {
    var id = options.currentTarget.dataset.id;
    console.log(id);
    db.collection('print').doc(id).update({
      data: {
        // 设为已接单
        status: "已接单"
      },
      success: function(res) {
        console.log(res.data)
      }
    })
    wx.showModal({
      title: '提示',
      content: '接单成功！',
      showCancel:false,
      success: function (res) {
        if (res.confirm) {
          console.log('用户点击确定')
        }
      }
    })
  },
})