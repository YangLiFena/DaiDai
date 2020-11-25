import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import requests
import json
import os
import cv2

WECHAT_URL = 'https://api.weixin.qq.com/'
APP_ID = 'wx4184fe0dc5886089'
APP_SECRET = 'cc2bd71e5125bbb08b79751045e3da32'
ENV = 'yuntest-1ge0b9sqe0319f10'  # 云环境ID

image = 'cloud://yuntest-1ge0b9sqe0319f10.7975-yuntest-1ge0b9sqe0319f10-1304211863/2891643.png'
src = 'cloud://yuntest-1ge0b9sqe0319f10.7975-yuntest-1ge0b9sqe0319f10-1304211863/2855057.doc'

def get_access_token():
    url = '{0}cgi-bin/token?grant_type=client_credential&appid={1}&secret={2}'.format(WECHAT_URL, APP_ID, APP_SECRET)
    response = requests.get(url)
    result = response.json()
    print(result)
    return result['access_token']

def get_file(src):
    accessToken = get_access_token()
    # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
    collection_name = 'StudentCard'
    url = '{0}tcb/batchdownloadfile?access_token={1}'.format(WECHAT_URL, accessToken)
    file_list = [
        {
            'fileid': src,
            'max_age': 7200
        },
        {
            'fileid': src,
            'max_age': 7200
        }
    ]
    data = {
        "env": ENV,
        'file_list': file_list
    }
    response = requests.post(url, data=json.dumps(data))
    print('--------------------')
    # print(response)
    data = response.json()
    print(data)
    download_list = data['file_list']
    list = []
    for item in download_list:
        list.append(item['download_url'])
    # img_src = data['file_list'][0]['download_url']
    # print(data['file_list'][0]['download_url'])

    # cap = cv2.VideoCapture(img_src)
    # if (cap.isOpened()):
    #     ret, img = cap.read()
    #     cv2.imshow("image", img)
    #     cv2.waitKey()
    print(list)
    return list
    # return img_src


# get_file(src)


def get_message(image):
    accessToken = get_access_token()
    # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
    collection_name = 'StudentCard'
    url = '{0}tcb/batchdownloadfile?access_token={1}'.format(WECHAT_URL, accessToken)
    file_list = [
        {
            'fileid': image,
            'max_age': 7200
        }
    ]
    data = {
        "env": ENV,
        'file_list': file_list
    }
    response = requests.post(url, data=json.dumps(data))
    print('--------------------')
    # print(response)
    data = response.json()
    print(data)
    img_src = data['file_list'][0]['download_url']
    print(data['file_list'][0]['download_url'])

    # cap = cv2.VideoCapture(img_src)
    # if (cap.isOpened()):
    #     ret, img = cap.read()
    #     cv2.imshow("image", img)
    #     cv2.waitKey()

    return img_src


# get_message(image)
#
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口位置和大小
        hbox = QHBoxLayout(self)
        # url = "http://photocdn.sohu.com/20120128/Img333056814.jpg"
        url = get_message(image)
        res = requests.get(url)
        img = QImage.fromData(res.content)

        l1 = QLabel(self)
        l1.setPixmap(QPixmap.fromImage(img))
        l1.setScaledContents(True)
        # l1.move(10, 10)
        hbox.addWidget(l1)
        self.setLayout(hbox)
        reply4 = QMessageBox.about(self, "标题", "关于对话框消息正文")
        # self.setGeometry(100, 100, 620, 500)
        self.show()

        # self.setGeometry(300, 300, 300, 220)
        # self.setWindowTitle('Icon')
        # # 设置窗口图标，引用图片
        # self.setWindowIcon(QIcon('icon_test1.png'))
        # self.show()


if __name__ == '__main__':
    # 创建应用程序
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())




list = ['https://7975-yuntest-1ge0b9sqe0319f10-1304211863.tcb.qcloud.la/2855057.doc', 'https://7975-yuntest-1ge0b9sqe0319f10-1304211863.tcb.qcloud.la/2855057.doc']

def down_load(list):
    # 下载地址
    # Download_addres = 'https://nj02cm01.baidupcs.com/file/da941ce26b392a4ea0b010b6e021a695?bkt=p3-1400da941ce26b392a4ea0b010b6e021a6956171262a00000003bca9&fid=3310494135-250528-127659779854873&time=1533574416&sign=FDTAXGERLQBHSK-DCb740ccc5511e5e8fedcff06b081203-KqPVE0es2sUR30U1G%2Fvps9I3VY4%3D&to=88&size=244905&sta_dx=244905&sta_cs=0&sta_ft=jpg&sta_ct=0&sta_mt=0&fm2=MH%2CQingdao%2CAnywhere%2C%2Cchongqing%2Ccmnet&resv0=cdnback&resv1=0&vuk=282335&iv=-2&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=1400da941ce26b392a4ea0b010b6e021a6956171262a00000003bca9&sl=82640974&expires=8h&rt=sh&r=220567738&mlogid=445212826855757932&vbdid=1883780403&fin=1533574308687.jpg&fn=1533574308687.jpg&rtype=1&dp-logid=445212826855757932&dp-callid=0.1.1&hps=1&tsl=50&csl=78&csign=0vnYzTYv2VV%2Ff%2FRkrbacf8q2JPs%3D&so=0&ut=8&uter=4&serv=0&uc=1400105996&ic=321428139&ti=86348c5ac45f19b1da511678c3490bd3448fbb7a71823ad8&by=themis'
    # 把下载地址发送给requests模块
    path = '031802318'
    os.makedirs(path)
    for i in range(0, len(list), 1):
        f = requests.get(list[i])
        # 下载文件
        with open('./' + path + '/' +  str(i) + '.doc', "wb") as code:
            code.write(f.content)

# down_load(list)