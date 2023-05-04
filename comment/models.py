from django.db import models
from user.models import AppUser


class Comment(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    rate = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.content[:10]}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Attachment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    file = models.FileField()
    type = models.CharField()

    def __str__(self):
        return f'{self.file}'

    class Meta:
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'
