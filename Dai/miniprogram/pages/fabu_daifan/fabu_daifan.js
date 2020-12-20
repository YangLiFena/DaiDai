Page({
  data:{
    input1:null,
    input2:null,
    input3:null,
    input4:null,
    input5:null,
    input6:null
  },
  input1:function(e){
    this.setData({
      input1:e.detail.value
    });
  },
  input2:function(e){
    this.setData({
      input2:e.detail.value
    });
  },
  input3:function(e){
    this.setData({
      input3:e.detail.value
    });
  },
  input4:function(e){
    this.setData({
      input4:e.detail.value
    });
  },
  input5:function(e){
    this.setData({
      input5:e.detail.value
    });
  },
  input6:function(e){
    this.setData({
      input6:e.detail.value
    });
  },
  success:function(options){
    console.log("菜品名称："+this.data.input1+"\n"+"购买地点："+this.data.input2+"\n"+"送达目的地："+this.data.input3+"\n"+"预约时间："+"\n"+"开始时间："+this.data.input5+" "+"结束时间："+this.data.input6)
    wx.navigateTo({
        url: '../fabu/fabu',
      })
    wx.showToast({
      title: '发布成功',
      icon: 'success',
      duration: 2000//持续的时间
    })
    },
  })