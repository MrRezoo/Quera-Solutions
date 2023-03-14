import json
from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.auth.models import User

from app.models import Post


class TestPost(TestCase):
    fixtures = ['posts', 'comments', 'users']

    def setUp(self):
        self.client = Client()
        self.admin = User.objects.get(username='admin')
        self.user_test_1 = User.objects.get(username='hamid')
        self.user_test_2 = User.objects.get(username='amir')

    def test_post_list(self):
        res = self.client.get(reverse('post_list'))
        data = json.loads(res.content.decode())
        expected = [{'created': '2018-07-18T11:26:53.044000Z', 'owner': 'admin', 'title': 'admin_post_1',
                     'body': 'admin_post_1'},
                    {'created': '2018-07-18T11:27:08.845000Z', 'owner': 'admin', 'title': 'admin_post_2',
                     'body': 'admin_post_2'},
                    {'created': '2018-07-18T11:27:30.623000Z', 'owner': 'hamid', 'title': 'hamid_post_1',
                     'body': 'hamid_post_1'},
                    {'created': '2018-07-18T11:27:40.074000Z', 'owner': 'hamid', 'title': 'hamid_post_2',
                     'body': 'hamid_post_2'},
                    {'created': '2018-07-18T11:28:00.152000Z', 'owner': 'amir', 'title': 'amir_post_1',
                     'body': 'amir_post_1'},
                    {'created': '2018-07-18T11:28:12.013000Z', 'owner': 'amir', 'title': 'amir_post_2',
                     'body': 'amir_post_2'}]
        for i in range(len(expected)):
            self.assertDictEqual(data[i], expected[i])

    def test_create_post(self):
        post_data = {
            "title": "Hello",
            "body": "World"
        }
        post_data = json.dumps(post_data)
        self.client.force_login(self.user_test_1)
        res = self.client.post(reverse('post_list'), content_type="application/json", data=post_data)
        data = json.loads(res.content.decode())
        self.assertEqual(res.status_code, 201)
        expected = {'owner': 'hamid', 'title': 'Hello', 'body': 'World', 'created': '2018-07-18T12:30:02.044738Z'}
        self.assertEqual(expected['owner'], data['owner'])
        self.assertEqual(expected['title'], data['title'])
        self.assertEqual(expected['body'], data['body'])
        self.assertTrue(Post.objects.filter(title='Hello', body="World").exists())
