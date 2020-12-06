// pages/identity/identity.js
const db = wx.cloud.database()
Page({
  data: {
    animation1: {},
    "hiddent": true,
    "imageHidden":true,
    name:'',
    sid:'',
    shenfenHidden:false,
    studentCardHidden:false
  },
  nameInput:function(e)
  {
    this.setData({
      name: e.detail.value
    });
  },
  sid:function(e)
  {
    this.setData({
      sid: e.detail.value
    });
  },
  addStudent:function(){
    //放入数据库
      db.collection('StudentCard').add({
      data: {
        name:this.data.name,
        sid:this.data.sid
      },
      success: function(res) {
        console.log(res)
      }
    })
  },
  jmpHomePage:function(options){ 
    //console.log(this.data.name);
    this.addStudent();
    wx.switchTab({
      url: '../mine/mine'
    })
  },
  getStudentCard:function(options){
    //获取学生证图片
    var that = this;
    wx.chooseImage({
      count: 1,
      success: function (res) {
        console.log(res)
        that.setData({ getStudentCard: res.tempFilePaths[0], studentCardHidden:true});
      },
    })
  },
  //输入错误提示
  warning: function () {
    var that = this;
    //动画
    var animation = wx.createAnimation({
      duration: 200,
      timingFunction: "ease-in-out",
      delay: 0
    });
    //显示
    that.setData({ "hiddent": false })
    //开始动画，导入动画
    animation.translateY(-60).step();
    that.setData({ "animation1": animation.export() })
    setTimeout(function () {
      that.setData({ "hiddent": true })
      animation.translateY(0).step();
      that.setData({ "animation1": animation.export() })
    }, 1500)
  },
  fail: function (res) {
    console.log(res.errMsg)
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

  }
})