from django.test import TestCase
from django.contrib.auth.models import User

from .models import CustomerMessage


class TestHomeModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create_superuser(username='test_user',
                                                   email='test@test.com',
                                                   password='test')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()

    def test_customer_message_model(self):
        customer_msg = CustomerMessage.objects.create(customer=self.user_1,
                                                      reason=1,
                                                      user_msg='Test')
        self.assertEqual(customer_msg.__str__(), f'The user {self.user_1} ' +
                         f'sent a message to the staff on ' +
                         f'{customer_msg.created_on} ' +
                         f'for the following reason: ' +
                         f'{customer_msg.get_reason_display()}')
        self.assertTrue(CustomerMessage.objects.filter(reason=1).exists())
