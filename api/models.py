from django.contrib.auth.models import AbstractUser
from django.db import models
from mptt import models as mptt_models
from ckeditor.fields import RichTextField

GENDER = (
    ('male', 'MALE'),
    ('female', 'Female')
)

DISTRICT = (
    (1, 'Алмазарский район'),
    (2, 'Бектемирский район'),
    (3, 'Мирабадский район'),
    (4, 'Мирзо-Улугбекский район'),
    (5, 'Сергелийский район'),
    (6, 'Учтепинский район'),
    (7, 'Чиланзарский район'),
    (8, 'Шайхантахурский район'),
    (9, 'Юнусабадский район'),
    (10, 'Яккасарайский район'),
    (11, 'Яшнабадский район'),
)


class Customer(AbstractUser):
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER, max_length=10)
    birth_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Customer'

    def __str__(self):
        return f'{self.first_name}' + '\t' + f'{self.last_name}' + '\t' + f'{self.username}'


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    district = models.CharField(choices=DISTRICT, max_length=100)
    waymark = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.customer.get_full_name)


class Category(mptt_models.MPTTModel):
    name = models.CharField(max_length=255, unique=False)
    slug = models.SlugField(max_length=255)
    parent = mptt_models.TreeForeignKey('self',
                                        on_delete=models.CASCADE,
                                        null=True,
                                        blank=True,
                                        related_name='children')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='product/%Y/%m/', blank=True, null=True)
    category = mptt_models.TreeForeignKey('Category', null=True, blank=True, on_delete=models.ForeignKey)
    description = RichTextField()
    rating = models.PositiveSmallIntegerField(default=0)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    slug = models.SlugField(max_length=255)
    is_sale = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        db_table = 'products'

    def __str__(self):
        return self.name


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_gallery')

    def __str__(self):
        return str(self.product.name)


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='carts')
    total = models.DecimalField(null=True, default=0, max_digits=16, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    ordered_at = models.DateTimeField(null=True, blank=True)
    items = models.ManyToManyField(Product)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.customer.username)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.cart.customer.username)


class Banner(models.Model):
    image = models.ImageField(upload_to='banner/')

    def __str__(self):
        return str(self.image)
