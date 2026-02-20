from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product, Highlight

def home(request):
    # On récupère les vidéos de pub pour l'accueil
    highlights = Highlight.objects.all().order_by('-created_at')[:3]
    return render(request, 'index.html', {'highlights': highlights})

def boutique(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'boutique.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail.html', {'product': product})