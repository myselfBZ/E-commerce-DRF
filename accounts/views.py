from rest_framework.decorators import api_view
from rest_framework.response import Response 
from ecommerce.models import Cart, CustomUser
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token 
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny

@api_view(["POST"])
@permission_classes([AllowAny])
def sign_up(request):
    sreialized = UserSerializer(data=request.data)
    if sreialized.is_valid():
        sreialized.save()
        user = User.objects.get(username=request.data['username'])
        
        token = Token.objects.create(user=user)
        user.set_password(request.data['password'])
        user.save()
        customuser = CustomUser.objects.create(user=user)
        print(customuser)
        cart = Cart.objects.create(user=customuser)
        return Response({"user":sreialized.data, "token":token.key})
    
    return Response({"message":sreialized.errors})


