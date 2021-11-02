from django.db import models
from PIL import Image


class Product(models.Model):
    SMARTPHONE = 'smartphone'
    LAPTOP = 'laptop'
    PC = 'pc'
    ACC = 'accessories'

    CHOICE_GROUP = {
        (SMARTPHONE, 'smartphone'),
        (LAPTOP, 'laptop'),
        (PC, 'pc'),
        (ACC, 'accessories'),
    }

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    availability = models.BooleanField(default=True)
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=SMARTPHONE)
    img = models.ImageField(default='no_image.jpg', upload_to='product_image')

    def __str__(self):
        return f'{self.name}'
