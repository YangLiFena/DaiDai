const cloud = require('wx-server-sdk')
cloud.init()
exports.main = async(event, context) => {
  console.log(event.openid)
  try {
    let date = new Date()
    fmt = "YYYY-mm-dd HH:MM:SS"
    console.log(1111)
    let ret;
    let opt = {
        "Y+": date.getFullYear().toString(),        // 年
        "m+": (date.getMonth() + 1).toString(),     // 月
        "d+": date.getDate().toString(),            // 日
        "H+": (date.getHours() + 8).toString(),           // 时
        "M+": date.getMinutes().toString(),         // 分
        "S+": date.getSeconds().toString()          // 秒
        // 有其他格式化字符需求可以继续添加，必须转化成字符串
    };
    for (let k in opt) {
        ret = new RegExp("(" + k + ")").exec(fmt);
        if (ret) {
            fmt = fmt.replace(ret[1], (ret[1].length == 1) ? (opt[k]) : (opt[k].padStart(ret[1].length, "0")))
        };
    };
    // let myDate = new Date;
    // let month = myDate.getMonth() + 1;
    // let day = myDate.getDate()
    // let year = myDate.getFullYear()
    // let hour = myDate.getHours() + 8
    // let minute = myDate.getMinutes()
    // let second = myDate.getSeconds()
    // let time = `${year}-${month}-${day} ${hour}:${minute}:${second}`;
    // console.log(time)
    const result = await cloud.openapi.subscribeMessage.send({
      touser: event.openid, //要推送给那个用户
      page: 'pages/mine/mine', //要跳转到那个小程序页面
      data: {//推送的内容
        thing2: {
          value: '身份认证审核'
        },
        date3: {
          value: fmt
        },
        phrase1: {
          value: '通过'
        }
      },
      templateId: 'RD1ESmvxwfPh4hS_If6EQuLFcC5W4Yn9j2ndfy4ZqN0' //模板id
    })
    console.log(111111111)
    console.log(result)
    return result
  } catch (err) {
    console.log(err)
    return err
  }
}