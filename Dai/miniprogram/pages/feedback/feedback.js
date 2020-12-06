const db = wx.cloud.database();
const yijian = db.collection('yijian');
Page({
  /**
   * 页面的初始数据
   */
  data: {
    loading: false,
    contact: '',
    content: ''
  },
  optchange: function(e) {
    console.log('textarea改变，携带值为', e.detail.value)
    this.setData({
      content: e.detail.value
    })
  },
  optchange1: function(e) {
    console.log('textarea改变，携带值为', e.detail.value)
    this.setData({
      contact: e.detail.value
    })
  },
  formSubmit: function (e) {
    let _that = this;
    let content = e.detail.value.opinion;
    let contact = e.detail.value.contact;
    let regPhone = /^1[3578]\d{9}$/;
    let regEmail = /^[a-z\d_\-\.]+@[a-z\d_\-]+\.[a-z\d_\-]+$/i;
    if (content == "") {
      wx.showModal({
        title: '提示',
        content: '反馈内容不能为空!',
      })
      return false
    }
    if (contact == "") {
      wx.showModal({
        title: '提示',
        content: '手机号或者邮箱不能为空!',
      })
      return false
    }
    if (contact == "" && content == "") {
      wx.showModal({
        title: '提示',
        content: '反馈内容,手机号或者邮箱不能为空!',
      })
      return false
    }
    if ((!regPhone.test(contact) && !regEmail.test(contact)) || (regPhone.test(contact) && regEmail.test(contact))) { //验证手机号或者邮箱的其中一个对
      wx.showModal({
        title: '提示',
        content: '您输入的手机号或者邮箱有误!',
      })
      return false
    } else {
      // this.setData({
      //   loading: true
      // })
      let model, system, platform;
      wx.getSystemInfo({
        success: function (res) {
          model = res.model;
          system = res.system;
          platform = res.platform;
        }
      })
      // wx.request({
      //   url: url + '/util/feedback',
      //   header: {
      //     'content-type': 'application/x-www-form-urlencoded'
      //   },
      //   data: {
      //     'content': content,
      //     'contact': contact,
      //     'device_model': model, //手机型号
      //     'device_system ': system, //操作系统版本
      //     'app_version': platform  //客户端平台
      //   },
      //   method: 'POST',
      //   success: function (res) {
      //     let status = res.data.status;
      //     if (status == 1) {
      //       _that.setData({
      //         loading: false,
      //         contact: '',
      //         contant: ''
      //       })
      //       wx.showToast({
      //         title: '成功',
      //         icon: 'success',
      //         duration: 1500
      //       })
      //     }
      //   },
      //   fail: function () {
      //     console.log("意见反馈接口调用失败")
      //   }
      // })
    }
  },
  onSubmit: function(event) {
    console.log(event)
    yijian.add({
      data: {
        contact: this.data.contact,
        content: this.data.content
      }
    }).then(res => {
      wx.showToast({
        title: '添加成功',
        icon: 'success'
      })
    })
  }
})