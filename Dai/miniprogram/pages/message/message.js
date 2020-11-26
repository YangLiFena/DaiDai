const db = wx.cloud.database();
const renyuan = db.collection('renyuan');
const users = db.collection('Users')
const app = getApp()
var sno1
var sno2
var roomId
Page({
  data: {
    tasks: [],
  },
  pageData: {
    skip: 0,
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
  urlTurn: function(options) {
    console.log(options.currentTarget.dataset.id)
    var id = options.currentTarget.dataset.id;
    renyuan.get().then(res => {
      var i;
      for(i = 0; i < res.data.length; i++)
      {
        if(res.data[i]._id == id)
        {
          sno1 = res.data[i].sno
        }
      }
    })
    console.log('--------')
    console.log(app.globalData)
    users.get().then(res => {
      var i;
      for(i = 0; i < res.data.length; i++)
      {
        if(res.data[i]._openid == app.globalData.OPEN_ID)
        {
          sno2 = res.data[i].sno
        }
      }
    })
    console.log(sno1)
    console.log(sno2)
    if(sno1 > sno2)
    {
      roomId = sno2 + sno1
    }
    else
    {
      roomId = sno1 + sno2
    }
    wx.redirectTo({
      url: `../im/room/room?roomId=${roomId}`,
    })
  }
})