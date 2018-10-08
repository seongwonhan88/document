from django.db import models


# Create your models here.

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'small'),
        ('M', 'medium'),
        ('L', 'large')
    )
    name = models.CharField('이름',max_length=60)
    shirt_size = models.CharField('셔츠 사이즈',max_length=1, choices=SHIRT_SIZES, help_text='sml 중 선택')
    age = models.IntegerField('나이',blank=True, null=True)
    starts = models.IntegerField('좋아요',default=0)
    nickname = models.CharField(
        '별명',
        max_length=50,
        unique=True,
        blank = True,
        null = True,
    )