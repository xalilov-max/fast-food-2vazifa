from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required , login_required
from .forms import FoodForm
from .models import Food, FoodType, Like, Comment
from django.http import JsonResponse
from .forms import CommentForm

def index(request):
    food_types = FoodType.objects.all()
    foods = Food.objects.all()
    return render(request, 'menu/index.html', {'food_types': food_types, 'foods': foods})

@login_required
def toggle_like(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    like, created = Like.objects.get_or_create(food=food, user=request.user)
    if not created:
        like.delete()
    return redirect('food_detail', food_id=food.id)

@login_required
def add_comment(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.food = food
            comment.user = request.user
            comment.save()
            return redirect('food_detail', food_id=food.id)
    else:
        form = CommentForm()
    return render(request, 'menu/add_comment.html', {'form': form, 'food': food})

# def food_detail(request, food_id):
#     food = get_object_or_404(Food, id=food_id)
#     food.view_count += 1
#     food.save()
#     liked = food.likes.filter(user=request.user).exists()
#     comments = food.comments.all()
#     return render(request, 'menu/food_detail.html', {
#         'food': food, 
#         'liked': liked,
#         'comments': comments,
#         'comment_form': CommentForm(),
#     })


def food_detail(request, id):
    food = get_object_or_404(Food, id=id)

    # Like qo'shish uchun
    if request.method == "POST" and request.user.is_authenticated:
        # Avval foydalanuvchi like bosganmi, tekshiramiz
        like, created = Like.objects.get_or_create(food=food, user=request.user)
        if not created:
            like.delete()  # Like mavjud bo'lsa, o'chiramiz
        return redirect('food_detail', id=food.id)

    return render(request, 'menu/food_detail.html', {'food': food})


def food_list(request):
    food_types = FoodType.objects.all()
    foods = Food.objects.all()
    return render(request, 'menu/food_list.html', {'food_types': food_types, 'foods': foods})


@permission_required('menu.add_food')
def food_create(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm()
    return render(request, 'menu/food_form.html', {'form': form})


@permission_required('menu.change_food')
def food_update(request, id):
    food = get_object_or_404(Food, id=id)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm(instance=food)
    return render(request, 'menu/food_form.html', {'form': form})


@permission_required('menu.delete_food')
def food_delete(request, id):
    food = get_object_or_404(Food, id=id)
    if request.method == 'POST':
        food.delete()
        return redirect('food_list')
    return render(request, 'menu/food_confirm_delete.html', {'food': food})
