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
        print(result)
        return result['access_token']


    def add_data(self,collectionName,accessToken):
        url = '{0}tcb/databaseadd?access_token={1}'.format(self.WECHAT_URL, accessToken)
        query = "db.collection('%s').add({data:{_id:'112',key:1,value:'2',kj:2}})" % collectionName
        print(query)
        data = {
            "env": self.ENV,  # 云环境ID
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print('2.新增数据：' + response.text)


    def databaseUpdate(self, accessToken, collectionName):
        url = '{0}tcb/databaseupdate?access_token={1}'.format(self.WECHAT_URL, accessToken)
        data = {
            "env": self.ENV,
            # "query": "db.collection('%s').where({_id:'111'}).update({data:{value: 222}})"%collection_name
            "query": "db.collection('%s').doc('111').set({data:{value: 2212}})" % collectionName
        }
        print(data)
        response = requests.post(url, data=json.dumps(data))
        result = response.json()
        print(result)     #将返回值打印


    # 查询某个集合中的数据，代码如下：
    def query_data(self, accessToken, collection_name):
        url = '{0}tcb/databasequery?access_token={1}'.format(self.WECHAT_URL, accessToken)
        query = "db.collection('%s').limit(100).get()" % collection_name
        data = {
            "env": self.ENV,
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print('3.查询数据：' + response.text)
        result = response.json()
        print(result)
        # resultValue =json.loads(result)
        # return resultValue['_id']


    def db(self):
        accessToken = self.get_access_token()
        print('accessToken:', accessToken)
        collectionName = 'Users'
        # add_data(collectionName, accessToken)
        self.query_data(accessToken, collectionName)
        # self.databaseUpdate(accessToken, collectionName)

    def search_order(self):
        # accessToken = self.get_access_token()
        accessToken = '39_9tXYaluroLAq2XQAB7S0wbl9LmaveP5zbjdc9njBqp8ix5xCA_3rAOkec6zN9WftySU3cECYuhKy5yi5q2nyQiJbQNAefGPD7TJtLwHqHRkl4RF5VyrHlh68qK--gzPBcbunQLnLMF6OAk3ZUPOcABAPKJ'
        collection_name = 'test4'
        url = '{0}tcb/databasequery?access_token={1}'.format(WECHAT_URL, accessToken)
        query = "db.collection('%s').where({putSno: '031802318'}).limit(100).get()" % collection_name
        data = {
            "env": ENV,
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        # print('查询数据：' + response.text)
        # print('--------------------')
        # result = response.json()
        # print(result)
        data = response.json()['data']
        print(data)
        good_list = []
        good_info = []
        for item in data:
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
            temp2.append(item_data['good'])
            temp2.append(item_data['getAddr'])
            temp2.append(item_data['putAddr'])
            temp2.append(item_data['date'])
            temp2.append(item_data['money'])
            temp2.append(item_data['credit'])
            temp2.append(item_data['message'])
            temp2.append(item_data['evaluate'])
            temp2.append(item_data['score'])
            good_info.append(temp2)
        return good_list, good_info
        # print(good_list)


# obj = DataBase()
# obj.search_order()