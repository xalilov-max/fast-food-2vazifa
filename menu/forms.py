from django import forms
from .models import Food
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Izohingizni kiriting',
        }

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_type', 'nomi', 'tarkibi', 'narxi']
        labels = {
            'food_type': 'Taom turi',
            'nomi': 'Taom nomi',
            'tarkibi': 'Tarkibi',
            'narxi': 'Narxi',
        }
