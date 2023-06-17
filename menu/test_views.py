from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, reverse
from menu.models import Category, MenuItem, Review
from profiles.models import UserProfile


class TestMenuViews(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create_user(username='test_user',
                                              password='test')

        cls.superuser = User.objects.create_superuser(username='test_super',
                                                      password='super',
                                                      email='test@example.com')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()
        cls.superuser.delete()

    def setUp(self):
        self.client.login(username=self.user_1.username,
                          password='test')

        self.category_name = 'pizza'
        self.friendly_name = 'Pizza'

        self.category = Category.objects.create(name=self.category_name,
                                                friendly_name=self
                                                .friendly_name)

        self.item_name = 'Test'
        self.calories = 'Test'
        self.has_sizes = True
        self.price = 10.00

        self.menu_item = MenuItem.objects.create(category=self.category,
                                                 name=self.item_name,
                                                 calories=self.calories,
                                                 has_sizes=self.has_sizes,
                                                 price=self.price)

    def tearDown(self):
        self.client.logout()
        self.menu_item.delete()
        self.category.delete()

    def test_get_menu_page(self):
        url = reverse('menu')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu.html')

    def test_get_menu_item_detail_page(self):
        url = reverse('menu_item_detail', args=[self.menu_item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu_item_detail.html')

    def test_post_menu_item_detail_page(self):
        url = reverse('menu_item_detail', args=[self.menu_item.id])
        response = self.client.post(url,
                                    {
                                        'menu_item': self.menu_item,
                                        'poster': self.user_1,
                                        'review': 'Test',
                                        'rating': 5
                                    })

        review = get_object_or_404(Review, pk=1)

        self.assertEqual(review.menu_item, self.menu_item)
        self.assertEqual(review.poster, self.user_1)
        self.assertEqual(review.get_rating_display(), 'Fantastico!')
        self.assertRedirects(response, f'/menu/{self.menu_item.id}/')

    def test_get_add_menu_item_page(self):
        self.client.logout()
        self.client.login(username=self.superuser.username,
                          password='super')

        url_1 = reverse('add_menu_item')
        response_1 = self.client.get(url_1)

        self.assertEqual(response_1.status_code, 200)
        self.assertTemplateUsed(response_1, 'menu/add_menu_item.html')

        self.client.logout()
        self.client.login(username=self.user_1.username,
                          password='test')

        url_2 = reverse('add_menu_item')
        response_2 = self.client.get(url_2)

        self.assertEqual(response_2.status_code, 302)

        self.client.logout()

        url_3 = reverse('add_menu_item')
        response_3 = self.client.get(url_3)

        self.assertEqual(response_3.status_code, 302)

    def test_post_add_menu_item_page(self):
        self.client.logout()
        self.client.login(username=self.superuser.username,
                          password='super')

        url = reverse('add_menu_item')

        response = self.client.post(url,
                                    {
                                        'category': self.category.id,
                                        'name': 'test 2',
                                        'calories': 'test',
                                        'has_sizes': True,
                                        'price': 12.00,
                                    })

        new_menu_item = get_object_or_404(MenuItem, pk=2)

        self.assertEqual(new_menu_item.name, 'test 2')
        self.assertEqual(new_menu_item.price, 12.00)
        self.assertRedirects(response, f'/menu/{new_menu_item.id}/' +
                             '?source=management')

    def test_get_edit_item_page(self):
        self.client.logout()
        self.client.login(username=self.superuser.username,
                          password='super')

        url_1 = reverse('edit_menu_item', args=[self.menu_item.id])
        response_1 = self.client.get(url_1)

        self.assertEqual(response_1.status_code, 200)

        self.client.logout()
        self.client.login(username=self.user_1.username,
                          password='test')

        url_2 = reverse('edit_menu_item', args=[self.menu_item.id])
        response_2 = self.client.get(url_2)

        self.assertEqual(response_2.status_code, 302)

        self.client.logout()

        url_3 = reverse('edit_menu_item', args=[self.menu_item.id])
        response_3 = self.client.get(url_3)

        self.assertEqual(response_3.status_code, 302)

    def test_post_edit_item_page(self):
        self.client.logout()
        self.client.login(username=self.superuser.username,
                          password='super')

        url = reverse('edit_menu_item', args=[self.menu_item.id])
        response = self.client.post(url,
                                    {
                                        'category': self.menu_item.id,
                                        'name': 'Test 3',
                                        'calories': self.menu_item.calories,
                                        'has_sizes': self.menu_item.has_sizes,
                                        'price': self.menu_item.price
                                    })
        updated_item = MenuItem.objects.get(name='Test 3')

        self.assertEqual(updated_item.name, 'Test 3')
        self.assertFalse(MenuItem.objects.filter(name='Test').exists())

    def test_delete_functionality(self):
        self.client.logout()
        self.client.login(username=self.superuser.username,
                          password='super')

        new_menu_item = MenuItem.objects.create(category=self.category,
                                                name='Test 2',
                                                calories='Test 2',
                                                has_sizes=True,
                                                price='12.00')

        self.assertTrue(MenuItem.objects.filter(name='Test 2').exists())
        self.assertEqual(new_menu_item.id, 2)

        url_1 = reverse('delete_menu_item', args=[new_menu_item.id])
        response_1 = self.client.post(url_1)

        self.assertFalse(MenuItem.objects.filter(name='Test 2').exists())
        self.assertRedirects(response_1, '/menu/?source=management')

        self.client.logout()
        self.client.login(username=self.user_1.username,
                          password='test')

        new_menu_item = MenuItem.objects.create(category=self.category,
                                                name='Test 2',
                                                calories='Test 2',
                                                has_sizes=True,
                                                price='12.00')

        url_2 = reverse('delete_menu_item', args=[new_menu_item.id])
        response_2 = self.client.post(url_2)

        self.assertTrue(MenuItem.objects.filter(name='Test 2').exists())
        self.assertEqual(response_1.status_code, 302)

    def test_favourite_functionality(self):
        user_profile_1 = get_object_or_404(UserProfile, user=self.user_1)

        url_1 = reverse('favourite_item', args=[self.menu_item.id])
        response_1 = self.client.post(url_1)

        changed_user_profile = get_object_or_404(UserProfile,
                                                 favourite_menu_item=self
                                                 .menu_item)

        self.assertRedirects(response_1, f'/menu/{self.menu_item.id}/')
        self.assertEqual(changed_user_profile.favourite_menu_item.name, 'Test')

        url_2 = reverse('favourite_item', args=[self.menu_item.id])
        response_2 = self.client.post(url_2)

        self.assertFalse(UserProfile.objects.filter
                         (favourite_menu_item=self.menu_item).exists())

        new_menu_item = MenuItem.objects.create(category=self.category,
                                                name='Test 2',
                                                calories='Test 2',
                                                has_sizes=True,
                                                price='12.00')

        url_3 = reverse('favourite_item', args=[new_menu_item.id])
        response_3 = self.client.post(url_3)

        self.assertFalse(UserProfile.objects.filter
                         (favourite_menu_item=self.menu_item).exists())

        self.assertTrue(UserProfile.objects.filter
                        (favourite_menu_item=new_menu_item).exists())

        self.client.logout()

        url_4 = reverse('favourite_item', args=[new_menu_item.id])
        response_4 = self.client.post(url_4)

        self.assertEqual(response_4.status_code, 302)
