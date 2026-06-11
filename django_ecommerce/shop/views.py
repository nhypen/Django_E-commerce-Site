from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, OrderItem
from .forms import CartAddProductForm, OrderCreateForm
from .cart import Cart


def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, "shop/product_list.html", {"products": products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    form = CartAddProductForm()
    return render(
        request,
        "shop/product_detail.html",
        {
            "product": product,
            "form": form,
        },
    )


def cart_detail(request):
    cart = Cart(request)
    return render(request, "shop/cart.html", {"cart": cart})


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = CartAddProductForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data["quantity"]
            cart.add(product=product, quantity=quantity)

    return redirect("cart_detail")


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart_detail")


def checkout(request):
    cart = Cart(request)

    if len(cart) == 0:
        return redirect("product_list")

    if request.method == "POST":
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )

            cart.clear()
            return render(request, "shop/order_success.html", {"order": order})
    else:
        form = OrderCreateForm()

    return render(
        request,
        "shop/checkout.html",
        {
            "cart": cart,
            "form": form,
        },
    )