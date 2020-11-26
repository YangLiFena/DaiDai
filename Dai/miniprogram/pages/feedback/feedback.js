const db = wx.cloud.database();
const yijian = db.collection('yijian');
Page({
  /**
   * 页面的初始数据
   */
  data: {
    
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

  onSubmit: function(event) {
    
    let content = this.data.content;
    let contact = this.data.contact;
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
  
    if ((!regPhone.test(contact) && !regEmail.test(contact)) || (regPhone.test(contact) && regEmail.test(contact))) { //验证手机号或者邮箱的其中一个对
      wx.showModal({
        title: '提示',
        content: '您输入的手机号或者邮箱有误!',
      })
      return false
    }
    
    // wx.showModal({
    //   title: '提示',
    //   content: '确认要删除该支出类型?',
    //   success: function (res) {
    //    if (res.confirm) {}
    //   }})


    console.log(event)
    yijian.add({
      data: {
        contact: this.data.contact,
        content: this.data.content
      }
    }).then(res => {
      wx.showToast({
        title: '反馈成功',
        icon: 'success'
      })
    })
      
  }
})