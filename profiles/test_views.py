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

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()

    def setUp(self):
        self.client.login(username=self.user_1.username,
                          password='test')

        self.user_1.userprofile.default_phone_number = 123456789
        self.user_1.userprofile.default_street_address1 = 'Test street 1'
        self.user_1.userprofile.default_street_address2 = 'Test street 2'
        self.user_1.userprofile.default_town_or_city = 'Test town city'
        self.user_1.userprofile.default_county = 'Test county'
        self.user_1.userprofile.default_postcode = 'Test postcode'
        self.user_1.userprofile.default_country = 'IE'

        self.category_names = ['pizza', 'sides']
        self.friendly_names = ['Pizza', 'Sides']

        self.category_1 = Category.objects.create(name=self.category_names[0],
                                                  friendly_name=self
                                                  .friendly_names[0])

        self.category_2 = Category.objects.create(name=self.category_names[1],
                                                  friendly_name=self
                                                  .friendly_names[1])

        self.item_names = ['Test pizza', 'Test side']
        self.calories = ['Test 1', 'Test 2']
        self.has_sizes = [True, False]
        self.prices = [10.00, 5.00]

        self.menu_item_1 = MenuItem.objects.create(category=self.category_1,
                                                   name=self.item_names[0],
                                                   calories=self.calories[0],
                                                   has_sizes=self.has_sizes[0],
                                                   price=self.prices[0])

        self.menu_item_2 = MenuItem.objects.create(category=self.category_2,
                                                   name=self.item_names[1],
                                                   calories=self.calories[1],
                                                   has_sizes=self.has_sizes[1],
                                                   price=self.prices[1])

        self.order = Order.objects.create(order_number=123212352,
                                          user_profile=self.user_1.userprofile,
                                          full_name='Test',
                                          email=self.user_1.email,
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

    def tearDown(self):
        self.client.logout()
        self.category_1.delete()
        self.category_2.delete()
        self.menu_item_1.delete()
        self.menu_item_2.delete()
        self.order.delete()

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
