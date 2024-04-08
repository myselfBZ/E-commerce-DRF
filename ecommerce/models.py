from django.db import models
from django.contrib.auth.models import User 



class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    liked = models.BooleanField()
    

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2,max_digits=7)
    number = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def like_number(self):
        return self.like_set.count()
    
    def available(self):
        if self.number == 0:
            return False
        return True
    
    def __str__(self) -> str:
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)


class Comment(models.Model):
    comment = models.TextField(max_length=511)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)


class Order(models.Model):
    product = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    