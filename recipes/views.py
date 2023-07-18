# from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from recipes.models import Recipe

# from utils.recipes.factory import make_recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes/pages/home.html', context)


def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #     category__id=category_id, is_published=True).order_by('-id')

    # if not recipes:
    #     raise Http404('Not found')

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id, is_published=True).order_by('-id')
    )

    category_name = recipes[0].category.name
    context = {
        'recipes': recipes,
        'category_name': f'Category: {category_name}',
    }
    return render(request, 'recipes/pages/category.html', context)


def recipe(request, id):
    recipe = get_object_or_404(
        Recipe,
        id=id, is_published=True
    )

    context = {
        'recipe': recipe,
        "is_detail_page": True,
    }

    return render(request, 'recipes/pages/recipe-view.html', context)
