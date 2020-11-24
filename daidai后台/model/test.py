import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import requests
import json
import cv2

WECHAT_URL = 'https://api.weixin.qq.com/'
APP_ID = 'wx4184fe0dc5886089'
APP_SECRET = 'cc2bd71e5125bbb08b79751045e3da32'
ENV = 'yuntest-1ge0b9sqe0319f10'  # 云环境ID

image = 'cloud://yuntest-1ge0b9sqe0319f10.7975-yuntest-1ge0b9sqe0319f10-1304211863/2891643.png'

def get_access_token():
    url = '{0}cgi-bin/token?grant_type=client_credential&appid={1}&secret={2}'.format(WECHAT_URL, APP_ID, APP_SECRET)
    response = requests.get(url)
    result = response.json()
    print(result)
    return result['access_token']


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



