from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    query = request.GET.get('search')
    if query:
        products = products.filter(name__icontains=query)

    if category_slug:

        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category = category)


    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'query': query
        }

    return render(request, 'products/product/list.html', context)
    
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id = id, slug = slug, available=True)
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'cart_product_form': cart_product_form 
    }

    return render(request, 'products/product/detail.html', context)
