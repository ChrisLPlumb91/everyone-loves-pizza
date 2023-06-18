from django.test import TestCase
from django.contrib.auth.models import User

from .forms import MenuItemForm, ReviewForm
from .models import Category, MenuItem, Review


class TestMenuForms(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create_superuser(username='test_user',
                                                   email='test@test.com',
                                                   password='test')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()

    def setUp(self):
        self.category_name = 'pizza'
        self.friendly_name = 'Pizza'

        self.category = Category.objects.create(name=self.category_name,
                                                friendly_name=self
                                                .friendly_name)

        self.menu_item = MenuItem.objects.create(name='Test menu item',
                                                 calories='Test calories',
                                                 has_sizes=True,
                                                 price=14.00)

    def tearDown(self):
        self.category.delete()
        self.menu_item.delete()

    def test_menu_item_form(self):
        data_1 = {
                    'name': 'Test',
                    'calories': 'Test',
                    'has_sizes': True,
                    'price': 10.00,
                 }

        form_1 = MenuItemForm(data_1)

        self.assertTrue(form_1.is_valid())
        self.assertEqual(form_1.cleaned_data['price'], 10.00)

        form_1.save()
        self.assertTrue(MenuItem.objects.filter(name='Test')
                        .exists())

        menu_item = MenuItem.objects.create(name='Test 2',
                                            calories='Test 2',
                                            has_sizes=True,
                                            price=10.00)

        data_2 = {
                    'name': 'Test',
                    'calories': 'Test',
                    'has_sizes': True,
                    'price': 12.00,
                 }

        form_2 = MenuItemForm(data_2, instance=menu_item)

        self.assertTrue(form_2.is_valid())
        self.assertEqual(form_2.cleaned_data['price'], 12.00)

        form_2.save()
        self.assertEqual(menu_item.price, 12.00)

        empty_form = MenuItemForm()
        self.assertFalse(empty_form.is_valid())

    def test_review_form(self):
        data_1 = {
                    'review': 'Test',
                    'rating': 5
                 }

        form_1 = ReviewForm(data_1)

        self.assertTrue(form_1.is_valid())
        self.assertEqual(form_1.cleaned_data['review'], 'Test')

        new_review = form_1.save(commit=False)
        new_review.menu_item = self.menu_item
        new_review.poster = self.user_1

        new_review.save()
        self.assertTrue(Review.objects.filter(review='Test')
                        .exists())

        review = Review.objects.create(menu_item=self.menu_item,
                                       poster=self.user_1,
                                       review='Test 2',
                                       rating=5)

        data_2 = {
                    'review': 'Test 2',
                    'rating': 3
                 }

        form_2 = ReviewForm(data_2, instance=review)

        self.assertTrue(form_2.is_valid())
        self.assertEqual(form_2.cleaned_data['rating'], 3)

        form_2.save()

        self.assertEqual(review.rating, 3)

        empty_form = ReviewForm()
        self.assertFalse(empty_form.is_valid())
