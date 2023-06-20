from django.shortcuts import render


from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import UserProfile
from .forms import UserProfileForm

from home.models import CustomerMessage, REASONS
from menu.models import Review, RATING
from checkout.models import Order


@login_required
def profile(request):
    """
    Display the user's profile, including their favourite item,
    their default delivery information, their order history,
    their review history, and their private message history.
    """
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

    for rating_pair in RATING:
        if rating_pair[1] == 'Niente...':
            continue

        if rating_pair[1][:-1] in review_counts.keys():
            continue
        else:
            review_counts[rating_pair[1][:-1]] = 0

    reviews = 0

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

    if reviews:
        paginated_reviews_profile = Paginator(reviews, 9)

        if not request.GET.get("page"):
            page_number = '1'
        else:
            page_number = request.GET.get("page")

        page_obj_profile = paginated_reviews_profile.get_page(page_number)
    else:
        if request.GET.get('rating_word'):
            messages.info(request, 'You have not left any '
                          'reviews with this rating.')

        reviews = (Review.objects.filter(poster=profile.user)
                   .order_by('-created_on'))

        paginated_reviews_profile = Paginator(reviews, 9)

        if not request.GET.get("page"):
            page_number = '1'
        else:
            page_number = request.GET.get("page")

        page_obj_profile = paginated_reviews_profile.get_page(page_number)

    messages_reason_order = (CustomerMessage.objects.filter
                             (customer=profile.user)
                             .order_by('reason'))

    user_message_counts = {}
    user_message_counts['All'] = messages_reason_order.count()

    for message in messages_reason_order:
        if user_message_counts.get(message.get_reason_display()):
            user_message_counts[message.get_reason_display()] += 1
        else:
            user_message_counts[message.get_reason_display()] = 1

    for reason_pair in REASONS:
        if reason_pair[1] == 'Choose a reason':
            continue

        if reason_pair[1] in user_message_counts.keys():
            continue
        else:
            user_message_counts[reason_pair[1]] = 0

    user_messages = 0

    if 'reason_words' in request.GET:
        if request.GET['reason_words'] != 'All':
            for message in messages_reason_order:
                if (request.GET['reason_words'].replace('-', ' ')
                        == message.get_reason_display()):
                    user_messages = (CustomerMessage.objects.filter
                                     (reason=message.reason)
                                     .order_by('-created_on'))
                    break
        else:
            user_messages = (CustomerMessage.objects.filter
                             (customer=profile.user)
                             .order_by('-created_on'))
    else:
        user_messages = (CustomerMessage.objects.filter
                         (customer=profile.user)
                         .order_by('-created_on'))

    if user_messages:
        paginated_messages_profile = Paginator(user_messages, 5)

        if not request.GET.get("msg_page"):
            page_number = '1'
        else:
            page_number = request.GET.get("msg_page")

        page_obj_messages = paginated_messages_profile.get_page(page_number)
    else:
        if request.GET.get('reason_words'):
            messages.info(request, 'You have not sent any messages '
                          'of this type.')

        user_messages = (CustomerMessage.objects.filter
                         (customer=profile.user)
                         .order_by('-created_on'))

        paginated_messages_profile = Paginator(user_messages, 5)

        if not request.GET.get("msg_page"):
            page_number = '1'
        else:
            page_number = request.GET.get("msg_page")

        page_obj_messages = paginated_messages_profile.get_page(page_number)

    orders = profile.orders.all()

    template = 'profiles/profile.html'

    context = {
        'form': form,
        'reviews': page_obj_profile,
        'review_counts': review_counts,
        'user_messages': page_obj_messages,
        'user_message_counts': user_message_counts,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Display the summary page for a given order placed by the user
    in the past.
    """
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
