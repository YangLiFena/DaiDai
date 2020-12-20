import unittest
import json
import requests
from model.database import DataBase


class Test(unittest.TestCase):

    def test_get_access_token(self):
        self.assertIsNotNone(DataBase.get_access_token(self))

    def test_search_order(self):
        DataBase.search_order('')
        DataBase.search_order('031802318')
        DataBase.search_order('031802331')
        DataBase.search_order('111')
        # DataBase.search_order('0a4429175fc0b62200640c515c1af839')
        # DataBase.search_order('e62469b25fc0b7510072d18b5a328c39')

        # self.assertIsNotNone(DataBase.search_order(''))


    def test_delete_order(self):
        # self.assertIsNotNone(DataBase.delete_order(self))
        DataBase.delete_order('e62469b25fc0b8600072db5c38102145')
        DataBase.delete_order('2a7b532a5fc8c8bd00c16a347ea03d7a')
        DataBase.delete_order('11')

    def test_search_user(self):
        # self.assertIsNotNone(DataBase.search_user(self))
        DataBase.search_user('')
        DataBase.search_user('031802318')
        DataBase.search_user('111')


    def test_update_credit(self):
        # self.assertIsNotNone(DataBase.update_credit(self))
        info = {}
        info['CREDIT'] = 99
        info['ID'] = '031802331'
        DataBase.update_credit(info)
        info2 = {}
        info2['CREDIT'] = 99
        info2['ID'] = '031812315'
        DataBase.update_credit(info2)

    def test_delete_user(self):
        # self.assertIsNotNone(DataBase.delete_user(self))
        DataBase.delete_user('031802318')
        DataBase.delete_user('000000100')
        DataBase.delete_user('111')


    def test_search_audit(self):
        # self.assertIsNotNone(DataBase.search_audit(self))
        DataBase.search_audit('')
        DataBase.search_audit('031802318')
        DataBase.search_audit('031812318')
        DataBase.search_audit('1111')

    def test_get_image(self):
        # self.assertIsNotNone(DataBase.get_image(self))
        DataBase.get_image('cloud://yuntest-1ge0b9sqe0319f10.7975-yuntest-1ge0b9sqe0319f10-1304211863/StudentCard/StudentCard2670478.png')
        DataBase.get_image('11')

    def test_user_access(self):
        # self.assertIsNotNone(DataBase.user_access(self))
        DataBase.user_access('031802318')
        DataBase.user_access('031812318')
        DataBase.user_access('11')

    def test_search_order_business(self):
        # self.assertIsNotNone(DataBase.search_order_business(self))
        DataBase.search_order_business('')
        DataBase.search_order_business('031802318')
        DataBase.search_order('11')

    def test_get_file(self):
        # self.assertIsNotNone(DataBase.get_file(self))
        DataBase.get_file(['cloud://yuntest-1ge0b9sqe0319f10.7975-yuntest-1ge0b9sqe0319f10-1304211863/2855057.doc'])

    def test_print_finish(self):
        # self.assertIsNotNone(DataBase.print_finish(self))
        DataBase.print_finish('12')
        DataBase.print_finish('c89bd61c5fd4a35a0138ee6e47864925')
        DataBase.print_finish('0bcbdde05fd360f40120ba490894dbd9')

    def test_search_feedback(self):
        # self.assertIsNotNone(DataBase.search_feedback(self))
        DataBase.search_feedback('031802318')
        DataBase.search_feedback('')


    def test_finish_feedback(self):
        # self.assertIsNotNone(DataBase.finish_feedback(self))
        DataBase.finish_feedback('7')
        DataBase.finish_feedback('8')
        DataBase.finish_feedback(8)
        DataBase.finish_feedback('11111')



if __name__ == '__main__':
    unittest.main()