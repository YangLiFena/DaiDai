Page({
  data: {
    catelist:[
      {
        id:1,
        image_src: '/photo/tag1.png'
      },
      {
        id:2,
        image_src: '/photo/tag2.png'
      },
      {
        id:3,
        image_src: '/photo/tag3.png'
      }
    ]
  },
  jmpFaBuPage:function(options){ 
    wx.navigateTo({
      url: '../fabu/fabu'
    })
  },
  jmpAllTasksPage:function(options){ 
    wx.navigateTo({
      url: '../alltasks/alltasks'
    })
  },
  jmpAsksPage:function(options){ 
    wx.navigateTo({
      url: '../kefu/kefu'
    })
  },
})

