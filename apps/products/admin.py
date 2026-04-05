from django.contrib import admin
# Import necessary models for admin registration
from .models import (
    Category, 
    SubCategory, 
    ProductType, 
    Brand, 
    Product, 
    ProductImage, 
    ColorVariant, 
    SizeVariant
)

# Inline configuration to add multiple images directly on the Product page
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

# Inline configuration to add color variants directly on the Product page
class ColorVariantInline(admin.TabularInline):
    model = ColorVariant
    extra = 1

# Inline configuration to add size variants directly on the Product page
class SizeVariantInline(admin.TabularInline):
    model = SizeVariant
    extra = 1

# Admin configuration for the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'is_active']
    prepopulated_fields = {'slug': ('name',)} # Automatically fill slug from the name field

# Admin configuration for the SubCategory model
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'slug']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('name',)} # Automatically fill slug from the name field

# Admin configuration for the ProductType model
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sub_category', 'slug']
    list_filter = ['sub_category']
    prepopulated_fields = {'slug': ('name',)} # Automatically fill slug from the name field

# Admin configuration for the Brand model
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

# Main Product admin with filters, search, and nested inlines for images/variants
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'product_type', 'slug','brand', 'price', 'stock', 'is_available']
    list_filter = ['is_available', 'brand', 'product_type']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)} # Automatically fill slug from the name field
    
    inlines = [
        ProductImageInline,
        ColorVariantInline,
        SizeVariantInline
    ]

# Standalone registration for ProductImage
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']

# Standalone registration for ColorVariant
@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'color_name']

# Standalone registration for SizeVariant
@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'size_name']