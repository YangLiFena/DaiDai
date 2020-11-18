const db = wx.cloud.database();
const print = db.collection('print');
Page({
  data: {
    tasks: {},
    tasks1: {},
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
        if(res.data[i]._id == "3dfe72d65fb244b500dc5ec719dbba98") 
        {
          this.setData({
            tasks: res.data[i]
          }, res => {
            callback()
          })
        }
        else if(res.data[i]._id == "d52d5a735fb13e2800ad54bc4ae6b3f2")
        {
          this.setData({
            tasks1: res.data[i]
          }, res => {
            callback()
          })
        }
        else if(res.data[i]._id == "d52d5a735fb0f6f000a8f02c3c0b07c4")
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