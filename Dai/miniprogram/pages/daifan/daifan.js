const db = wx.cloud.database();
const print = db.collection('print');
Page({
  data: {
    good: null,
    locationObj1: {},
    locationObj2: {},
    date: '2020-01-01',
    time: '00:00',
    message: null,
    money: null
  },
  chooseLocation1: function(e) {
    wx.chooseLocation({
      success: res => {
        let locationObj = {
          latitude: res.latitude,
          longitude: res.longitude,
          name: res.name,
          address: res.address
        }
        this.setData({
          locationObj1: locationObj
        })
      }
    })
  },
  chooseLocation2: function(e) {
    wx.chooseLocation({
      success: res => {
        let locationObj = {
          latitude: res.latitude,
          longitude: res.longitude,
          name: res.name,
          address: res.address
        }
        this.setData({
          locationObj2: locationObj
        })
      }
    })
  },
  bindDateChange: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      date: e.detail.value
    })
  },
  bindTimeChange: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      time: e.detail.value
    })
  },
  optchange5: function(e) {
    console.log('textarea改变，携带值为', e.detail.value)
    this.setData({
      message: e.detail.value
    })
  },
  optchange1: function(e) {
    console.log('textarea改变，携带值为', e.detail.value)
    this.setData({
      good: e.detail.value
    })
  },
  optchange: function(e) {
    console.log('input发送选择改变，携带值为', e.detail.value)
    console.log(typeof e.detail.value)
    this.setData({
      money: e.detail.value,
    })
    this.setData({
      t: Number(this.data.money) * 100
    })
  },
  onSubmit: function(event) {
    console.log(event)
    print.add({
      data: {
        from: this.data.locationObj1,
        to: this.data.locationObj2,
        date: this.data.date,
        time: this.data.time,
        good: this.data.good,
        message: this.data.message,
        money: this.data.money
      }
    }).then(res => {
      wx.showToast({
        title: '添加成功',
        icon: 'success'
      })
    })
  }
})