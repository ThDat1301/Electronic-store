import stripe
import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'electronic-store.settings'
application = get_wsgi_application()

from home_page.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY


def initProduct():
    products = Product.objects.all()
    for p in products:
        product = stripe.Product.create(
            name=p.name,
        )
        price = stripe.Price.create(
            product=product,
            unit_amount=int(p.price),
            currency='usd'
        )


if __name__ == '__main__':
    initProduct()

