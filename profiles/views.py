from django.shortcuts import render


from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import UserProfile
from .forms import UserProfileForm

from menu.models import Review
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)

    reviews_rating_order = (Review.objects.filter(poster=profile.user)
                            .order_by('-rating'))

    review_counts = {}
    review_counts['All'] = reviews_rating_order.count()
    total_rating = 0

    for review in reviews_rating_order:
        if review_counts.get(review.get_rating_display()[:-1]):
            review_counts[review.get_rating_display()[:-1]] += 1
        else:
            review_counts[review.get_rating_display()[:-1]] = 1

        total_rating += review.rating

    if 'rating_word' in request.GET:
        if request.GET['rating_word'] != 'All':
            for review in reviews_rating_order:
                if request.GET['rating_word'] == (review.
                                                  get_rating_display()):
                    reviews = (Review.objects.filter(rating=review.rating)
                               .order_by('-created_on'))
                    break
        else:
            reviews = (Review.objects.filter(poster=profile.user)
                       .order_by('-created_on'))
    else:
        reviews = (Review.objects.filter(poster=profile.user)
                   .order_by('-created_on'))

    paginated_reviews_profile = Paginator(reviews, 9)

    if not request.GET.get("page"):
        page_number = '1'
    else:
        page_number = request.GET.get("page")

    page_obj_profile = paginated_reviews_profile.get_page(page_number)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'reviews': page_obj_profile,
        'review_counts': review_counts,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
