const db = wx.cloud.database();
const renyuan = db.collection('renyuan');
Page({
  data: {
    tasks: [],
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
    renyuan.skip(this.pageData.skip).get().then(res => {
      console.log(res)
      let oldData = this.data.tasks;
      this.setData({
        tasks: oldData.concat(res.data),
      }, res => {
        this.pageData.skip = this.pageData.skip + 10
        wx.hideLoading()
        callback()
      })
    })
  },
})