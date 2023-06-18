from django.test import TestCase
from django.contrib.auth.models import User

from .forms import UserProfileForm


class TestProfilesForm(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create_user(username='test_user',
                                              email='test@test.com',
                                              password='test')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()

    def test_user_profile_form(self):
        data_1 = {
                    'default_phone_number': '89237525215',
                    'default_street_address1': 'Test 1',
                    'default_street_address2': 'Test 1',
                    'default_town_or_city': 'Test 1',
                    'default_county': 'Test 1',
                    'default_postcode': 'Test 1',
                    'default_country': 'IE'
                 }

        form_1 = UserProfileForm(data_1, instance=self.user_1.userprofile)

        self.assertTrue(form_1.is_valid())
        self.assertEqual(form_1.cleaned_data['default_county'], 'Test 1')

        form_1.save()

        self.assertEqual(self.user_1.userprofile.default_county, 'Test 1')
