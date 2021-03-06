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
        # abstract_base_classes_photopost
        related_name='%(class)ss'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PhotoPost(PostBase):
    # related_name = PhotoPosts
    photo_url = models.CharField(max_length=500)


class TextPost(PostBase):
    # related_name = TextPost
    text = models.TextField()
