from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField(
        'self',
    )

    def __str__(self):

        friend_list = self.friends.all()
        friend_list_str = ', '.join([friend.name for friend in friend_list])
        return f'{self.name} (friend: {friend_list_str})'
