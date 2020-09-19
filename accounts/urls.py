from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('',views.test,name='home')
	# path('login/', views.loginPage, name="login"),  
	# path('logout/', views.logoutUser, name="logout"),    
    # path('checkout/', CheckoutView.as_view(), name='checkout'),
    # path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    # path('product/<slug>', ItemDetailView.as_view(), name='product'),
    # path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    # path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    # path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    # path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    # path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    # path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
]