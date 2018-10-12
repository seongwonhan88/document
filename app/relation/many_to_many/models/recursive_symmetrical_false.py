from django.db import models

__all__ = (
    'InstagramUser',
)


class InstagramUser(models.Model):
    # following : following list
    # followers : my followers

    # individual
    # follower : a follow b
    # followee : b is a's followee

    name = models.CharField(max_length=50)

    # 내가 follow 를 한 유저 목록
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',  # 거꾸로 올때 어떻게 표현할 것인가
    )

    def __str__(self):
        return self.name
