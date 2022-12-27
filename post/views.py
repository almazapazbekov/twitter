from django.shortcuts import render
from rest_framework import viewsets, authentication, permissions, views
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from .models import Tweet, Comment, CommentLikeDislike, TweetLikeDislike
from .serializers import CommentSerializer, TweetSerializer
from .permissions import Permission


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    authentication_classes = [authentication.TokenAuthentication, SessionAuthentication]
    permission_classes = [Permission, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [authentication.TokenAuthentication, SessionAuthentication]
    permission_classes = [Permission, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikeTweetAPIView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication, SessionAuthentication]
    permission_classes = [Permission, ]

    def post(self, request, *args, **kwargs):
        tweet_id = kwargs.get('tweet_id')
        author = request.user
        dislike = kwargs.get('dislike')
        new_like_dislike_tweet = TweetLikeDislike(
            tweet_id=tweet_id,
            author=author,
            is_dislike=dislike
        )
        new_like_dislike_tweet.save()
        return Response(status=200)


class LikeCommentAPIView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication, SessionAuthentication]
    permission_classes = [Permission, ]

    def post(self, request, *args, **kwargs):
        comment_id = kwargs.get('comment_id')
        author = request.user
        dislike = kwargs.get('dislike')
        new_like_dislike_comment = CommentLikeDislike(
            comment_id=comment_id,
            author=author,
            is_dislike=dislike
        )
        new_like_dislike_comment.save()
        return Response(status=200)
