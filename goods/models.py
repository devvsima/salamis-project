from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Назва")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "категорію"
        verbose_name_plural = "Категорії"


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Назва")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Фотографія"
    )
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Ціна"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Знижка в відсотках"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кільікість")
    categorie = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name="Категорія")


    class Meta:
        db_table = "product"
        verbose_name = "товар"
        verbose_name_plural = "товари"
