from django.shortcuts import render
import requests
from rest_framework import viewsets

from apps.commits.models import BitbucketCommit, GithubCommit
from apps.commits.serializers import BitbucketCommitSerializer, GithubCommitSerializer

BITBUCKET_API_URI = 'https://api.bitbucket.org/2.0/repositories/biobakery/halla/commits'
GITHUB_API_URI    = 'https://api.github.com/repos/pytest-dev/pytest/commits'


class BitbucketCommitViewSet(viewsets.ModelViewSet):
    serializer_class = BitbucketCommitSerializer
    queryset = BitbucketCommit.objects.all().order_by('-date')

    def get_queryset(self):
        reload_commits = self.request.query_params.get('reload', None)
        commits = self.queryset
        if not len(commits) or reload_commits is not None:
            commits = self.get_commits_from_api()
        return commits
    
    def get_commits_from_api(self):
        json = requests.get(BITBUCKET_API_URI).json()
        commits = []
        for row in json['values']:
            sha = row['hash']
            date = row['date']
            author_username = row['author']['raw']
            message = row['message']
            api_url = row['links']['self']['href']
            html_url = row['links']['html']['href']
            commit = BitbucketCommit(sha, date, author_username, message, api_url, html_url)
            commits.append(commit)
        for commit in commits:
            commit.save()
        return commits
    

class GithubCommitViewSet(viewsets.ModelViewSet):
    serializer_class = GithubCommitSerializer
    queryset = GithubCommit.objects.all().order_by('-date')

    def get_queryset(self):
        reload_commits = self.request.query_params.get('reload', None)
        print(self.request.query_params)
        commits = self.queryset
        if not len(commits) or reload_commits is not None:
            commits = self.get_commits_from_api()
        return commits
    
    def get_commits_from_api(self):
        json = requests.get(GITHUB_API_URI).json()
        commits = []
        for row in json:
            sha = row['sha']
            date = row['commit']['author']['date']
            author_username = row['author']['login']
            message = row['commit']['message']
            api_url = row['url']
            html_url = row['html_url']
            commit = GithubCommit(sha, date, author_username, message, api_url, html_url)
            commits.append(commit)
        for commit in commits:
            commit.save()
        return commits