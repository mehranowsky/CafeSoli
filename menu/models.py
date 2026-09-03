from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته")
    icon = models.CharField(max_length=10, blank=True, verbose_name="آیکون (ایموجی)")
    image = models.ImageField(upload_to='category_images/', blank=True, null=True, verbose_name="تصویر پس‌زمینه")

    class Meta:
        verbose_name = "دسته"
        verbose_name_plural = "دسته‌ها"
        ordering = ['name']

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="دسته"
    )
    name = models.CharField(max_length=200, verbose_name="نام آیتم")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        verbose_name="قیمت (تومان)",
        help_text="قیمت را به عدد وارد کنید، مثلاً 45000"
    )
    tags = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="برچسب‌ها",
        help_text="با کاما جدا کنید، مثلاً: محبوب, بدون گلوتن"
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "آیتم منو"
        verbose_name_plural = "آیتم‌های منو"
        ordering = ['category', 'name']

    def __str__(self):
        return self.name

    def price_formatted(self):
        return f"{self.price:,} تومان"