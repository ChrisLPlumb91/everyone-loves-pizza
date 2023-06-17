from django.test import TestCase
from django.shortcuts import get_object_or_404, redirect, reverse
from menu.models import Category, MenuItem
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


class TestMenuViews(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create_user(username='test_user',
                                              password='test')

        cls.superuser = User.objects.create_superuser(username='test_super',
                                                      password='super',
                                                      email='test@example.com')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()
        cls.superuser.delete()

    def setUp(self):
        self.client.login(username=self.user_1.username,
                          password='test')

        self.category_name = 'pizza'
        self.friendly_name = 'Pizza'

        self.category = Category.objects.create(name=self.category_name,
                                                friendly_name=self
                                                .friendly_name)

        self.item_name = 'Test'
        self.calories = 'Test'
        self.has_sizes = True
        self.price = 10.00

        self.menu_item = MenuItem.objects.create(category=self.category,
                                                 name=self.item_name,
                                                 calories=self.calories,
                                                 has_sizes=self.has_sizes,
                                                 price=self.price)

        self.file = SimpleUploadedFile("file.txt", b"file_content")

    def tearDown(self):
        self.client.logout()
        self.menu_item.delete()

    def test_get_menu_page(self):
        url = reverse('menu')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu.html')

    def test_get_menu_item_detail_page(self):
        url = reverse('menu_item_detail', args=[self.menu_item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu_item_detail.html')

    def test_get_add_menu_item_page(self):
        self.client.logout()
        self.client.login(username=self.superuser.username,
                          password='super')

        url_1 = reverse('add_menu_item')
        response_1 = self.client.get(url_1)

        self.assertEqual(response_1.status_code, 200)
        self.assertTemplateUsed(response_1, 'menu/add_menu_item.html')

        self.client.logout()
        self.client.login(username=self.user_1.username,
                          password='test')

        url_2 = reverse('add_menu_item')
        response_2 = self.client.get(url_2)

        self.assertEqual(response_2.status_code, 302)

    def test_post_add_menu_item_page(self):
        self.client.logout()
        self.client.login(username=self.superuser.username,
                          password='super')

        url_1 = reverse('add_menu_item')

        response_1 = self.client.post(url_1,
                                      {
                                        'category': self.category,
                                        'name': 'test 2',
                                        'calories': 'test',
                                        'has_sizes': True,
                                        'price': 12.00,
                                      })

        # self.assertEqual(new_menu_item.name, 'test item 2')
        # self.assertEqual(new_menu_item.price, 12.00)
        # self.assertTemplateUsed(response_1, 'menu/add_menu_item.html')
