from django.test import TestCase
from django.contrib.auth.models import User

from .models import Category, MenuItem, Review


class TestMenuModels(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create_superuser(username='test_user',
                                                   email='test@test.com',
                                                   password='test')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()

    def setUp(self):
        self.menu_item = MenuItem.objects.create(price=12.00)

    def tearDown(self):
        self.menu_item.delete()

    def test_category_model(self):
        category = Category.objects.create(name='test_category_2',
                                           friendly_name='Test Category 2')
        self.assertEqual(category.__str__(), category.name)
        self.assertEqual(category.get_friendly_name(), category.friendly_name)
        self.assertEqual(category.friendly_name, 'Test Category 2')
        self.assertTrue(Category.objects.filter(name='test_category_2')
                        .exists())

        category.delete()

    def test_menu_item_model(self):
        menu_item = MenuItem.objects.create(price=10.00)

        self.assertTrue(MenuItem.objects.filter(price=10.00).exists())
        self.assertEqual(menu_item.price, 10.00)

        self.assertEqual(menu_item.__str__(), '')
        menu_item.name = 'Test Menu Item'
        self.assertEqual(menu_item.__str__(), 'Test Menu Item')

        menu_item.delete()

    def test_review_model(self):
        review = Review.objects.create(menu_item=self.menu_item,
                                       poster=self.user_1)
        self.assertTrue(review)
        self.assertEqual(review.__str__(), f'This {review.rating}-star ' +
                         f'review was posted by {self.user_1} ' +
                         f'on {review.created_on}, ' +
                         f'and reads as follows: "{review.review}".')
        self.assertTrue(Review.objects.filter(menu_item=self.menu_item)
                        .exists())

        review.delete()
