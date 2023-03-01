from home_page.models import Category


def get_category(request):
    categories = Category.objects.all()
    data = {
        'categories': categories,
    }
    return data
