const db = wx.cloud.database();
const tousu = db.collection('tousu');
Page({
  data: {
    array: ['该用户存在欺诈骗钱行为', 
    '该用户发布不适当的信息对我造成骚扰', 
    '该用户存在恶意行为（如反复发布取消任务）'],
    index: 0,
    fileList: [],
    message: null,
    type: null,
    people: null
  },
  urlTurn: function() {
    wx.redirectTo({
      url: `../renyuan/renyuan`,
    })
  },
  optchange: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      index: e.detail.value
    })
  },
  afterRead: function(event) {
    console.log(event)
    wx.cloud.uploadFile({
      cloudPath: `${Math.floor(Math.random() * 10000000)}.png`,
      filePath: event.detail.file.url
    }).then(res => {
      console.log(res)
      let FileList = this.data.fileList
      let temp = {url: res.fileID}
      this.setData({
        fileList: FileList.concat(temp)
      })
    }).catch(err => {
      console.error(err)
    })
  },
  optchange: function(e) {
    console.log('textarea改变，携带值为', e.detail.value)
    this.setData({
      message: e.detail.value
    })
  },
  onSubmit: function(event) {
    console.log(event)
    tousu.add({
      data: {
        people: this.data.people,
        message: this.data.message,
        type: this.data.array[this.data.index],
        fileList: this.data.fileList,
      }
    }).then(res => {
      wx.showToast({
        title: '添加成功',
        icon: 'success'
      })
    })
  },
  onLoad: function (options) {
    this.setData({
      people: options.people
    })
  },
})

