from django.db import models

__all__ = (
    'TwitterUser',
    'Relation',
)


class TwitterUser(models.Model):
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
    )

    def __str__(self):
        return self.name

    @property
    def following_relations(self):
        return self.relations_by_from_user.filter(relation_type='f')

    @property
    def follower_relations(self):
        return self.relations_by_to_user.filter(relation_type='f')

    @property
    def block_relations(self):
        return self.relations_by_from_user.filter(relation_type='b')


class Relation(models.Model):
    CHOICES_RELATION_TYPE = (
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
        related_name='relations_by_to_user',
    )
    # 입력 값을 제한하는 choices 옵션 추
    relation_type = models.CharField(
        max_length=1,
        choices=CHOICES_RELATION_TYPE,
    )
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'from({}), to({}), {}'.format(
            self.from_user.name,
            self.to_user.name,
            self.get_relation_type_display(),
        )

