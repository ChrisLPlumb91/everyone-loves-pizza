from django.test import TestCase
from django.shortcuts import get_object_or_404, redirect, reverse
from home.models import CustomerMessage
from menu.models import Category, MenuItem
from django.contrib.auth.models import User


class TestHomeViews(TestCase):

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
                                                friendly_name=self
                                                .friendly_name)

        self.item_name = 'Test'
        self.calories = 'Test'
        self.has_sizes = True
        self.price = 10.00

        for x in range(4):
            MenuItem.objects.create(category=self.category,
                                    name=self.item_name,
                                    calories=self.calories,
                                    has_sizes=self.has_sizes,
                                    price=self.price)

    def tearDown(self):
        self.client.logout()
        menu_items = MenuItem.objects.all()
        for item in menu_items:
            item.delete()
        self.category.delete()

    def test_view_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_view_contact_page(self):
        url = reverse('contact_us')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact_us.html')

    def test_post_contact_page(self):
        url = reverse('contact_us')
        response = self.client.post(url,
                                    {
                                        'customer': self.user_1,
                                        'reason': 1,
                                        'user_msg': 'Test',
                                    })
        customer_msg = CustomerMessage.objects.get(customer=self.user_1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(customer_msg.customer, self.user_1)
        self.assertEqual(customer_msg.get_reason_display(), 'Giving feedback')
        self.assertEqual(customer_msg.reason, 1)
