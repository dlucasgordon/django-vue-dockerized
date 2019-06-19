from rest_framework import serializers

from apps.commits.models import BitbucketCommit, GithubCommit

class AbstractCommitSerializer(serializers.ModelSerializer):
    pass

class BitbucketCommitSerializer(AbstractCommitSerializer):
    class Meta:
        model = BitbucketCommit
        fields = '__all__'

class GithubCommitSerializer(AbstractCommitSerializer):
    class Meta:
        model = GithubCommit
        fields = '__all__'
