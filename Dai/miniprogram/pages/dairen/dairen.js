const db = wx.cloud.database();
const print = db.collection('print');
const app=getApp()
Page({
  data: {
    locationObj1: {},
    locationObj2: {},
    date: '2020-01-01',
    time: '00:00',
    money: null,
    t: 0,

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
        money: this.data.money,
        avatarUrl:app.globalData.AVATAR,
        status:"待接单",
        nickName:app.globalData.NICKNAME,
        orderType:"带人"
      }
    }).then(res => {
      wx.showToast({
        title: '提交订单成功！',
        icon: 'success',
        success: res2 => {
          wx.redirectTo({
            url: `../dairenxiang/dairenxiang?id=${res._id}`,
          })
        }
      }) 
    })
  }
})