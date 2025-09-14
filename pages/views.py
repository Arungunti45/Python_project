from django.shortcuts import render,get_object_or_404,redirect
from .models import Product, Category,Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url="login")
def home(request):
    return render(request, "pages/home.html")

# @login_required
def about_view(request):
    return render(request, 'pages/about.html')

# @login_required
def contact_view(request):
    return render(request, 'pages/contact.html')

# @login_required
def product_list(request):
    category_param = request.GET.get('category')
    query = request.GET.get('q')

    products = Product.objects.all()
    categories = Category.objects.all()

    # Filter by category (ID or name)
    if category_param:
        if category_param.isdigit():
            products = products.filter(category_id=category_param)
        else:
            products = products.filter(category__name=category_param)

    # Filter by search query
    if query:
        products = products.filter(name__icontains=query)

    return render(request, 'pages/product_list.html', {
        'products': products,
        'categories': categories,
    })


def checkout_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        # Save delivery address (for now, just dummy order)
        order = Order.objects.create(
            product=product,
            user=request.user,
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            pincode=request.POST.get("pincode"),
            payment_method="COD"  # fixed payment method
        )
        return redirect('payment', order.id)

    return render(request, 'pages/checkout.html', {"product": product})

# def payment_view(request, order_id):

def payment_type_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        order.payment_method = request.POST.get("payment_method")
        order.save()
        return redirect('payment', order.id)  # go to payment page
    return render(request, 'pages/payment_type.html', {"order": order})


def payment_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    return render(request, 'pages/direct_payment.html', {"order": order})

def confirm_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.is_paid = True
    order.save()
    return render(request, 'pages/payment_success.html', {"order": order})


