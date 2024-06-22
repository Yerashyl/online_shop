from django.contrib import admin

from My_Online_shop.models import Product, Order, Category, Customer

# Register your models here.
admin.site.site_header = 'MyOnlineShop'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'stock')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total_price', 'customer_name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)