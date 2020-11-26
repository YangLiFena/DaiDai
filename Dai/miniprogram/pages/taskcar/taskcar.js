// pages/orderManager/orderManager.js
const db = wx.cloud.database();
var app=getApp()
var util = require('../../utils/util.js');
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
    console.log(myid)
    const _ = db.command
    that.setData({ data: null });
    switch(status){
      case 0://所有相关订单，发单和接单
      db.collection('print').where(_.or([{
          orderTaker: myid
        },{
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
          status:_.neq("已完成").and(_.neq("已评价")).and(_.neq("已取消"))
        },
        {
          _openid:myid,//自己发单，待接单
          status:_.neq("已完成").and(_.neq("已评价")).and(_.neq("已取消"))
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
            _openid:app.globalData.OPEN_ID,//自己发的单，评价别人
            status:_.in(['已完成','已评价'])
          }).get({
            success: function(res) {
              that.setData({ data: res.data });
            }
          })
          break;
          case 4://status=已完成，orderTaker不是自己，可以自己完成自己的订单
          db.collection('print').where({
            _openid:app.globalData.OPEN_ID,//自己发的单
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
//点完成
  complete: function (options) {
    var that = this;
    var index = options.currentTarget.dataset.id;
    var myid=app.globalData.OPEN_ID
    var s = '确定你已完成订单'
    //console.log(index)
    db.collection('print').doc(index).get({
      success:function(res) {
        console.log(res.data)
        if(res.data.status=='已取消'){
          s="不能完成已取消的订单！"
        }else if(res.data.status=='已完成'){
          s='不能重复完成订单！'
        }else if(res.data.status=='待接单'){
          s='订单还未接单，请取消'
        }else if (res.data.status=='已接单'&&res.data.orderTaker != myid) {
          s = "确定你的订单已被完成"
        }
        if(s=='确定你的订单已被完成'||s=='确定你已完成订单'){
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
        }else{
          wx.showModal({
            title: '提示',
            content: s,
            showCancel:false,
          })
        }
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
          case "带货":
            wx.navigateTo({
              url: `../daihuoxiang/daihuoxiang?id=${id}`,
          })
          break;
        }
      }
    })
  },
  //点评价
  comment:function(options){
    var id =options.currentTarget.dataset.id;
    var userid
    var status
    db.collection('print').doc(id).get().then(res=>{
      userid=res.data._openid
      status=res.data.status
      var s
      if(status=='待接单'){
        s='订单未接单！'
      }else if(status=='已接单'){
        s='订单未完成！'
      }else if(status=='已评价'){
        s='不能重复评价！'
      }else if(status=='已取消'){
        s='订单已取消！'
      }else if(status=='已完成'){//进行评价
        db.collection('Users').where({
          _openid:userid
        }).get({
          success: function(res) {
            wx.navigateTo({
              url: `../commentDetail/commentDetail?id=${id}`,
            })
          }
        })
      }
      if(status!='已完成'){
        wx.showModal({
          title: '提示',
          content: s,
          showCancel:false,
        })
      }
    })
  },
  completeOrder: function (index) {
    var that=this
    var time = util.formatTime(new Date());
    //改状态，加入完成时间
    db.collection('print').doc(index).update({
      data: {
        status: "已完成",
        completeTime:time
      },
      success: function(res) {
        console.log(res)
        that.onLoad()
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
  send: function(index) {
    wx.requestSubscribeMessage({
      tmplIds: ['RD1ESmvxwfPh4hS_If6EQuLFcC5W4Yn9j2ndfy4ZqN0', 'sEX6_fydKEFlqrHXh3j2H0fJAGc3wSqjMK25ABVxOmo'],
      success (res) {console.log(res) },
      fail(res){console.log(res)}
    })
    db.collection('print').doc(index).get().then(res=>{
      var userid=res.data._openid
      var type=res.data.orderTaker
      console.log(userid)
      wx.cloud.callFunction({
        name: "cancel_order",
        data:{
          touser:userid,
          page: 'pages/mine/mine',
          templateId: 'sEX6_fydKEFlqrHXh3j2H0fJAGc3wSqjMK25ABVxOmo',
          data: {//推送的内容
            character_string1: {
              // 订单id，要改
              value: index
            },
            thing2: {
              // 订单类型，要改
              value: type
            },
          },
        }
      }).then(res => {
        console.log("推送消息成功", res)
      }).catch(res => {
        console.log("推送消息失败", res)
      })
  })
},
//点取消
  cancel:function(options){
    var index = options.currentTarget.dataset.id;
    var that=this
    db.collection('print').doc(index).get({
      success:function(res){
        var status=res.data.status
        var s
        if(status=='已取消'){
          s='不能重复取消订单！'
          wx.showModal({
            title: '提示',
            content: s,
            showCancel:false,
          })
        }else if(status=='已完成'||status=='已评价'){
          s='订单已完成！'
          wx.showModal({
            title: '提示',
            content: s,
            showCancel:false,
          })
        }else if(status=='待接单'){
          wx.showModal({
            title: '确定取消订单？',
            success: function (res) {
              if (res.confirm) {
                db.collection('print').doc(index).pdate({
                  data:{
                    status:'已取消'
                  }
                })
              } else if (res.cancel) {
                console.log('用户点击取消')
              }
            }
          })
        }else if(status=='已接单'){
          wx.showModal({
            title: '确定取消订单？',
            content: '请与下单或接单用户联系后再取消订单！',
            success: function (res) {
              if (res.confirm) {
                that.cancelOrder(index)//完成状态设置
              } else if (res.cancel) {
                console.log('用户点击取消')
              }
            }
          })
        }
      }
    })
  },
  cancelOrder: function (index) {
    var that=this
    db.collection('print').doc(index).update({//index 订单_id
      data:{
        status:'已取消'
      },
      success: function(res) {
        that.send(index);//向被取消用户发送订阅消息
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