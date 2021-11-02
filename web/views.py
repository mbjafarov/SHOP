from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from web.models import Product

@login_required
def index(request):
    return render(request, 'web/index.html')


def shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'web/shop.html', context)
