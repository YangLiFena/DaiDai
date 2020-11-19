const db = wx.cloud.database();
const print = db.collection('print');
Page({
  data: {
    tasks2: {}
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
        if(res.data[i]._id == "d52d5a735fb0f6f000a8f02c3c0b07c4")
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