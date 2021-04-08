import uuid

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils.timezone import now as datetime_now

fs = FileSystemStorage(location=settings.MEDIA_ROOT)


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=False, verbose_name="Nome")

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return f"{self.name} - {str(self.id)}"


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    price = models.FloatField(verbose_name="Preço")
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE, verbose_name="Marca")
    image = models.ImageField(verbose_name="Imagem", storage=fs)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f"{self.name} - {self.brand.name}"


class Sell(models.Model):
    STATUS_CHOICES = [
        ("cart", "cart"),
        ("sold", "sold"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(default=datetime_now, verbose_name="Data")
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], unique=False,
                              verbose_name="Status")

    def get_total_price(self):
        price = 0
        for product_exit in ProductExit.objects.filter(sell=self.id):
            price += product_exit.product.price * product_exit.quantity
        return price

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"

    def __str__(self):
        return f"{self.date} - {self.id}"


class ProductExit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="Produto")
    quantity = models.IntegerField(verbose_name="Quantidade")
    sell = models.ForeignKey(to=Sell, on_delete=models.CASCADE, verbose_name="Venda")

    class Meta:
        verbose_name = "Item de Venda"
        verbose_name_plural = "Itens de Venda"

    def __str__(self):
        return f"{self.sell.date} - {self.product.name}:{self.quantity} - {self.product.brand.name}"


class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="Produto")
    quantity = models.IntegerField(verbose_name="Quantidade")

    class Meta:
        verbose_name = "Entrada de Produto"
        verbose_name_plural = "Entradas de Produtos"

    def __str__(self):
        return f"{self.product.name}:{self.quantity} - {self.product.brand.name}"
