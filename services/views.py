from django.shortcuts import render, get_object_or_404

from .models import Produit, Terms, Profil


def index(request):
    context = {}
    context["produits"] = Produit.objects.order_by("name")
    context["profils"] = Profil.objects.order_by("slug")
    return render(request, 'index.html', context=context)


def get_page_produit(request, slug):
    context = {}
    context["produit"] = Produit.objects.get(slug=slug)
    context["produits"] = Produit.objects.order_by("name")
    return render(request, 'product.html', context=context)


def terms_of_use(request):
    context = {}
    context["content"] = Terms.objects.get()
    context["produits"] = Produit.objects.order_by("name")
    return render(request, 'condition_of_use.html', context=context)