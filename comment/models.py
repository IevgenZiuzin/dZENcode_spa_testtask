from django.core.exceptions import ValidationError
from django.db import models
from user.models import AppUser, GuestUser


class Comment(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True, blank=True)
    guest = models.ForeignKey(GuestUser, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='answers', null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    rate = models.SmallIntegerField(default=0)
    rated_users = models.ManyToManyField(AppUser, related_name='rated_comments')

    def __str__(self):
        return f'{self.content[:20]}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Attachment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    file = models.FileField()
    type = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.file}'

    class Meta:
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'
