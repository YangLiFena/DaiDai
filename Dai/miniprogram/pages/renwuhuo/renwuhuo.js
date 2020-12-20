const db = wx.cloud.database();
const print = db.collection('print');
Page({
  data: {
    tasks: [],
    tasks1: [],
    tasks2: [],
    skip: 0
  },
  onLoad: function(options) {
    this.getData();
  },
  onReachBottom: function() {
    this.getData()
  },
  onPullDownRefresh: function() {
    this.data.tasks = []
    this.data.skip = 0
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
    print.skip(this.data.skip).get().then(res => {
      console.log(res)
      let oldData = this.data.tasks
      var i;
      this.setData({
        tasks: oldData.concat(res.data)
      },res => {
        this.data.skip = this.data.skip + 20
        wx.hideLoading()
        callback();
      })
      for(i = 0; i < res.data.length; i++)
      {
        // if(res.data[i]._id == "3dfe72d65fb244b500dc5ec719dbba98") 
        // {
        //   this.setData({
        //     tasks: res.data[i]
        //   }, res => {
        //     callback()
        //   })
        // }
        if(res.data[i].orderType == "带人")
        {
          this.setData({
            tasks1: res.data[i]
          }, res => {
            callback()
          })
        }
        else if(res.data[i].orderType == "打印")
        {
          this.setData({
            tasks2: res.data[i]
          }, res => {
            callback()
          })
        }
      }
    })
  },
})