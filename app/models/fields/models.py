from django.db import models


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField( max_length=60)
    shirt_size = models.CharField('셔츠사이즈', help_text='s는 작습니다', max_length=1, choices=SHIRT_SIZES)
