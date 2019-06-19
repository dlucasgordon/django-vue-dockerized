from django.db import models

class AbstractCommit(models.Model):
    sha =  models.CharField(verbose_name='Sha', max_length=40, primary_key=True)
    # node_id = models.CharField(verbose_name='Node ID', max_length=80)
    date = models.DateTimeField(verbose_name='Timestamp')
    author_username = models.CharField(verbose_name='Author Username', max_length=255)
    # author_email = models.EmailField(verbose_name='Email', max_length=255)
    message = models.TextField(verbose_name='Message')
    api_url = models.URLField(verbose_name='API URL')
    html_url = models.URLField(verbose_name='HTML URL')

    class Meta:
        abstract = True

class BitbucketCommit(AbstractCommit):
    pass

class GithubCommit(AbstractCommit):
    pass
