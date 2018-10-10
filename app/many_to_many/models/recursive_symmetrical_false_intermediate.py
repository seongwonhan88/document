from django.db import models


__all__ = (
    'TwitterUser',
    'Relation',
)

class TwitterUser(models.Model):
    """
    특정 유저가 다른 유저를 (인스턴스 메서드)
        follow (팔로우하기)
        block (차단하기)

    중간모델이 저장하는 정보
        from_user
            어떤 유저가 '만든' 관계인지
        to_user
            관계의 '대상'이 되는 유저
        relation_type
            follow 또는  block (팔로우 또는 차단)

    용어정리
    - 다른사람이 자신을 follow하는 사람 목록
        followers
        팔로워 목록
    - 자신이 다른사람을 follow 한 사람 목록
        following
        팔로우 목록
    - 자신을 block 하는 다른사람 목록

    - 자신이 다른 사람을 block 한 목록
        block_list
    """
    name = models.CharField(max_length=50)
    relation_users = models.ManyToManyField(
        'self',
        through='Relation',
        symmetrical=False
    )

    def __str__(self):
        return self.name


class Relation(models.Model):
    CHOICE_RELATION_TYPE=(
        ('f', 'Follow'),
        ('b', 'Block'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_from_user',
    )

    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relation_set'
    )
    relation_type = models.CharField(
        choices=CHOICE_RELATION_TYPE,
        max_length=1,
    )
    created_at = models.DateTimeField(auto_now_add=True)