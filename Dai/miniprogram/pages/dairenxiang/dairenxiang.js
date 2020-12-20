const db = wx.cloud.database();
const print = db.collection('print');
Page({
  data: {
    tasks1: {},
    id: null
  },
  onLoad: function(options) {
    console.log(options.id)
    this.setData({
      id: options.id
    })
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
        if(res.data[i]._id == this.data.id)
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