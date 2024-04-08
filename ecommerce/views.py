from rest_framework import generics 
from .models import Like, Product, Order
from .serializers import LikeSerializer, ProductSerializer, CommnetSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from .models import Product, Like
from rest_framework.decorators import api_view
from django.http import HttpRequest
from django.contrib.auth.models import User

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer:ProductSerializer):
        serializer.save(owner=self.request.user)

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductUpdateAPIVIew(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    

class LikeView(APIView):
    
    def post(self, request, pk):
        data = request.data
        serializer = LikeSerializer(data=data)
        user = request.user
        product = Product.objects.get(id=pk)
        if serializer.is_valid():
            
            liked = serializer.validated_data['liked']
            if liked == True:
                if Like.objects.filter(user=user, product=product).exists():
                    return Response({"error": "User has already liked this product."})
                like = Like.objects.create(user=user, product=product, liked=liked)
                like_serialized = LikeSerializer(like)
                return Response({"like": like_serialized.data})
            like = Like.objects.get(user=user, product=product).delete()
            return Response({"message":"Unliked successfully"})
        
        return Response(serializer.errors)
    

class CommentCreateAPIView(APIView):
     
    
     def post(self, request, pk):
         user = request.user

         data = CommnetSerializer(data=request.data)
         if data.is_valid():
             product = Product.objects.get(id=pk)
             comment = data.save(product=product, user=user)
             comment = CommnetSerializer(comment)
             return Response({"comment":comment.data})
            

class Get10MostLiked(APIView):
    

    def get(self, request):
        most_liked_products = (
        Product.objects.annotate(num_likes=Count('like'))
        .order_by('-num_likes')[:10]
        )
        serializer = ProductSerializer(most_liked_products, many=True)
        return Response(serializer.data)
        
class CartAPIView(APIView):
    

    def post(self, request, pk):
        product = Product.objects.get(id=pk)
        user = request.user
        cart = user.customuser.cart
        if not product in cart.product.all():
            product.number -= 1
            cart.product.add(product)
            return Response({"message":f"Product {product.title} has been added"})
        return Response({"message":"Product is already in there"})    
    
    def delete(self, request, pk):
        user = request.user 
        product = Product.objects.get(pk=pk)
        if not product in user.customuser.cart.product.all():
            return Response({"message":"Product is not in the cart."})
        user.customuser.cart.product.remove(product)
        return Response({"message":f"{product.title} has been removed successfully"})

            

    
        
@api_view(["GET"])
def getYourLikedProducts(request:HttpRequest):
     user = request.user
     likes = user.like_set.all()
     products = []

     for like in likes:
         products.append(like.product)
    
     product_serializer = ProductSerializer(products, many=True)
     return Response(product_serializer.data)
    
@api_view(["GET"])
def see_products_in_cart(request):
    user = request.user
    products = user.customuser.cart.product.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)  

@api_view(["POST", "GET"])
def order_product(request: HttpRequest, pk:int):
    user:User = request.user
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        review = request.data.get("review", "")
        if not product in user.customuser.cart.product.all():
            return Response({"message": "You need to add this product to the cart first"})
        order = Order.objects.create(user=user, review=review)
        order.product.add(product)
        order.save()
        user.customuser.cart.product.remove(product)
        return Response({"message": f"Your order for {product.title} is on its way"})

@api_view(["GET"])
def orders(request):
    user = request.user
    orders = user.order_set.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)