const db = wx.cloud.database();
const print = db.collection('print');
Page({
  data: {
    tasks2: {},
    id: null,
    skip: 0
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
    print.skip(this.data.skip).get().then(res => {
      console.log(res)
      var i;
      for(i = 0; i < res.data.length; i++)
      {
        if(res.data[i]._id == this.data.id)
        {
          this.setData({
            tasks2: res.data[i]
          }, res => {
            callback()
          })
        }
      }
      let temp = this.data.skip
      this.setData({
        skip: temp + 20
      })
    })
  },
})