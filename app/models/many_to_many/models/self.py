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
