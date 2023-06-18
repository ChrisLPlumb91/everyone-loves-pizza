from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import UserProfile


class TestProfilesModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create_user(username='test_user',
                                              email='test@test.com',
                                              password='test')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()

    def test_user_profile_model(self):
        self.assertTrue(UserProfile.objects.filter(user=self.user_1).exists())

        user_profile = get_object_or_404(UserProfile, user=self.user_1)
        self.assertEqual(user_profile.__str__(), self.user_1.username)
