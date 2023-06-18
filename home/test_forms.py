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

        data_1 = {'reason': 2, 'user_msg': 'Test 2'}

        form_1 = CustomerMessageForm(data_1, instance=customer_msg)

        self.assertTrue(form_1.is_valid())
        self.assertEqual(form_1.cleaned_data['user_msg'], 'Test 2')
        self.assertEqual(form_1.fields['user_msg'].label, 'Message')

        form_1.save()
        self.assertEqual(customer_msg.user_msg, 'Test 2')

        data_2 = {'reason': 3, 'user_msg': 'Test 3'}

        form_2 = CustomerMessageForm(data_2)

        self.assertTrue(form_2.is_valid())
        self.assertEqual(form_2.cleaned_data['user_msg'], 'Test 3')

        new_msg = form_2.save(commit=False)
        new_msg.customer = self.user_1
        new_msg.save()
        self.assertTrue(CustomerMessage.objects.filter(user_msg='Test 3')
                        .exists())

        empty_form = CustomerMessageForm()
        self.assertFalse(empty_form.is_valid())
