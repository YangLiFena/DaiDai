// miniprogram/pages/alltasks/alltasks.js
const db = wx.cloud.database();
const app=getApp()
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
    "userInfo": null,
    quanbu: "border-bottom: 3px solid #EF4143;color:#EF4143;font-weight:bold",
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var userInfo = wx.getStorageSync("userInfo");
    console.log(app.globalData)
    this.setData({
      "userInfo": userInfo
    })
    this.getMsg(0);
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

  item: function (options) {
    this.getMsg();
  },
  //获取数据库信息
  getMsg() {
    var that = this;
    const _=db.command
    db.collection('print').where({
      status:"待接单",
      orderType:_.neq('打印')//任务大厅无打印单
    }).get({
      success: function(res) {
        res.data.reverse()//最近发单的在上面
       that.setData({ data: res.data });
      }
    })
  },
  //订单详情
  detail: function (options) {
    console.log(options)
    var id = options.currentTarget.dataset.id;
    console.log(id);
    db.collection('print').doc(id).get({
      success: function(res) {
        console.log(res)
        var d=res.data.orderType
        switch(d){
          case "打印":
            wx.navigateTo({
            url: `../dayinxiang/dayinxiang?id=${id}`,
          })
          break;
          case "带人":
            wx.navigateTo({
            url: `../dairenxiang/dairenxiang?id=${id}`,
          })
          break;
          case "带货":
            wx.navigateTo({
            url: `../daihuoxiang/daihuoxiang?id=${id}`,
          })
          break;
        }
      }
    })
  },
  takeOrder: function (options) {
    var that=this
    var id = options.currentTarget.dataset.id;
    console.log(id);
    var myid=app.globalData.OPEN_ID
    db.collection('print').doc(id).update({
      data: {
        status: "已接单",
        orderTaker:myid
      },
      success: function(res) {
        console.log(res)
      }
    })
    wx.showModal({
      title: '提示',
      content: '接单成功！',
      showCancel:false,
      success: function (res) {
        if (res.confirm) {
          console.log('用户点击确定')
          that.onLoad()//刷新页面
        }
      }
    })
  },
  contact: function() {
    wx.redirectTo({
      url: '../im/room/room',
    })
  }
})