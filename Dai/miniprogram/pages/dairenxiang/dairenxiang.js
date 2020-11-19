const db = wx.cloud.database();
const print = db.collection('print');
Page({
  data: {
    tasks1: {},
  },
  onLoad: function(options) {
    this.getData();
  },
  getData: function(callback) {
    if(!callback) {
      callback = res => {}
    }
    print.get().then(res => {
      console.log(res)
      var i;
      for(i = 0; i < res.data.length; i++)
      {
        if(res.data[i]._id == "d52d5a735fb13e2800ad54bc4ae6b3f2")
        {
          this.setData({
            tasks1: res.data[i]
          }, res => {
            callback()
          })
        }
      }
    })
  },
})