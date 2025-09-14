from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('products/', views.product_list, name='product_list'),
    path("checkout/<int:product_id>/", views.checkout_view, name="checkout"),
    path("payment-type/", views.payment_type_view, name="payment_type"),
    path("payment/<int:order_id>/", views.payment_view, name="payment"),
    path('confirm-payment/<int:order_id>/', views.confirm_payment, name='confirm_payment')

    # path('products/category/<int:category_id>/', views.product_list, name='product_list_by_category'),
]
