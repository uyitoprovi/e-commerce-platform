from django.shortcuts import redirect, render
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem
from .tasks import order_created

# Create your views here.


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            # Create OrderItem for each item in the cart
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            # Clear the cart
            cart.clear()
            # order_created.delay(order.id)
            # return render(request, "orders/order/created.html", {"order": order})
            order_created.delay(order.id)
            # set the order in the session
            request.Session["order_id"] = order.id
            # redirect for payment
        return redirect("payment:process")
    else:
        form = OrderCreateForm()

    return render(request, "orders/order/create.html", {"cart": cart, "form": form})
