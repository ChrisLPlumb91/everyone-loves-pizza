from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator

from .models import MenuItem, Category, Review
from .forms import MenuItemForm, ReviewForm


def menu(request):
    """ A view to show the full menu, including sorting and search queries """

    menu_items = MenuItem.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                menu_items = menu_items.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            menu_items = menu_items.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            menu_items = menu_items.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                (messages.error(request, "You didn't enter " +
                 "any search criteria!"))
                return redirect(reverse('menu'))

            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query))
            menu_items = menu_items.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'menu_items': menu_items,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'menu/menu.html', context)


def menu_item_detail(request, menu_item_id):
    """ A view to show individual menu_item details """

    if request.method == 'POST':
        if request.user.is_authenticated:
            menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
            review_form = ReviewForm(request.POST)

            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.menu_item = menu_item
                review.poster = request.user
                review.save()
                print(review)
                messages.success(request, 'Successfully added review! ' +
                                 'Thanks for your feedback on the ' +
                                 f'{review.menu_item.name}!' +
                                 'Please wait for us to approve it!')
                return redirect(reverse('menu_item_detail',
                                        args=[menu_item_id]))
            else:
                messages.error(request, 'Failed to add your review...')
                return redirect(reverse('menu_item_detail',
                                        args=[menu_item_id]))
    else:
        menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
        reviews_rating_order = (Review.objects.filter(menu_item=menu_item)
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

        average_rating = total_rating / reviews_rating_order.count()

        if 'rating_word' in request.GET:
            if request.GET['rating_word'] != 'All':
                for review in reviews_rating_order:
                    if request.GET['rating_word'] == (review.
                                                      get_rating_display()):
                        reviews = (Review.objects.filter(rating=review.rating)
                                   .order_by('-created_on'))
                        break
            else:
                reviews = (Review.objects.filter(menu_item=menu_item)
                           .order_by('-created_on'))
        else:
            reviews = (Review.objects.filter(menu_item=menu_item)
                       .order_by('-created_on'))

        paginated_reviews = Paginator(reviews, 9)
        page_number = request.GET.get("page")
        page_obj = paginated_reviews.get_page(page_number)

        review_form = ReviewForm()

        context = {
            'menu_item': menu_item,
            'reviews': page_obj,
            'review_form': review_form,
            'review_counts': review_counts,
            'rating': average_rating,
        }

        return render(request, 'menu/menu_item_detail.html', context)


@login_required
def add_menu_item(request):
    """ Add an item to the menu """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            menu_item = form.save()
            messages.success(request, 'Successfully added menu item!')
            return redirect(reverse('menu_item_detail', args=[menu_item.id]))
        else:
            messages.error(request, 'Failed to add menu item. ' +
                           'Please ensure the form is valid.')
    else:
        form = MenuItemForm()

    template = 'menu/add_menu_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_menu_item(request, menu_item_id):
    """ Edit an item on the menu """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=menu_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated menu item!')
            return redirect(reverse('menu_item_detail', args=[menu_item.id]))
        else:
            messages.error(request, 'Failed to update menu item. ' +
                           'Please ensure the form is valid.')
    else:
        form = MenuItemForm(instance=menu_item)
        messages.info(request, f'You are editing {menu_item.name}')

    template = 'menu/edit_menu_item.html'
    context = {
        'form': form,
        'menu_item': menu_item,
    }

    return render(request, template, context)


@login_required
def delete_menu_item(request, menu_item_id):
    """ Delete an item from the menu """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    menu_item.delete()
    messages.success(request, 'Menu item deleted!')
    return redirect(reverse('menu'))
