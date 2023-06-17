from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, reverse

from django.conf import settings
from menu.models import Category, MenuItem
from checkout.models import Order

from cart.contexts import cart_contents

import stripe


class TestCheckoutViews(TestCase):

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

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()

    def setUp(self):
        self.client.login(username=self.user_1.username,
                          password='test')

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

    def tearDown(self):
        self.client.logout()
        self.menu_item_1.delete()
        self.menu_item_2.delete()
        self.category_1.delete()
        self.category_2.delete()

    def test_get_checkout_page(self):
        url_1 = reverse('add_to_cart', args=[self.menu_item_1.id])
        response_1 = self.client.post(url_1,
                                      {
                                        'quantity': 1,
                                        'menu_item_size': 10,
                                        'redirect_url':
                                        f'/menu/{self.menu_item_1.id}/'
                                      })
        url_2 = reverse('checkout')
        response_2 = self.client.get(url_2)

        self.assertEqual(response_2.status_code, 200)
        self.assertTemplateUsed(response_2, 'checkout/checkout.html')
        self.assertTrue(self.client.session['cart'])
        self.assertEqual(self.client.session['cart'],
                         {'1': {'items_by_size': {'10': 1}}})

    def test_post_checkout_page(self):
        url_1 = reverse('add_to_cart', args=[self.menu_item_1.id])
        response_1 = self.client.post(url_1,
                                      {
                                        'quantity': 1,
                                        'menu_item_size': 10,
                                        'redirect_url':
                                        f'/menu/{self.menu_item_1.id}/'
                                      })

        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        current_cart = cart_contents(self.client)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        client_secret = intent.client_secret

        url_3 = reverse('checkout')
        response_3 = self.client.post(url_3,
                                      {
                                        'full_name': 'Chris',
                                        'email': self.user_1.email,
                                        'phone_number': self
                                        .user_1.userprofile
                                        .default_phone_number,
                                        'country': self
                                        .user_1.userprofile
                                        .default_country,
                                        'postcode': self
                                        .user_1.userprofile
                                        .default_postcode,
                                        'town_or_city': self
                                        .user_1.userprofile
                                        .default_town_or_city,
                                        'street_address1': self
                                        .user_1.userprofile
                                        .default_street_address1,
                                        'street_address2': self
                                        .user_1.userprofile
                                        .default_street_address2,
                                        'county': self
                                        .user_1.userprofile
                                        .default_county,
                                        'client_secret': client_secret
                                      })

        order = Order.objects.get(pk=1)

        self.assertEqual(response_3.status_code, 302)
        self.assertRedirects(response_3, '/checkout/checkout_success/' +
                             f'{order.order_number}')
