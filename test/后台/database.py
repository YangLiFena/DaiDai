#coding=gbk
import requests
import json


WECHAT_URL = 'https://api.weixin.qq.com/'
APP_ID = 'wx4184fe0dc5886089'
APP_SECRET = 'cc2bd71e5125bbb08b79751045e3da32'
ENV = 'yuntest-1ge0b9sqe0319f10'  # 云环境ID

class DataBase():
    def get_access_token(self):
        url = '{0}cgi-bin/token?grant_type=client_credential&appid={1}&secret={2}'.format(WECHAT_URL, APP_ID, APP_SECRET)
        response = requests.get(url)
        result = response.json()
        # print(result)
        return result['access_token']


    @classmethod
    def search_order(self, sno):
        if sno == '':
            accessToken = self.get_access_token(self)
            # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
            collection_name = 'test4'
            url = '{0}tcb/databasequery?access_token={1}'.format(WECHAT_URL, accessToken)
            query1 = "db.collection('%s').limit(100).get()" % (collection_name)
            data1 = {
                "env": ENV,
                "query": query1
            }
            query2 = "db.collection('%s').limit(100).get()" % (collection_name)
            data2 = {
                "env": ENV,
                "query": query2
            }
            response1 = requests.post(url, data=json.dumps(data1))
            # print('查询数据：' + response.text)
            # print('--------------------')
            # result = response.json()
            # print(result)
            all_data1 = response1.json()['data']

            response2 = requests.post(url, data=json.dumps(data2))
            all_data2 = response2.json()['data']
        else:
            accessToken = self.get_access_token(self)
            # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
            collection_name = 'test4'
            url = '{0}tcb/databasequery?access_token={1}'.format(WECHAT_URL, accessToken)
            query1 = "db.collection('%s').where({putSno: '%s'}).limit(100).get()" % (collection_name, sno)
            data1 = {
                "env": ENV,
                "query": query1
            }
            query2 = "db.collection('%s').where({getSno: '%s'}).limit(100).get()" % (collection_name, sno)
            data2 = {
                "env": ENV,
                "query": query2
            }
            response1 = requests.post(url, data=json.dumps(data1))
            # print('查询数据：' + response.text)
            # print('--------------------')
            # result = response.json()
            # print(result)
            all_data1 = response1.json()['data']

            response2 = requests.post(url, data=json.dumps(data2))
            all_data2 = response2.json()['data']
        # print(data)
        good_list = []
        good_info = []
        for item in all_data1:
            item_data = json.loads(item)
            temp1 = []
            temp1.append(item_data['orderId'])
            temp1.append(item_data['putSno'])
            temp1.append(item_data['getSno'])
            temp1.append(item_data['type'])
            temp1.append(item_data['status'])
            good_list.append(temp1)
            # print(temp)
            temp2 = []
            if item_data['type'] == '带货':
                temp2.append(item_data['good'])
                temp2.append(item_data['putAddr'])
                temp2.append(item_data['getAddr'])
                temp2.append(item_data['date'])
                temp2.append(item_data['money'])
                temp2.append(item_data['credit'])
                temp2.append(item_data['message'])
                temp2.append(item_data['evaluate'])
                temp2.append(item_data['score'])
            elif item_data['type'] == '带人':
                temp2.append(item_data['putAddr'])
                temp2.append(item_data['getAddr'])
                temp2.append(item_data['date'])
                temp2.append(item_data['money'])
                temp2.append(item_data['credit'])
                temp2.append(item_data['message'])
                temp2.append(item_data['evaluate'])
                temp2.append(item_data['score'])
            else:
                temp2.append(item_data['size'])
                temp2.append(item_data['color'])
                temp2.append(item_data['way'])
                temp2.append(item_data['num'])
                temp2.append(item_data['message'])
            good_info.append(temp2)

        if sno == '':
            return good_list, good_info

        # print(data)
        for item in all_data2:
            item_data = json.loads(item)
            temp1 = []
            temp1.append(item_data['orderId'])
            temp1.append(item_data['putSno'])
            temp1.append(item_data['getSno'])
            temp1.append(item_data['type'])
            temp1.append(item_data['status'])
            good_list.append(temp1)
            # print(temp)
            temp2 = []
            if item_data['type'] == '带货':
                temp2.append(item_data['good'])
                temp2.append(item_data['getAddr'])
                temp2.append(item_data['putAddr'])
                temp2.append(item_data['date'])
                temp2.append(item_data['money'])
                temp2.append(item_data['credit'])
                temp2.append(item_data['message'])
                temp2.append(item_data['evaluate'])
                temp2.append(item_data['score'])
            elif item_data['type'] == '带人':
                temp2.append(item_data['getAddr'])
                temp2.append(item_data['putAddr'])
                temp2.append(item_data['date'])
                temp2.append(item_data['money'])
                temp2.append(item_data['credit'])
                temp2.append(item_data['message'])
                temp2.append(item_data['evaluate'])
                temp2.append(item_data['score'])
            else:
                temp2.append(item_data['size'])
                temp2.append(item_data['color'])
                temp2.append(item_data['way'])
                temp2.append(item_data['num'])
                temp2.append(item_data['message'])
            good_info.append(temp2)
        # print('!!!!!!!!!!!!!!!!!!')
        # print(good_list)
        # print(good_info)
        return good_list, good_info
        # print(good_list)

    @classmethod
    def delete_order(self, orderId):
        print(orderId)
        accessToken = self.get_access_token(self)
        # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
        collection_name = 'test4'
        url = '{0}tcb/databasedelete?access_token={1}'.format(WECHAT_URL, accessToken)
        query = "db.collection('%s').where({orderId: '%s'}).remove()" % (collection_name, orderId)
        data = {
            "env": ENV,
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print('--------------------')
        # print(response)
        data = response.json()
        print(data)
        if data['deleted'] == 1:
            return True
        else:
            return False

    @classmethod
    def search_user(self, sno):
        print(sno)
        if sno == '':
            accessToken = self.get_access_token(self)
            # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
            collection_name = 'test5'
            url = '{0}tcb/databasequery?access_token={1}'.format(WECHAT_URL, accessToken)
            query = "db.collection('%s').limit(100).get()" % (collection_name)
            data = {
                "env": ENV,
                "query": query
            }
            response = requests.post(url, data=json.dumps(data))
        else:
            accessToken = self.get_access_token(self)
            # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
            collection_name = 'test5'
            url = '{0}tcb/databasequery?access_token={1}'.format(WECHAT_URL, accessToken)
            query = "db.collection('%s').where({sno: '%s'}).limit(100).get()" % (collection_name, sno)
            data = {
                "env": ENV,
                "query": query
            }
            response = requests.post(url, data=json.dumps(data))
        print(response)
        data = response.json()['data']
        print(data)
        user_list = []
        for item in data:
            item_data = json.loads(item)
            temp = []
            temp.append(item_data['sno'])
            temp.append(item_data['name'])
            temp.append(item_data['gender'])
            temp.append(item_data['nickname'])
            temp.append(item_data['credit'])
            user_list.append(temp)
        return user_list
        # print(good_list)

    @classmethod
    def update_credit(self, user_info):
        credit = user_info['CREDIT']
        sno = user_info['ID']
        # credit = 80
        # sno = '031802318'
        accessToken = self.get_access_token(self)
        # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
        collection_name = 'test5'
        url = '{0}tcb/databaseupdate?access_token={1}'.format(WECHAT_URL, accessToken)
        query = "db.collection('%s').where({sno: '%s'}).update({data: {credit: %d}})" % (collection_name, sno, credit)
        data = {
            "env": ENV,
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print(response)
        data = response.json()
        print(data)
        if data['modified'] == 1:
            return True
        else:
            return False

    @classmethod
    def delete_user(self, sno):
        accessToken = self.get_access_token(self)
        # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
        collection_name = 'test5'
        url = '{0}tcb/databasedelete?access_token={1}'.format(WECHAT_URL, accessToken)
        query = "db.collection('%s').where({sno: '%s'}).remove()" % (collection_name, sno)
        data = {
            "env": ENV,
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print('--------------------')
        # print(response)
        data = response.json()
        print(data)
        if data['deleted'] == 1:
            return True
        else:
            return False

    @classmethod
    def search_audit(self, sno):
        # print(sno)
        if sno == '':
            accessToken = self.get_access_token(self)
            # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
            collection_name = 'StudentCard'
            url = '{0}tcb/databasequery?access_token={1}'.format(WECHAT_URL, accessToken)
            query = "db.collection('%s').where({access: 0}).limit(100).get()" % (collection_name)
            data = {
                "env": ENV,
                "query": query
            }
            response = requests.post(url, data=json.dumps(data))
        else:
            accessToken = self.get_access_token(self)
            # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
            collection_name = 'StudentCard'
            url = '{0}tcb/databasequery?access_token={1}'.format(WECHAT_URL, accessToken)
            query = "db.collection('%s').where({access: 0, sid: '%s'}).limit(100).get()" % (collection_name, sno)
            data = {
                "env": ENV,
                "query": query
            }
            response = requests.post(url, data=json.dumps(data))
        print(response)
        data = response.json()['data']
        print(data)
        audit_list = []
        for item in data:
            item_data = json.loads(item)
            temp = []
            temp.append(item_data['sid'])
            temp.append(item_data['name'])
            temp.append(item_data['addr'])
            temp.append(item_data['_openid'])
            audit_list.append(temp)
        return audit_list
        # print(good_list)

    @classmethod
    def get_image(self, image):
        accessToken = self.get_access_token(self)
        # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
        # collection_name = 'StudentCard'
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

        return img_src

    @classmethod
    def user_access(self, sno):
        accessToken = self.get_access_token(self)
        # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
        collection_name = 'StudentCard'
        url = '{0}tcb/databaseupdate?access_token={1}'.format(WECHAT_URL, accessToken)
        query = "db.collection('%s').where({sid: '%s'}).update({data: {access: 1}})" % (collection_name, sno)
        data = {
            "env": ENV,
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print(response)
        data = response.json()
        print(data)
        if data['modified'] == 1:
            return True
        else:
            return False

    @classmethod
    def search_order_business(self, sno):
        if sno == '':
            accessToken = self.get_access_token(self)
            # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
            collection_name = 'test4'
            url = '{0}tcb/databasequery?access_token={1}'.format(WECHAT_URL, accessToken)
            query1 = "db.collection('%s').where({type: '打印', status: '待完成'}).limit(100).get()" % (collection_name)
            data1 = {
                "env": ENV,
                "query": query1
            }
            response1 = requests.post(url, data=json.dumps(data1))
            all_data1 = response1.json()['data']
        else:
            accessToken = self.get_access_token(self)
            # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
            collection_name = 'test4'
            url = '{0}tcb/databasequery?access_token={1}'.format(WECHAT_URL, accessToken)
            query1 = "db.collection('%s').where({putSno: '%s', type: '打印', status: '待完成'}).limit(100).get()" % (collection_name, sno)
            data1 = {
                "env": ENV,
                "query": query1
            }
            response1 = requests.post(url, data=json.dumps(data1))
            all_data1 = response1.json()['data']
        good_list = []
        good_info = []
        for item in all_data1:
            item_data = json.loads(item)
            # print(item_data)
            temp1 = []
            temp1.append(item_data['orderId'])
            temp1.append(item_data['putSno'])
            temp1.append(item_data['status'])
            temp1.append(item_data['file'])
            good_list.append(temp1)
            temp2 = []
            temp2.append(item_data['size'])
            temp2.append(item_data['color'])
            temp2.append(item_data['way'])
            temp2.append(item_data['num'])
            temp2.append(item_data['message'])
            good_info.append(temp2)
        return good_list, good_info

    @classmethod
    def get_file(self, src_list):
        accessToken = self.get_access_token(self)
        # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
        collection_name = 'StudentCard'
        url = '{0}tcb/batchdownloadfile?access_token={1}'.format(WECHAT_URL, accessToken)
        file_list = []
        for item in src_list:
            temp = {}
            temp['fileid'] = item
            temp['max_age'] = 7200
            file_list.append(temp)
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

    @classmethod
    def print_finish(self, orderId):
        accessToken = self.get_access_token(self)
        # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
        collection_name = 'test4'
        url = '{0}tcb/databaseupdate?access_token={1}'.format(WECHAT_URL, accessToken)
        query = "db.collection('%s').where({orderId: '%s'}).update({data: {status: '已完成'}})" % (collection_name, orderId)
        data = {
            "env": ENV,
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print(response)
        data = response.json()
        print(data)
        if data['modified'] == 1:
            return True
        else:
            return False

    @classmethod
    def call_cloud_function(self, id):
        print(id)
        accessToken = self.get_access_token(self)
        url = 'https://api.weixin.qq.com/tcb/invokecloudfunction'
        # url = '{0}tcb/invokecloudfunction?access_token={1}'.format(WECHAT_URL, accessToken)
        data = {
            'openid': id
        }
        params = {
            'access_token': accessToken,
            'env': ENV,
            'name': 'access',
        }
        # query = "db.collection('%s').where({sno: '%s'}).update({data: {credit: %d}})" % (collection_name, sno, credit)
        # data = {
        #     "env": ENV,
        #     'name': 'access',
        # }
        response = requests.post(url, params=params, json=data)
        print(response)
        data = response.json()
        print(data)

    @classmethod
    def search_feedback(self, sno):
        if sno == '':
            accessToken = self.get_access_token(self)
            # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
            collection_name = 'yijian'
            url = '{0}tcb/databasequery?access_token={1}'.format(WECHAT_URL, accessToken)
            query1 = "db.collection('%s').limit(100).get()" % (collection_name)
            data1 = {
                "env": ENV,
                "query": query1
            }
            response1 = requests.post(url, data=json.dumps(data1))
            all_data1 = response1.json()['data']
        else:
            accessToken = self.get_access_token(self)
            # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
            collection_name = 'yijian'
            url = '{0}tcb/databasequery?access_token={1}'.format(WECHAT_URL, accessToken)
            query1 = "db.collection('%s').where({sno: '%s'}).limit(100).get()" % (collection_name, sno)
            data1 = {
                "env": ENV,
                "query": query1
            }
            response1 = requests.post(url, data=json.dumps(data1))
            all_data1 = response1.json()['data']
        good_list = []
        good_info = []
        for item in all_data1:
            item_data = json.loads(item)
            # print(item_data)
            temp1 = []
            temp1.append(item_data['id'])
            temp1.append(item_data['sno'])
            temp1.append(item_data['contact'])
            good_list.append(temp1)
            temp2 = []
            temp2.append(item_data['content'])
            good_info.append(temp2)
        return good_list, good_info


    @classmethod
    def finish_feedback(self, id):
        # print(id)
        accessToken = self.get_access_token(self)
        # accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
        collection_name = 'yijian'
        url = '{0}tcb/databasedelete?access_token={1}'.format(WECHAT_URL, accessToken)
        query = "db.collection('%s').where({id: '%s'}).remove()" % (collection_name, id)
        data = {
            "env": ENV,
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print('--------------------')
        # print(response)
        data = response.json()
        print(data)
        if data['deleted'] == 1:
            return True
        else:
            return False

# obj = DataBase()
# obj.search_feedback('')