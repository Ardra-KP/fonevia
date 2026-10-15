from django.shortcuts import render
from phones.models import Phone, Brand
from shops.models import Shop
from repairs.models import Repair

def home(request):
    shops = Shop.objects.filter(is_verified=True) if hasattr(Shop, 'is_verified') else Shop.objects.all()
    brands = Brand.objects.all().order_by('name')
    # Brand illa enkil default list
    if not brands.exists():
        brands = []
    return render(request, 'core/home.html', {
        'brands': brands,
        'shops': shops,
        'total_shops': shops.count() if hasattr(shops, 'count') else len(shops),
    })

def dashboard(request):
    return render(request, 'core/dashboard.html', {
        'total_repairs': 12,
        'pending_repairs': 2,
        'shops': Shop.objects.all()[:6],
        'repairs': Repair.objects.all()[:10] if hasattr(Repair, 'objects') else [],
        'total_earning': 4200,
        'phones': Phone.objects.all(),
    })