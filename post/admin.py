from django.contrib import admin

from .models import Tweet, Comment, CommentLikeDislike, TweetLikeDislike, User

admin.site.register(Tweet)
admin.site.register(Comment)
admin.site.register(CommentLikeDislike)
admin.site.register(TweetLikeDislike)
admin.site.register(User)