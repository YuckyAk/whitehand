from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Size (models.Model):
    heigh = models.IntegerField()
    width = models.IntegerField()

    def __str__(self):
        return f"id: {self.id}, Ширина: {self.width}, Высота: {self.heigh}"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images')
    manufacturer = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"


class Feedback(models.Model):
    name=models.CharField(max_length=100, verbose_name='Имя')
    masage=models.TextField(verbose_name='Сообщение')
    number=models.DecimalField(max_digits=12, decimal_places=0)

    def __str__(self):
        return self.name
