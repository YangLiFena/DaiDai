const cloud = require('wx-server-sdk')
cloud.init()
exports.main = async(event, context) => {
  // console.log(event.openid)
  try {
    let date = new Date()
    fmt = "YYYY-mm-dd HH:MM:SS"
    console.log(1111)
    let ret;
    let opt = {
        "Y+": date.getFullYear().toString(),        // 年
        "m+": (date.getMonth() + 1).toString(),     // 月
        "d+": date.getDate().toString(),            // 日
        "H+": (date.getHours() + 8).toString(),     // 时
        "M+": date.getMinutes().toString(),         // 分
        "S+": date.getSeconds().toString()          // 秒
    };
    for (let k in opt) {
        ret = new RegExp("(" + k + ")").exec(fmt);
        if (ret) {
            fmt = fmt.replace(ret[1], (ret[1].length == 1) ? (opt[k]) : (opt[k].padStart(ret[1].length, "0")))
        };
    };
    const result = await cloud.openapi.subscribeMessage.send({
      touser: 'on6E640xFe7ihC1D55d7jmOdf2vs', //要推送给那个用户的openid，要改
      page: 'pages/mine/mine', //要跳转到那个小程序页面，要改
      data: {//推送的内容
        character_string1: {
          // 订单id，要改
          value: '111'
        },
        thing2: {
          // 订单类型，要改
          value: '带货'
        },
        time5: {
          // 时间，不用改
          value: fmt
        }
      },
      templateId: 'sEX6_fydKEFlqrHXh3j2H0fJAGc3wSqjMK25ABVxOmo'
    })
    console.log(111111111)
    console.log(result)
    return result
  } catch (err) {
    console.log(err)
    return err
  }
}