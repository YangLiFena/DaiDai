const db = wx.cloud.database();
const print = db.collection('print');
const app=getApp()
var util=require('../../utils/util.js')
Page({
  data: {
    newcomment: {},
    id: null,
    skip: 0,
    points:0,
    content:'',
    commentAvatar:'',//被评价人的头像
    commentNickName:'',
    completeTime:'',
  },
  onLoad: function(options) {
    this.id=options.id
    var that=this
    db.collection('print').doc(this.id).get({
      success:function(res){
        that.setData({completeTime:res.data.completeTime})
        db.collection('Users').where({
          _openid:res.data.orderTaker
        }).get({
          success:function(res){
            var d=res.data[0]
            that.setData({commentAvatar:d.head_picture,
            commentNickName:d.name,
            })
          }
        })
        
      }
    })
  },
  optchange: function(e) {
    this.content=e.detail.value
  },
  onChange:function(event){
    this.points=event.detail
  },
  onSubmit: function(event) {
    var TIME = util.formatTime(new Date());
    this.newcomment={
      nickName:app.globalData.NICKNAME,//自己的昵称
      avatar:app.globalData.AVATAR,
      time:TIME,
      message:this.content,
      points:this.points
    }
    console.log(this.newcomment)
    db.collection('print').doc(this.id).update({
      data:{
        status:'已评价',
      },
    })
    db.collection('print').doc(this.id).get().then(res => {
      const _ = db.command
      var myid=res.data._openid
      db.collection('Users').where({
        _openid:myid
      }).update({
        data:{
          get: _.push([this.newcomment])
        },
        success: res =>{
            console.log("数组添加成功")
            console.log(res)
            //var pages = getCurrentPages(); //当前页面
            //var beforePage = pages[pages.length -2 ]; //前一页
            wx.navigateBack({
              success: function () {
                //beforePage.onLoad(); // 执行前一个页面的onLoad方法
              }
            });
        }
      })
    })

  },
})