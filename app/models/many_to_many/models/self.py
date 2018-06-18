from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    # 관계가 대칭적으로 형성됨
    friends = models.ManyToManyField(
        'self',
    )

    def __str__(self):
        return self.name

    def show_friends(self):
        print('{}의 친구목록'.format(self.name))
        for friend in self.friends.all():
            print('-{}'.format(friend))

        print('총 {}명'.format(len(self.friends.all())))
