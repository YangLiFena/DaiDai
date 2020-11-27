// pages/identity/identity.js
const db = wx.cloud.database()
var app=getApp()
Page({
  data: {
    animation1: {},
    "hiddent": true,
    "imageHidden":true,
    name:'',
    sid:'',
    addr: '',
    flagtext:false,
    flagimage:false,
    shenfenHidden:false,
    studentCardHidden:false
  },
  nameInput:function(e)
  {
    this.setData({
      name: e.detail.value
    });
  },
  sid:function(e)
  {
    this.setData({
      sid: e.detail.value
    });
  },

  getStudentCard:function(options){
    //获取学生证图片
    var that = this;
    wx.chooseImage({
      count: 1,
      success: function (res) {
        console.log(res)
        that.setData({ getStudentCard: res.tempFilePaths[0], studentCardHidden:true});
        that.setData({
          flagimage: true
        })
        
        const filePath = res.tempFilePaths[0];
        const cloudPath = "StudentCard/"+'StudentCard'+`${Math.floor(Math.random() * 10000000)}.png`;

        wx.cloud.uploadFile({
          cloudPath: cloudPath,
          filePath: filePath,
          success:res=>{
            console.log(res.fileID)
            that.setData({
             addr: res.fileID
             })
          },
          
          fail:err=>{

          }
        })
        


        
      },
    })
  },

    send: function (e) {
    let _that = this;
    let name = e.detail.value.text;
    let sid = e.detail.value.number;
    let regNum = /^\d{9}$/;
    let regName =/^[\u4E00-\u9FA5\uf900-\ufa2d·s]{2,20}$/;
    let flagimage = this.data.flagimage;

    if(!flagimage){
      wx.showModal({
        title: '提示',
        content: '请上传照片!',
      })
      return false
    }

    if (name == "" && sid == "") {
      wx.showModal({
        title: '提示',
        content: '学号和姓名不能为空!',
      })
      return false
    }

    if (name == "") {
      wx.showModal({
        title: '提示',
        content: '姓名不能为空!',
      })
      return false
    }

    if (!regName.test(name)) { //验证姓名
      wx.showModal({
        title: '提示',
        content: '您输入姓名有误!',
      })
      return false
    }

    if (sid == "") {
      wx.showModal({
        title: '提示',
        content: '学号不能为空!',
      })
      return false
    }
    
    

    if (!regNum.test(sid)) { //验证学号
      wx.showModal({
        title: '提示',
        content: '您输入的学号有误!',
      })
      return false
    }
    
    

    else{
      this.setData({
        flagtext: true
      })}
  },
  
  

  addStudent:function(){
    //放入数据库
      let flagtext =this.data.flagtext
      if(flagtext){
      db.collection('StudentCard').add({
        data: {
          name:this.data.name,
          sid:this.data.sid,
          addr:this.data.addr,
          access: 0
        },
        success: function(res) {
          console.log(res)
        }
      })
      var that=this
      wx.getSetting({
        success (res){
          if (res.authSetting['scope.userInfo']) {
            // 已经授权，可以直接调用 getUserInfo 获取头像昵称
            wx.getUserInfo({
              success: function(res) {
                db.collection('Users').add({
                  data: {//全局变量放mine里获取了
                    name:app.globalData.NICKNAME,//昵称
                    head_picture:app.globalData.AVATAR,//头像
                    sex:app.globalData.SEX,//性别
                    sid:that.data.sid,//学号
                    sname:that.data.name,//姓名
                    credit:100,//信誉分初始100
                  },
                  success: function(res) {
                    console.log(res)
                  }
                })
              }
            })
          }
        }
      })

    }
  },
  jmpHomePage:function(options){ 
    //console.log(this.data.name);
    wx.requestSubscribeMessage({
      tmplIds: ['RD1ESmvxwfPh4hS_If6EQuLFcC5W4Yn9j2ndfy4ZqN0', 'sEX6_fydKEFlqrHXh3j2H0fJAGc3wSqjMK25ABVxOmo'],
      success (res) { }
    })
    let flagtext =this.data.flagtext
    if(flagtext){
    this.addStudent();
    wx.switchTab({
      url: '../mine/mine'
    })
  }
  },

  fail: function (res) {
    console.log(res.errMsg)
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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

  }
})