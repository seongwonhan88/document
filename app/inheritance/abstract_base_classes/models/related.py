from django.db import models

__all__ = (
    'RelatedUser',
    'PostBase',
    'PhotoPost',
    'TextPost',
)


class RelatedUser(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostBase(models.Model):
    author = models.ForeignKey(
        RelatedUser,
        on_delete=models.CASCADE,
        # 유저(Person) 입장에서
        # 자신이 특정 post의 'author'인 경우
        #
        # 해당하는 모든 PostBase객체를 참조하는 역방향 매니저 이름
        # %(class) class 상속
        # %(app_label) app 상속
        related_name='%(app_label)s_%(class)s_set',
        related_query_name='%(app_label)s_%(class)s',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PhotoPost(PostBase):
    photo_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Post(author: {self.author.name})'


class TextPost(PostBase):
    text = models.TextField(blank=True)

    def __str__(self):
        return f'Post(author: {self.author.name})'
