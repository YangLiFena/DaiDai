// import automator from 'miniprogram-automator'
const automator = require('miniprogram-automator')
describe('index', () => {
  let miniProgram
  let page
  // 连接微信开发者工具
  beforeAll(async () => {
    miniProgram = await automator.launch({
      cliPath: 'E:\微信开发\微信web开发者工具\cli.bat',
      projectPath: 'E:\微信开发\code\printpaper2\miniprogram'
    })
    page = await miniProgram.reLaunch('../pages/message/message')
    await page.waitFor(500)
  }, 40000)

  it('初始化洗数据后， 初始数据满足要求', async (done)=>{
    const data = await page.data() 
    expect(data).toMatchObject({
      items: expect.anything(),
      facet: expect.anything()
    })  
    done()
  })

  afterAll(async () => {
    await miniProgram.close()
  })
})