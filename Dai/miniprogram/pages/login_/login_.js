// pages/login.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    type: "wechat",
    userInfo:{},
    showAuth:false,
  },

  auth:function(e){
   // var userInfo = JSON.stringify(e.detail.userInfo);
   //console.log(userInfo);
    this.setData({
      userInfo: e.detail.userInfo,
      showAuth:false
    });

  },

  /**
   * 生命周期函数--监听页面加载
   */
  //在页面加载完成时调用
 
  onGetUserInfo: function(e) {
    const db = wx.cloud.database();
    const users = db.collection("Users")
console.log(e)
    if (e.detail.userInfo) {
      db.collection('Users').add({
        // data 字段表示需新增的 JSON 数据
        data: {
          name:e.detail.userInfo.nickName,
          head_picture:e.detail.userInfo.avatarUrl,
          sex:e.detail.userInfo.gender,
        },

        success: function(res) {
          // res 是一个对象，其中有 _id 字段标记刚创建的记录的 id
          console.log(res)

        }
      })    

       console.log(this.data.name),
      wx.setStorageSync('login', true)
      wx.redirectTo({
        url: '../identity/identity',
      })
    } else {
      wx.showModal({
        title: "提示",
        content: "授权失败，请稍后重试"
      })
    }
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

})