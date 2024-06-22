from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.db.models import Q

from My_Online_shop.models import Product, Category


# Create your views here.
class AllProducts(View):
    def get(self, request):
        params = request.GET
        all_products = Product.objects.all()
        if params.get('search'):
            all_products = Product.objects.filter(Q(name__icontains=params['search'])|Q(description__icontains=params['search']))
        response = [
            {
                'name': product.name,
                'description':product.description,
                'price': product.price,
                'stock': product.stock,
            }for product in all_products
        ]
        return JsonResponse(data = {"response" : response})

class ProductView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        response = {'name': product.name,
                    'description': product.description,
                    'price': product.price,
                    'stock': product.stock}

        return JsonResponse(data = response)

class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = [{'name': category.name,
                     'description': category.description} for category in categories]
        return JsonResponse(data = {'response': response})

class ProductsOfCategory(View):
    def get(self, request, id):
        params = request.GET
        products = Product.objects.filter(category_id=id)
        filter = params.get('filter')
        if filter:
            if filter == 'below_100':
                products = products.filter(price__lte=100)
            elif filter == 'above_300':
                products = products.filter(price__gte=300)
        response = [
            {
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'stock': product.stock,
            } for product in products
        ]
        return JsonResponse(data = {'response': response})