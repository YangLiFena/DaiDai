const db = wx.cloud.database();
const print = db.collection('print');
const app=getApp()
Page({
  data: {
    array1: ['A4', 'A3', 'B5'],
    objectArray1: [
      {
        id: 0,
        name: 'A4'
      },
      {
        id: 1,
        name: 'A3'
      },
      {
        id: 2,
        name: 'B5'
      }
    ],
    index1: 0,
    array2: ['单面打印', '双面打印'],
    objectArray2: [
      {
        id: 0,
        name: '单面打印'
      },
      {
        id: 1,
        name: '双面打印'
      },
    ],
    index2: 0,
    array3: ['黑白打印', '彩色打印'],
    objectArray3: [
      {
        id: 0,
        name: '黑白打印'
      },
      {
        id: 1,
        name: '彩色打印'
      },
    ],
    index3: 0,
    printNum: null,
    message: null,
    ok: "cross"
  },
  optchange1: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      index1: e.detail.value
    })
  },
  optchange2: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      index2: e.detail.value
    })
  },
  optchange3: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      index3: e.detail.value
    })
  },
  optchange4: function(e) {
    console.log('input发送选择改变，携带值为', e.detail.value)
    this.setData({
      printNum: e.detail.value
    })
  },
  optchange5: function(e) {
    console.log('textarea改变，携带值为', e.detail.value)
    this.setData({
      message: e.detail.value
    })
  },
  selectFile: function() {
    wx.chooseMessageFile({
      count: 10,
      type: 'file',
      success: res => {
        console.log(res.tempFiles[0].path)
        wx.cloud.uploadFile({
          cloudPath: `${Math.floor(Math.random() * 10000000)}`,
          filePath: res.tempFiles[0].path
        }).then(res => {
          console.log(res)
          this.setData({
            file: res.fileID,
            ok: "success"
          })
          wx.showToast({
            title: '文件上传成功！',
          })
        }).catch(err => {
          console.error(err)
        })
      }
    })
  },
  onSubmit: function(event) {
    let printNum = this.data.printNum;
    let ok = this.data.ok;
    let regNum = /^\+?[1-9][0-9]*$/;
  
    if(!regNum.test(printNum)){
      wx.showModal({
        title: '提示',
        content: '亲亲，请输入正确打印份数!',
      })
      return false
    }

    if(ok!="success"){
      wx.showModal({
        title: '提示',
        content: '亲亲，请上传打印的文件!',
      })
      return false
    }

    console.log(event)
    var that=this
    db.collection('Users').where({
      _openid:app.globalData.OPEN_ID
    }).get({
      success:function(res){
        print.add({
          data: {
            size: that.data.array1[that.data.index1],
            way: that.data.array2[that.data.index2],
            color: that.data.array3[that.data.index3],
            price: 1111,
            num: that.data.printNum,
            message: that.data.message,
            avatarUrl:app.globalData.AVATAR,
            status:"待接单",
            nickName:app.globalData.NICKNAME,
            orderType:"打印",
            sendSid:res.data[0].sid,//发单人学号
          }
        }).then(res => {
          wx.showToast({
            title: '提交订单成功！',
            icon: 'success',
            success: res2 => {
              wx.redirectTo({
                url: `../dayinxiang/dayinxiang?id=${res._id}`,
              })
            }
          }) 
        })
      }
    })

  }
})