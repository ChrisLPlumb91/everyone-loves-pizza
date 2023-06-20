from django.db import models
from django.contrib.auth.models import User

RATING = (('', 'Niente...'), (1, 'Disgustoso!'), (2, 'Brutto!'),
          (3, 'Bene!'), (4, 'Eccellente!'), (5, 'Fantastico!'))


class Category(models.Model):
    """ A model representing categories that items on the menu fall under."""
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=15)
    friendly_name = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class MenuItem(models.Model):
    """ A model representing items that can be ordered from the menu."""
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=24)
    description = models.TextField(blank=True, default='')
    ingredients = models.TextField(blank=True, default='')
    calories = models.CharField(max_length=15)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    full_image_url = models.URLField(max_length=1024, null=True, blank=True)
    full_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """ A model representing reviews left by users on menu items."""
    menu_item = models.ForeignKey(MenuItem, null=False, blank=False,
                                  on_delete=models.CASCADE,
                                  related_name='item_reviews')
    poster = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='user_reviews')
    review = models.TextField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING, default=0)

    def __str__(self):
        return (f'This {self.rating}-star review was posted by ' +
                f'{self.poster} on {self.created_on}, ' +
                f'and reads as follows: "{self.review}".')
