from django.db import models
from django.utils import timezone

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

    @property
    def followers(self):
        """
        :return: 나를 follow하는 다른 TwitterUser QuerySet
        """

        return TwitterUser.objects.filter(
            from_user_relations__to_user=self,
            from_user_relations__relation_type='f',
        )

    @property
    def following(self):
        """
        :return: 내가 follow하는 다른 TwitterUser QuerySet
        """
        return TwitterUser.objects.filter(
            to_user_relations__from_user=self,
            to_user_relations__relation_type='f'
        )

    @property
    def block_list(self):
        """
        :return: 내가 block하는 다른 TwitterUser QuerySet
        """
        return TwitterUser.objects.filter(
            to_user_relations__from_user=self,
            to_user_relations__relation_type='b',
        )

    def follow(self, user):
        """
        user를 follow하는 Relation을 생성
            1. 이미 존재한다면 만들지 않는다
            2. user가 block_list에 속한다면 만들지 않는다
        :param user: TwitterUser
        :return: tuple(Relation instance,
        """
        if not self.from_user_relations.filter(to_user=user).exists():
            self.from_user_relations.create(to_user=user, relation_type='f')
        return self.from_user_relations.get(to_user=user)

    def block(self, user):
        """
        user를 block하는 Relation을 생성
            1. 이미 존재한다면 만들지 않는다
            2. user가 following에 속한다면 해제시키고 만든다
        :param user: TwitterUser
        :return: tuple(Relation instance,
        """
        try:
            relation = self.from_user_relations.get(to_user=user)
            if relation.relation_type == 'f':
                relation.relation_type = 'b'
                relation.created_at= timezone.now()
                relation.save()

        except Relation.DoesNotExist:
            relation= self.from_user_relations.create(to_user=user, relation_type='b')

        return relation

    @property
    def follower_relations(self):
        """
         :return: 나를 follow하는 Relation QuerySet
        """
        return

    @property
    def followee_relations(self):
        """
         :return: 내가 follow하는 Relation QuerySet
        """
        return


class Relation(models.Model):
    CHOICE_RELATION_TYPE = (
        ('f', 'Follow'),
        ('b', 'Block'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='from_user_relations',
        # 만약에 related_name이 지정 되어 있을 경우, related_query_name의 기본값은 related_name과 같음
        related_query_name='from_user_relations'
    )

    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='to_user_relations',
        related_query_name='to_user_relations'
    )
    relation_type = models.CharField(
        choices=CHOICE_RELATION_TYPE,
        max_length=1,
    )
    created_at = models.DateTimeField(auto_now_add=True)
