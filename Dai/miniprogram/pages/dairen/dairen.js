const db = wx.cloud.database();
const print = db.collection('print');
const app=getApp()
var timestamp = Date.parse(new Date());
var date = new Date(timestamp);
//获取年份  
var Y =date.getFullYear();
//获取月份  
var M = (date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1);
//获取当日日期 
var D = date.getDate() < 10 ? '0' + date.getDate() : date.getDate(); 
//时
var h = date.getHours();
//分
var m = date.getMinutes();
h = h < 10 ? ('0' + h) : h;
m = m < 10 ? ('0' + m) : m;

console.log("当前时间：" + Y + '年'  + M+ '月' + D+ '日' + h + m);
var Nowdate = Y+'-'+ M +'-' + D;
var Nowtime = h +':'+ m;
Page({
  data: {
    locationObj1: {},
    locationObj2: {},
    date: Nowdate,
    time: Nowtime,
    money: null,
    t: 0,
    message:'',

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
      t: Number(this.data.money) * 100
    })
    this.setData({
      t: Number(this.data.money) * 100
    })
  },
  optchange4: function(e) {
    console.log('textarea改变，携带值为', e.detail.value)
    this.setData({
      credit: e.detail.value
    })
  },
  optchange5: function(e) {
    console.log('textarea改变，携带值为', e.detail.value)
    this.setData({
      message: e.detail.value
    })
  },
  onSubmit: function(event) {
    let locationObj1 = this.data.locationObj1;
    let locationObj2 = this.data.locationObj2;
    let date = this.data.date;
    let time = this.data.time;
    let money =this.data.money;
    let exp = /(^[1-9]([0-9]+)?(\.[0-9]{1,2})?$)|(^(0){1}$)|(^[0-9]\.[0-9]([0-9])?$)/;

    if (Object.keys(locationObj1).length === 0) {
      wx.showModal({
        title: '提示',
        content: '亲亲，请选择出发地!',
      })
      return false
    }

    if (Object.keys(locationObj2).length === 0) {
      wx.showModal({
        title: '提示',
        content: '亲亲，请选择目地点!',
      })
      return false
    }    
    
    if (date < Nowdate){
      wx.showModal({
        title: '提示',
        content: '亲亲，咱不能回到过去哦!请重新选择出行日期',
      })
      return false
    }    

    if (time < Nowtime){
      if(date<=Nowdate)
      {
      wx.showModal({
        title: '提示',
        content: '亲亲，咱不能回到过去哦!请重新选择出行时间',
      })
      return false  
      }
    }   

    if(!exp.test(money)){
      wx.showModal({
        title: '提示',
        content: '亲亲，请重新输入打赏费用',
      })
      return false
    }
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
        orderType:"带人",
        message:this.data.message,
        details:this.data.locationObj1.name+'到'+this.data.locationObj2.name,
        credit: this.data.credit
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