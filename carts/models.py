from django.db import models
from users.models import User
from goods.models import Products




class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(i.products_price() for i in self)  
    def total_quantity(self):
        if self:
            return sum(i.quantity() for i in self)  
        return 0 

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,blank=True, null=True, verbose_name="Користувач")
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveSmallIntegerField(default=0 ,verbose_name="Кількість")
    session_key = models.CharField(max_length=32, null=True, blank=True)
    time_of_creation = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")

    class Meta:
        db_table = 'cart'
        verbose_name = 'Кошик'
        verbose_name_plural = 'Кошик'

    objects = CartQueryset().as_manager()
    def products_price(self):
        return round(self.product.discount_price() * self.quantity, 2)


    def __str__(self):
        return f"Кошик {self.user.username} | Товар {self.product} | Кількість {self.quantity}"
    