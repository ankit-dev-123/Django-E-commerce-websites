from django.db import models
from django.utils.text import slugify

# Model for storing product categories and their basic information
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to="category/", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "1. Categories"

    # Automatically generate a slug from the category name on save
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Model for sub-categories (e.g., Men's, Women's) linked to a parent category
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = "2. Sub-Categories"
    # Generate a slug combined with the parent category name on save
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.category.name}-{self.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.name} > {self.name}"

# Model for product types (e.g., Slim Fit, Cotton) linked to a sub-category
class ProductType(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="product_types")
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = "3. Product Types"

    # Generate a slug combined with the sub-category name on save
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.sub_category.name}-{self.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sub_category.name} > {self.name}"

# Model for storing product brands
class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
# Main model for storing detailed product information
class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Logic to ensure a unique slug is generated for every product on save
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        original_slug = self.slug
        queryset = Product.objects.all()
        if self.pk:
            queryset = queryset.exclude(pk=self.pk)
        
        counter = 1
        # If the generated slug already exists, append a counter to keep it unique
        while queryset.filter(slug=self.slug).exists():
            self.slug = f"{original_slug}-{counter}"
            counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Model for storing multiple images associated with a single product
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/")
    
# Model for defining product color variations (e.g., Red, Blue)
class ColorVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="colors")
    color_name = models.CharField(max_length=50)
    
# Model for defining product size variations (e.g., S, M, L, XL)
class SizeVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sizes")
    size_name = models.CharField(max_length=20)