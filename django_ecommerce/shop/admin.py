from django.contrib import admin
from .models import Product, Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "available", "created_at")
    list_filter = ("available", "created_at")
    search_fields = ("name", "description")


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "paid", "created_at")
    list_filter = ("paid", "created_at")
    search_fields = ("full_name", "email")
    inlines = [OrderItemInline]