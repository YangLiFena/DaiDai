const db = wx.cloud.database();
const Users = db.collection('Users');
const app=getApp()
Page({
  data: {
    num: 0,
    value: 5,
    tasks: []
  },
  pageData: {
    skip: 0
  },
  onLoad: function(options) {
    this.getData();
  },
  onReachBottom: function(options) {
    this.getData();
  },
  onPullDownRefresh: function() {
    this.data.tasks = []
    this.pageData.skip = 0
    this.getData(res => {
      wx.stopPullDownRefresh();
    })
  },
  getData: function(callback) {
    if(!callback) {
      callback = res => {}
    }
    wx.showLoading({
      title: '数据加载中',
    })
    const _ = db.command

    Users.skip(this.pageData.skip).where({
      _openid: app.globalData.OPEN_ID
    }).get().then(res => {
      let oldData = this.data.tasks;
      var d=res.data[0]
      console.log(d.get)
      var v=parseFloat(0)
      for(var i=0;i<d.get.length;i++){
        v+=parseFloat(d.get[i].points)
      }
      v/=parseFloat(d.get.length)
      console.log(v)
      this.setData({
        tasks: oldData.concat(d.get),
        num: d.get.length,
        value:v
      }, res => {
        this.pageData.skip = this.pageData.skip + 20
        wx.hideLoading()
        callback()
      })
    })
  },
})