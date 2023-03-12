from django.db.models import Min, Max
from home_page.models import Category, Product, Color
from django.http import JsonResponse

def get_category(request):
    categories = Category.objects.all()
    colors = Color.objects.all();
    maxminPrice = Product.objects.aggregate(Min('price'), Max('price'))
    data = {
        'categories': categories,
        'minmaxPrice': maxminPrice,
        'colors': colors
    }
    return data


    return data


def add_To_Cart(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    cart = request.session['cart']
    id = request.POST.get('id')
    name = request.POST.get('name')
    price = request.POST.get('price')
    image = request.POST.get('image')
    quantity = request.POST.get('quantity')
    if id in cart:
        cart[id]['quantity'] = int(cart[id]['quantity']) + 1
    else:
        cart[id] = {
            'id': id,
            'name': name,
            'price': price,
            'image': image,
            'quantity': quantity
        }
    request.session['cart'] = cart
    cartInfo = request.session['cart']
    # html = render_to_string('cart.html', {'cart': cartInfo})
    # return HttpResponse('cart.html', {'cart': cartInfo})
    return JsonResponse({'cart': request.session['cart'], 'totalitems':len(request.session['cart'])})