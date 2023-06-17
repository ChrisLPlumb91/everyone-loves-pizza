from django.test import TestCase
from django.shortcuts import get_object_or_404, redirect, reverse
from menu.models import Category, MenuItem
from django.contrib.auth.models import User


class TestCartViews(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create_user(username='test_user',
                                              password='test')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()

    def setUp(self):
        self.client.login(username=self.user_1.username,
                          password='test')

        self.category_name = 'pizza'
        self.friendly_name = 'Pizza'

        self.category = Category.objects.create(name=self.category_name,
                                                friendly_name=self.friendly_name)

        self.item_name = 'Test'
        self.calories = 'Test'
        self.has_sizes = True
        self.price = 10.00

        self.menu_item = MenuItem.objects.create(category=self.category,
                                                 name=self.item_name,
                                                 calories=self.calories,
                                                 has_sizes=self.has_sizes,
                                                 price=self.price)

    def tearDown(self):
        self.client.logout()
        self.menu_item.delete()

    def test_view_cart_page(self):
        response = self.client.get('cart/')

    def test_add_to_cart(self):
        url = f'cart/add/{self.menu_item.id}'

        response = self.client.post(url,
                                    {
                                        'quantity': 1,
                                        'menu_item_size': 10,
                                    })

        self.assertRedirects(response, f'menu/{menu_item.id}')
