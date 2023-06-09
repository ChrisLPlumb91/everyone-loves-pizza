from django import forms
from .widgets import CustomClearableFileInput
from .models import MenuItem, Category, Review


class MenuItemForm(forms.ModelForm):

    class Meta:
        model = MenuItem
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    full_image = forms.ImageField(label='Full Image', required=False,
                                  widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'review',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['review'].widget.attrs['rows'] = 7
        self.fields['review'].widget.attrs['placeholder'] = ("How was " +
                                                             "the pizza? " +
                                                             "We'd love " +
                                                             "to know!")
