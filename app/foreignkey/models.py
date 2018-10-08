from django.db import models


# Create your models here.
class Car(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer', #문자열로 만들면 나중에 생성되더라도 오류나지 않음. 장고에서 지원
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FCUser(models.Model):
    name = models.CharField(max_length=30)
    instrucutor = models.ForeignKey(
        'self',
        blank = True,
        null = True,
        on_delete=models.SET_NULL, #해당 키가 삭제되면 자동으로 null처리
        related_name='students',

    )

    def __str__(self):
        return self.name