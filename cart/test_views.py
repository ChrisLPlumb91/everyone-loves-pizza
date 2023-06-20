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

    def test_view_cart_page(self):
        url = reverse('view_cart')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_add_to_cart(self):
        url_1 = reverse('add_to_cart', args=[self.menu_item_1.id])
        response_1 = self.client.post(url_1,
                                      {
                                        'quantity': 1,
                                        'menu_item_size': 10,
                                        'redirect_url':
                                        f'/menu/{self.menu_item_1.id}/'
                                      })

        self.assertEqual(response_1.status_code, 302)
        self.assertRedirects(response_1, f'/menu/{self.menu_item_1.id}/')
        self.assertTrue(self.client.session['cart'])
        self.assertEqual(self.client.session['cart'],
                         {'1': {'items_by_size': {'10': 1}}})

        url_2 = reverse('add_to_cart', args=[self.menu_item_2.id])
        response_2 = self.client.post(url_2,
                                      {
                                        'quantity': 3,
                                        'redirect_url':
                                        f'/menu/{self.menu_item_2.id}/'
                                      })

        self.assertEqual(response_2.status_code, 302)
        self.assertRedirects(response_2, f'/menu/{self.menu_item_2.id}/')
        self.assertTrue(self.client.session['cart'])
        self.assertEqual(self.client.session['cart'],
                         {'1': {'items_by_size': {'10': 1}}, '2': 3})

    def test_adjust_cart(self):
        url_1 = reverse('add_to_cart', args=[self.menu_item_1.id])
        response_1 = self.client.post(url_1,
                                      {
                                        'quantity': 1,
                                        'menu_item_size': 10,
                                        'redirect_url':
                                        f'/menu/{self.menu_item_1.id}/'
                                      })

        url_2 = reverse('adjust_cart', args=[self.menu_item_1.id])
        response_2 = self.client.post(url_2,
                                      {
                                        'quantity': 2,
                                        'menu_item_size': 12,
                                      })

        self.assertEqual(response_2.status_code, 302)
        self.assertRedirects(response_2, f'/cart/')
        self.assertTrue(self.client.session['cart'])
        self.assertEqual(self.client.session['cart'],
                         {'1': {'items_by_size': {'10': 1, '12': 2}}})

    def test_remove_from_cart(self):
        url_1 = reverse('add_to_cart', args=[self.menu_item_1.id])
        response_1 = self.client.post(url_1,
                                      {
                                        'quantity': 1,
                                        'menu_item_size': 10,
                                        'redirect_url':
                                        f'/menu/{self.menu_item_1.id}/'
                                      })

        url_2 = reverse('add_to_cart', args=[self.menu_item_2.id])
        response_2 = self.client.post(url_2,
                                      {
                                        'quantity': 3,
                                        'redirect_url':
                                        f'/menu/{self.menu_item_2.id}/'
                                      })

        url_3 = reverse('remove_from_cart', args=[self.menu_item_1.id])
        response_3 = self.client.post(url_3,
                                      {
                                        'menu_item_size': 10,
                                      })

        self.assertEqual(response_3.status_code, 200)
        self.assertTrue(self.client.session['cart'])
        self.assertEqual(self.client.session['cart'], {'2': 3})

        url_4 = reverse('remove_from_cart', args=[self.menu_item_2.id])
        response_4 = self.client.post(url_4)

        self.assertEqual(response_4.status_code, 200)
        self.assertFalse(self.client.session['cart'])
