from django.shortcuts import render
from .models import Book
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from BookStoreProject.shopping_cart.models import Order
#from django.views.generic import ListView


# Create your views here.
def book_list(request):
    object_list = Book.objects.all()

    context = {
        'object_list': object_list,

    }
    return render(request, "book/shop.html", context)


@login_required
def single_book(request, id):
    single = Book.objects.get(id=id)
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]
    return render(request, 'book/book-single.html', {'singleBook': single, 'current_order_products': current_order_products})


#class SearchResultsView(ListView):
    #model = Book
    #template_name = 'book/search_results.html'

    #def get_queryset(self, q):
        #books_list = Book.objects.filter(title=q)
        #return books_list


def search(request):
    name = request.GET['q']
    books_list = Book.objects.filter(title=name)
    return render(request, 'book/search_results.html', {'books_list': books_list})




