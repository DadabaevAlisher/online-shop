from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

        for item in cart:
            OrderItem.objects.create(
                order = order,
                product = item['product'],
                price = item['price'],
                quantity = item['quantity']

            )
        cart.clear()

        return  render(request, 'orders/order/created.html', {'order': order})
    
    else:
        form = OrderCreateForm(initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        })

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})