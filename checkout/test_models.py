from django.test import TestCase
from django.contrib.auth.models import User

from .models import Order, OrderLineItem
from menu.models import MenuItem
from profiles.models import UserProfile


class TestCheckoutModels(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create_user(username='test_user',
                                              email='test@test.com',
                                              password='test')

        cls.user_1.userprofile.default_phone_number = 123456789
        cls.user_1.userprofile.default_street_address1 = 'Test street 1'
        cls.user_1.userprofile.default_street_address2 = 'Test street 2'
        cls.user_1.userprofile.default_town_or_city = 'Test town city'
        cls.user_1.userprofile.default_county = 'Test county'
        cls.user_1.userprofile.default_postcode = 'Test postcode'
        cls.user_1.userprofile.default_country = 'IE'

        cls.menu_item = MenuItem.objects.create(price=12.00)

        cls.order = Order.objects.create(order_number='32342384723853',
                                         user_profile=cls.user_1.userprofile,
                                         full_name='Test',
                                         email=cls.user_1.email,
                                         phone_number='1231321321',
                                         country=cls.user_1.
                                         userprofile.default_country,
                                         town_or_city='Test',
                                         street_address1='Test',
                                         delivery_cost=1.00,
                                         order_total=10.00,
                                         grand_total=11.00,
                                         original_bag='Test',
                                         stripe_pid='Test')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()
        cls.menu_item.delete()
        cls.order.delete()

    def test_order_model(self):
        order = Order.objects.create(order_number='32342384723853',
                                     user_profile=self.user_1.userprofile,
                                     full_name='Test',
                                     email=self.user_1.email,
                                     phone_number='1231321321',
                                     country=self.user_1.
                                     userprofile.default_country,
                                     town_or_city='Test',
                                     street_address1='Test',
                                     delivery_cost=1.00,
                                     order_total=10.00,
                                     grand_total=11.00,
                                     original_bag='Test',
                                     stripe_pid='Test')

        self.assertEqual(order.__str__(), order.order_number)
        self.assertTrue(Order.objects.
                        filter(order_number='32342384723853').exists())

    def test_order_line_item_model(self):
        order_line_item = OrderLineItem.objects.create(order=self.order,
                                                       menu_item=self
                                                       .menu_item,
                                                       quantity=1,
                                                       lineitem_total=self
                                                       .menu_item.price)

        self.assertEqual(order_line_item.order, self.order)
        self.assertEqual(order_line_item.menu_item, self.menu_item)
        self.assertEqual(order_line_item.__str__(),
                         f'SKU {self.menu_item.name} on order ' +
                         f'{self.order.order_number}')
        self.assertTrue(OrderLineItem.objects.filter(menu_item=self.menu_item)
                        .exists())
