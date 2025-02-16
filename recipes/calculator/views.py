from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def index(request):
    return render(request, 'calculator/index.html', {'recipes': DATA.keys()})

def recipe_view(request, dish_name):
    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
    except ValueError:
        servings = 1

    recipe = DATA.get(dish_name, {}).copy()
    if recipe:
        for ingredient in recipe:
            recipe[ingredient] *= servings
        context = {'recipe': recipe}
        return render(request, 'calculator/recipe.html', context)
    else:
        return render(request, 'calculator/recipe_not_found.html')