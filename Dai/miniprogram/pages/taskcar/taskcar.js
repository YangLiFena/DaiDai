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
    this.getMsg('getUserOrderList', 0);
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
    console.log("item:"+item)
    switch (item) {
      case "quanbu":
        this.setData({ quanbu: "border-bottom: 3px solid #EF4143;color:#EF4143;font-weight:bold" });
        this.getMsg('getUserOrderList', 0);
        break;
      case "send":
        this.setData({ send: "border-bottom: 3px solid #EF4143;color:#EF4143;font-weight:bold" });
        this.getMsg('getUserSendOrderList',  0);
        break;
      case "end":
        this.setData({ end: "border-bottom: 3px solid #EF4143;color:#EF4143;font-weight:bold" });
        this.getMsg('getUserLootOrderList',  0);
        break;
      case "daiban":
        this.setData({ daiban: "border-bottom: 3px solid #EF4143;color:#EF4143;font-weight:bold" });
        this.getMsg('getStatusOrderList',  2);
        break;
      case "daiwancheng":
        this.setData({ daiwancheng: "border-bottom: 3px solid #EF4143;color:#EF4143;font-weight:bold" });
        this.getMsg('getStatusOrderList',  3);
        break;
      case "daipingjia":
        this.setData({ daipingjia: "border-bottom: 3px solid #EF4143;color:#EF4143;font-weight:bold" });
        this.getMsg('getUserOrderNotEvaluate',  4);
        break;
    }
  },
  getMsg(xuanxiang, status) {
    console.log(xuanxiang + " --   -- " + status)
    var that = this;
    var userInfo = this.data.userInfo;
    var util = require('../../utils/util.js');
    switch(status){
      case 0:
        db.collection('print').where({
          orderTaker:app.globalData.OPEN_ID//接单人是自己TODO
        }).get({
          success: function(res) {
            that.setData({ data: res.data });
          }
        })
        break;
      case 1:
        db.collection('print').where({
          orderTaker:app.globalData.OPEN_ID,
          status: "已接单"
        }).get({
          success: function(res) {
            // res.data 是包含以上定义的两条记录的数组
            that.setData({ data: res.data });
          }
        })
        break;
        case 2:
          db.collection('print').where({
            _openid:app.globalData.OPEN_ID
          }).get({
            success: function(res) {
              that.setData({ data: res.data });
            }
          })
          break;
        case 3:
          db.collection('print').where({
            orderTaker:app.globalData.OPEN_ID,
            status: "已完成"
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
  jiedan: function (options) {
    console.log(options);
    var id = options.currentTarget.dataset.id;
    var orderid = options.currentTarget.dataset.orderid;
    console.log(orderid)
    wx.navigateTo({
      url: '/pages/orderLootPrivate/orderLootPrivate?id=' + id + "&orderid=" + orderid,
    })
  },
  fadan: function (options) {
    console.log(options.currentTarget.dataset.id);
    var id = options.currentTarget.dataset.id;
    wx.navigateTo({
      url: '/pages/privateOrder/privateOrder?id=' + id,
    })
  },
  complete: function (options) {
    console.log(options.currentTarget.dataset.index);
    var that = this;
    var index = options.currentTarget.dataset.index;
    var data = this.data.data[index][0];
    var s = '你确定完成订单了吗？ 订单金额只有在双方都确认，点击"完成订单"才会到达接单的同学的账户。'
    if (data.orderHost == that.data.userInfo.id) {
      s = "你确定接单的同学已经完成了吗？"
    }
    wx.showModal({
      title: '提示',
      content: s,
      success: function (res) {
        if (res.confirm) {
          that.completeOrder(index)
        } else if (res.cancel) {
          console.log('用户点击取消')
        }
      }
    })
  },
  detail: function (options) {
    console.log(options.currentTarget.dataset.id);
    var id = options.currentTarget.dataset.id;
    wx.navigateTo({
      url: '/pages/orderDetail/orderDetail?id=' + id,
    })
  },
  completeOrder: function (index) {
    var data = this.data.data[index][0];
    var orderId = data.id;
    var status;
    if (data.status == "订单已承接") {
      status = 2
    } else if (data.status == "订单已完成") {
      status = 3;
    }
    var userInfo = this.data.userInfo;
    var s = "完成订单申请成功,请等待发布订单的同学点击完成订单！！"
    if (data.orderHost == userInfo.id) {
      s = "订单已结束,订单金额将到达接单人的账户，感谢您的使用！！";
    }
    wx.request({
      url: 'https://api.wnschool.cn/order-updateOrderStatus',
      data: {
        // "code":code,
        "order.id": orderId,
        "order.status": status + 1,
        "user.id": userInfo.id
      },
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: 'POST',
      success: function (res) {
        console.log(res);
        if (res.data == "lootSuccess") {
          wx.showModal({
            title: '提示',
            content: s,
            showCancel: false,
            success: function (res) {
              if (res.confirm) {
                console.log('用户点击确定')
              }
            }
          })
          // wx.showToast({
          //   title: s,
          //   success: function () {

          //     setTimeout(function () {
          //       wx.hideToast();
          //     }, 2000)
          //   }
          // })
        } else{
          wx.showModal({
            title: '提示',
            content: '订单发生错误',
            showCancel:false,
            success: function (res) {
              if (res.confirm) {
                console.log('用户点击确定')
              }
            }
          })
        }
      }
    })
  },
  cancel:function(options){
    var index = options.currentTarget.dataset.index;
        var item = this.data.data[index];
        if (item[0].status == "订单新发布" && item[2].shenfen=="发单"){
          wx.showModal({
            title: '你确定要取消订单？',
            content: '确定取消订单后，将会退还您的订单金额。',
            success:function(){
              
            }
          })
          //订单主人在状态1时发出取消信号
        } else if (item[0].status == "订单已承接" && item[2].shenfen == "发单"){
          //订单主人在状态2时发出取消信号
          wx.showModal({
            title: '你的订单已被承接，你无法取消订单，请联系承接订单的童鞋取消订单吧.',
            content: '',
            showCancel: false
          })
        } else if(item[0].status == "订单已承接" && item[2].shenfen == "接单"){
          //接单人在状态2时发出取消信号
          wx.showModal({
            title: '你确定要取消订单？',
            content: '确定取消订单后，订单金额将退还到达发布订单的童鞋。'
          })
        }
  }
})