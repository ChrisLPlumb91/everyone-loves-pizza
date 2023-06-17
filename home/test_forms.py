from django.test import TestCase
from django.contrib.auth.models import User
from .forms import CustomerMessageForm
from .models import CustomerMessage


class TestHomeForm(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create_superuser(username='test_user',
                                                   email='test@test.com',
                                                   password='test')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()

    def test_customer_message_form(self):
        customer_msg = CustomerMessage.objects.create(customer=self.user_1,
                                                      reason=1,
                                                      user_msg='Test')

        data = {'reason': 2, 'user_msg': 'Test 2'}

        form = CustomerMessageForm(data, instance=customer_msg)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['user_msg'], 'Test 2')
        self.assertEqual(form.fields['user_msg'].label, 'Message')

        empty_form = CustomerMessageForm()
        self.assertFalse(empty_form.is_valid())
