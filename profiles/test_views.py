from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, reverse, redirect

from .models import UserProfile
from menu.models import Category, MenuItem, Review
from checkout.models import Order


class TestProfileViews(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create_user(username='test_user',
                                              email='test@test.com',
                                              password='test',)

        cls.user_1.userprofile.default_phone_number = 123456789
        cls.user_1.userprofile.default_street_address1 = 'Test street 1'
        cls.user_1.userprofile.default_street_address2 = 'Test street 2'
        cls.user_1.userprofile.default_town_or_city = 'Test town city'
        cls.user_1.userprofile.default_county = 'Test county'
        cls.user_1.userprofile.default_postcode = 'Test postcode'
        cls.user_1.userprofile.default_country = 'IE'

        cls.category_names = ['pizza', 'sides']
        cls.friendly_names = ['Pizza', 'Sides']

        cls.category_1 = Category.objects.create(name=cls.category_names[0],
                                                 friendly_name=cls
                                                 .friendly_names[0])

        cls.category_2 = Category.objects.create(name=cls.category_names[1],
                                                 friendly_name=cls
                                                 .friendly_names[1])

        cls.item_names = ['Test pizza', 'Test side']
        cls.calories = ['Test 1', 'Test 2']
        cls.has_sizes = [True, False]
        cls.prices = [10.00, 5.00]

        cls.menu_item_1 = MenuItem.objects.create(category=cls.category_1,
                                                  name=cls.item_names[0],
                                                  calories=cls.calories[0],
                                                  has_sizes=cls.has_sizes[0],
                                                  price=cls.prices[0])

        cls.menu_item_2 = MenuItem.objects.create(category=cls.category_2,
                                                  name=cls.item_names[1],
                                                  calories=cls.calories[1],
                                                  has_sizes=cls.has_sizes[1],
                                                  price=cls.prices[1])

        cls.order = Order.objects.create(order_number=123212352,
                                         user_profile=cls.user_1.userprofile,
                                         full_name='Test',
                                         email=cls.user_1.email,
                                         phone_number='26127127',
                                         country='IE',
                                         postcode='Test',
                                         town_or_city='Test',
                                         street_address1='Test',
                                         street_address2='Test',
                                         county='Test',
                                         delivery_cost=1.00,
                                         order_total=10.00,
                                         grand_total=11.00,
                                         original_bag='Test',
                                         stripe_pid='Test')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()
        cls.category_1.delete()
        cls.category_2.delete()
        cls.menu_item_1.delete()
        cls.menu_item_2.delete()

    def setUp(self):
        self.client.login(username=self.user_1.username,
                          password='test')

    def tearDown(self):
        self.client.logout()

    def test_get_profile_page(self):
        url_1 = reverse('profile')
        response_1 = self.client.get(url_1)

        self.assertEqual(response_1.status_code, 200)
        self.assertTemplateUsed(response_1, 'profiles/profile.html')

        self.client.logout()

        url_2 = reverse('profile')
        response_2 = self.client.get(url_2)

        self.assertEqual(response_2.status_code, 302)

    def test_post_profile_page(self):
        url_1 = reverse('profile')
        response_1 = self.client.post(url_1,
                                      {
                                        'default_phone_number': '0987654321',
                                        'default_country': 'NZ',
                                        'default_postcode': 'New test',
                                        'default_town_or_city': 'New test',
                                        'default_street_address1': 'New test',
                                        'default_street_address2': 'New test',
                                        'default_county': 'New test',
                                      })

        changed_user_profile = UserProfile.objects.get(user=self.user_1)

        self.assertEqual(changed_user_profile.default_county, 'New test')

        self.client.logout()

        url_2 = reverse('profile')
        response_2 = self.client.post(url_2,
                                      {
                                        'default_phone_number': '0987654321',
                                        'default_country': 'NZ',
                                        'default_postcode': 'New test',
                                        'default_town_or_city': 'New test',
                                        'default_street_address1': 'New test',
                                        'default_street_address2': 'New test',
                                        'default_county': 'New test',
                                      })

        self.assertEqual(response_2.status_code, 302)

    def test_get_order_history_page(self):
        url_1 = reverse('order_history', args=[self.order.order_number])
        response_1 = self.client.get(url_1)

        self.assertEqual(response_1.status_code, 200)
        self.assertTemplateUsed(response_1, 'checkout/checkout_success.html')

        self.client.logout()

        url_2 = reverse('order_history', args=[self.order.order_number])
        response_2 = self.client.get(url_2)

        self.assertEqual(response_2.status_code, 302)
