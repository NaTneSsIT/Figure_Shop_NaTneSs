from django.urls import path
from . import views

urlpatterns=[
    path('shop/',views.store,name="store"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/',views.updateItem,name="update_item"),
    path('shop/prodDetail/<int:id>',views.prodDetail,name="prodDetail"),
    path('',views.default,name="default"),
]