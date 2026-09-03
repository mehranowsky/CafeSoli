from django.shortcuts import render, get_object_or_404
from .models import Category

def menu_view(request):
    categories = Category.objects.all()
    selected_category = None
    items = []

    category_id = request.GET.get('category')
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        items = selected_category.items.all()
        for item in items:
            item.tag_list = [tag.strip() for tag in item.tags.split(',') if tag.strip()]

    context = {
        'categories': categories,
        'selected_category': selected_category,
        'items': items,
    }
    return render(request, 'menu/menu.html', context)