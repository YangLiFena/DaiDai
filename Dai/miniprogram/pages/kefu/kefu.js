var app = getApp();
//const config = require("../../config.js");

Page({

      /**
       * 页面的初始数据
       */
      data: {
            weixin: "wxid_up2bruqdf61322",
            qq: "1045929609",
            //gzh: JSON.parse(config.data).kefu.gzh,
            //phone: JSON.parse(config.data).kefu.phone,
            //banner: "/photo/1.png"
      },
      onLoad() {
      
      },

      //复制
      copy(e) {
            wx.setClipboardData({
                  data: e.currentTarget.dataset.copy,
                  success: res => {
                        wx.showToast({
                              title: '复制' + e.currentTarget.dataset.name+'成功',
                              icon: 'success',
                              duration: 1000,
                        })
                  }
            })
      },

      //预览图片
      preview(e) {
            wx.previewImage({
                  urls: e.currentTarget.dataset.link.split(",")
            });
      },
})