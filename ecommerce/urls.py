from django.urls import path
from . import views 

urlpatterns = [
    
    path('products', views.ProductListAPIView.as_view()),
    path('products', views.ProductCreateAPIView.as_view()),
    path('products/<int:pk>', views.ProductUpdateAPIVIew.as_view()),
    path('products/<int:pk>', views.ProductDeleteAPIView.as_view()),
    path('products/like/<int:pk>', views.LikeView.as_view()),
    path('products/<int:pk>', views.ProductDetailAPIView.as_view()),
    path('products/comment/<int:pk>', views.CommentCreateAPIView.as_view()),
    path('products/most-liked', views.Get10MostLiked.as_view()),
    path('cart/<int:pk>', views.CartAPIView.as_view()),
    path('your-liked-products', views.getYourLikedProducts),
    path('cart-items', views.see_products_in_cart),
    path('orders/<int:pk>', views.order_product),
    path("orders", views.orders)
]