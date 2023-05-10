from django.contrib import admin
from .models import Comment, Attachment


class CommentsInline(admin.TabularInline):
    model = Comment


class AttachmentInline(admin.TabularInline):
    model = Attachment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'datetime', '__str__')
    inlines = (CommentsInline, AttachmentInline)


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'file', 'type')
