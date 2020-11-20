// pages/orderManager/orderManager.js
const db = wx.cloud.database();
var app=getApp()
Page({

  data: {
    personal: true,
    "userInfo": null,
    quanbu: "border-bottom: 3px solid #EF4143;color:#EF4143;font-weight:bold",
    details:""
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.getMsg(0);
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },
  personal: function () {
    this.setData({
      personal: false
    })
  }, exit: function () {
    this.setData({
      personal: true
    })
  },
  preview: function () {
    var avatar = this.data.userInfo.avatarUrl;
    console.log(avatar)
    wx.previewImage({
      urls: [avatar]
    })
  },
  item: function (options) {
    this.setData({ quanbu: "", daiban: "", send: "", end: "", daipingjia: "", });
    var item = options.currentTarget.dataset.item;
    console.log(item)
    switch (item) {
      case "quanbu":
        this.setData({ quanbu: "border-bottom: 3px solid #EF4143;color:#EF4143;font-weight:bold" });
        this.getMsg(0);
        break;
      case "daiban":
        this.setData({ daiban: "border-bottom: 3px solid #EF4143;color:#EF4143;font-weight:bold" });
        this.getMsg(1);
        break;
      case "send":
        this.setData({ send: "border-bottom: 3px solid #EF4143;color:#EF4143;font-weight:bold" });
        this.getMsg(2);
        break;
      case "end":
        this.setData({ end: "border-bottom: 3px solid #EF4143;color:#EF4143;font-weight:bold" });
        this.getMsg(3);
        break;
      case "daipingjia":
        this.setData({ daipingjia: "border-bottom: 3px solid #EF4143;color:#EF4143;font-weight:bold" });
        this.getMsg(4);
        break;
    }
  },
  getMsg(status) {
    var that = this;
    var myid=app.globalData.OPEN_ID
    const _ = db.command
    //var userInfo = this.data.userInfo;
    //var util = require('../../utils/util.js');
    that.setData({ data: null });
    switch(status){
      case 0://所有相关订单，发单和接单
      db.collection('print').where(_.or([
        {
          orderTaker: myid
        },
        {
          _openid:myid
        }
      ]))
      .get({
        success: function(res) {
          console.log(res.data)
          that.setData({data:res.data})
        }
      })
        break;
      case 1://所有相关+status不是已完成
      db.collection('print').where(_.or([
        {
          orderTaker: myid,
          status:_.neq("已完成").and(_.neq("待评价"))
        },
        {
          _openid:myid,//自己发单，待接单
          status:_.neq("已完成").and(_.neq("待评价"))
        }
      ]))
      .get({
        success: function(res) {
          console.log(res.data)
          that.setData({data:res.data})
        }
      })
        break;
        case 2://发的单
          db.collection('print').where({
            _openid:app.globalData.OPEN_ID
          }).get({
            success: function(res) {
              that.setData({ data: res.data });
            }
          })
          break;
        case 3://status=已完成，已评价，待评价就是已完成
          db.collection('print').where({
            orderTaker:app.globalData.OPEN_ID,
            status:_.in(['已完成', '已评价'])
          }).get({
            success: function(res) {
              that.setData({ data: res.data });
            }
          })
          break;
          case 4://status=已完成，orderTaker不是自己
          db.collection('print').where({
            orderTaker:_.neq(app.globalData.OPEN_ID),
            status:"已完成"
          }).get({
            success: function(res) {
              that.setData({ data: res.data });
            }
          })
            break;
    }
  },
  evaluate: function (options) {
    console.log(options.currentTarget.dataset.orderid);
    var orderId = options.currentTarget.dataset.orderid;
    var lootUserId = options.currentTarget.dataset.lootuserid;
    wx.navigateTo({
      url: '/pages/evaluate/evaluate?orderId=' + orderId + "&lootUserId=" + lootUserId,
    })
  },
  complete: function (options) {
    var that = this;
    var index = options.currentTarget.dataset.id;
    var myid=app.globalData.OPEN_ID
    var s = '确定你已完成订单'
    console.log(index)
    db.collection('print').doc(index).get({
      success:function(res) {
        console.log(res)
        if (res.data.orderTaker != myid) {
          s = "确定你的订单已被完成"
        }
        wx.showModal({
          title: '提示',
          content: s,
          success: function (res) {
            if (res.confirm) {
              that.completeOrder(index)//完成状态设置
            } else if (res.cancel) {
              console.log('用户点击取消')
            }
          }
        })
      }
    })
  },
  //订单详情
  detail: function (options) {
    var id =options.currentTarget.dataset.id;
    console.log(id);
    db.collection('print').doc(id).get({
      success: function(res) {
        console.log(res)
        var d=res.data.orderType
        switch(d){
          case "打印":
            wx.navigateTo({
            url: `../dayinxiang/dayinxiang?id=${id}`,
          })
          break;
          case "带人":
            wx.navigateTo({
              url: `../dairenxiang/dairenxiang?id=${id}`,
          })
          break;
          case "带饭":
            wx.navigateTo({
              url: `../daihuoxiang/daihuoxiang?id=${id}`,
          })
          break;
        }
      }
    })
  },
  completeOrder: function (index) {
    db.collection('print').doc(index).update({
      data: {
        status: "已完成",
      },
      success: function(res) {
        console.log(res)
      }
    })
    wx.showModal({
      title: '提示',
      content: '订单已完成！',
      showCancel:false,
      success: function (res) {
        if (res.confirm) {
          console.log('用户点击确定')
        }
      }
    })
  },
  cancel:function(options){
    var index = options.currentTarget.dataset.id;
    var that=this
    wx.showModal({
      title: '确定取消订单？',
      //content: '确定取消订单后，将会退还您的订单金额。',
      success: function (res) {
        if (res.confirm) {
          that.cancelOrder(index)//完成状态设置
        } else if (res.cancel) {
          console.log('用户点击取消')
        }
      }
    })
  },
  cancelOrder: function (index) {
    console.log(index)
    db.collection('print').doc(index).remove({
      success: function(res) {
        console.log(res)
        wx.showModal({
          title: '提示',
          content: '订单已取消！',
          showCancel:false,
          success: function (res) {
            if (res.confirm) {
              console.log('用户点击确定')
            }
          }
        })
      }
    })
  },
  contact: function() {
    wx.redirectTo({
      url: '../im/room/room',
    })
  }
})