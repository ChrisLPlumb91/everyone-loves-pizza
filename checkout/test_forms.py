from django.test import TestCase
from django.contrib.auth.models import User

from .forms import OrderForm
from .models import Order


class TestCheckoutModel(TestCase):
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

        cls.order = Order.objects.create(order_number='32342384723853',
                                         user_profile=cls.user_1.userprofile,
                                         full_name='Test',
                                         email=cls.user_1.email,
                                         phone_number='1231321321',
                                         country=cls.user_1.
                                         userprofile.default_country,
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
        cls.order.delete()

    def test_order_form(self):
        data_1 = {
                    'full_name': 'Test 1',
                    'email': self.user_1.email,
                    'phone_number': 12423521,
                    'country': self.user_1.
                    userprofile.default_country,
                    'postcode': 'Test 1',
                    'town_or_city': 'Test 1',
                    'street_address1': 'Test 1',
                    'street_address2': 'Test 1',
                    'county': 'Test 1',
                 }

        form_1 = OrderForm(data_1)

        self.assertTrue(form_1.is_valid())
        self.assertEqual(form_1.cleaned_data['full_name'], 'Test 1')

        new_order = form_1.save(commit=False)
        new_order.order_number = '123225412342'
        new_order.user_profile = self.user_1.userprofile
        new_order.delivery_cost = 1.00
        new_order.order_total = 10.00
        new_order.grand_total = 11.00
        new_order.original_bag = 'Test'
        new_order.stripe_pid = 'Test'
        new_order.save()

        self.assertTrue(Order.objects.filter(order_number='123225412342')
                        .exists())

        order_2 = Order.objects.create(order_number='32463246333',
                                       user_profile=self.user_1.userprofile,
                                       full_name='Test 2',
                                       email=self.user_1.email,
                                       phone_number='452346236',
                                       country=self.user_1.
                                       userprofile.default_country,
                                       postcode='Test 2',
                                       town_or_city='Test 2',
                                       street_address1='Test 2',
                                       street_address2='Test 2',
                                       county='Test 2',
                                       delivery_cost=2.00,
                                       order_total=20.00,
                                       grand_total=22.00,
                                       original_bag='Test 2',
                                       stripe_pid='Test 2')

        data_2 = {
                    'full_name': 'Test 2',
                    'email': self.user_1.email,
                    'phone_number': 314235235345,
                    'country': self.user_1.
                    userprofile.default_country,
                    'postcode': 'Test 2',
                    'town_or_city': 'Test 2',
                    'street_address1': 'Test 2',
                    'street_address2': 'Test 2',
                    'county': 'Test 2',
                 }

        form_2 = OrderForm(data_2, instance=order_2)

        self.assertTrue(form_2.is_valid())
        self.assertEqual(form_2.cleaned_data['phone_number'],
                         '314235235345')

        form_2.save()
        self.assertEqual(order_2.phone_number, '314235235345')

        empty_form = OrderForm()
        self.assertFalse(empty_form.is_valid())
