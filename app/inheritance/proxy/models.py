from django.db import models


class User1Manager(models.Manager):
    def normal_users(self):
        # 상위클래스에서 정의한 '기본적으로' 돌려줄 QuerySet
        return super().get_queryset().filter(is_admin=False)
        # return User1.objects.filter(is_admin=False)

    def admin_users(self):
        return super().get_queryset().filter(is_admin=True)
        # return User1.objects.filter(is_admin=True)


class User1(models.Model):
    # 가능한 행동(메서드)
    # - 유저 삭제

    name = models.CharField(max_length=50)
    is_admin = models.BooleanField('Admin', default=False)

    objects = User1Manager()

    def __str__(self):
        return self.name

    def find_user(self, name):
        return User1.objects.filter(name__contains=name)

    class Meta:
        db_table = 'Inheritance_Proxy_User1'


class NormalUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=False)


class AdminUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)


class NormalUser(User1):
    objects = NormalUserManager()

    class Meta:
        proxy = True


class Admin(User1):
    objects = AdminUserManager()

    class Meta:
        proxy = True

    def delete_user(self, user):
        user.delete()
