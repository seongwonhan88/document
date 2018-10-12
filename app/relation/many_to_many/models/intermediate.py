from django.db import models

__all__ = (
    'Person',
    'Group',
    'Membership',
)


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        # 기본형태: 클래스명의 소문자화_set
        related_name='group_set',
        # 기본형태: 클래스명의 소문자화
        # MTM연결된 다른(target) 테이블 속성에서 검색하고자 할 때
        # .filter(키=값)
        #   에서 '키'에 다른 특정 '테이블'을 가리키고 싶을때
        #   MTM필드를 정의한 테이블의 경우에는 해당 필드명을 사용(Membership의 경우는 members)
        #   MTM필드의 target테이블의 경우에는 필드가 정의되어 있지 않고,
        #     이 때 사용하는 이름이 'related_query_name'속성에 할당된 이름
        related_query_name='group',
  )


    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
