const db = wx.cloud.database();
const print = db.collection('print');
Page({
  data: {
    tasks: {},
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
      }
    })
  },
})