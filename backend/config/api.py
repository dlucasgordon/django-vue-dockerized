from rest_framework import routers
from apps.users.views import UserViewSet
from apps.commits.views import BitbucketCommitViewSet, GithubCommitViewSet

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'users', UserViewSet)

# Commits API
api.register(r'commits/bitbucket', BitbucketCommitViewSet)
api.register(r'commits/github',    GithubCommitViewSet)
