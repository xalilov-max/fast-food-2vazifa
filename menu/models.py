from django.db import models
from django.contrib.auth.models import User


class FoodType(models.Model):
    nomi = models.CharField(max_length=50, verbose_name="Nomi")

    def __str__(self):
        return self.nomi

class Food(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, related_name='foods', verbose_name="Taom turi")
    nomi = models.CharField(max_length=100, verbose_name="Nomi")
    tarkibi = models.TextField(verbose_name="Tarkibi")
    narxi = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    view_count = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")

    def __str__(self):
        return self.nomi
        
class Like(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('food', 'user')

class Comment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Izoh")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:20]}"


