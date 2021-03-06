# Generated by Django 2.1.1 on 2019-06-19 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BitbucketCommit',
            fields=[
                ('sha', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Sha')),
                ('date', models.DateField(verbose_name='Date')),
                ('author_username', models.CharField(max_length=255, verbose_name='Author Username')),
                ('message', models.TextField(verbose_name='Message')),
                ('api_url', models.URLField(verbose_name='API URL')),
                ('html_url', models.URLField(verbose_name='HTML URL')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GithubCommit',
            fields=[
                ('sha', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Sha')),
                ('date', models.DateField(verbose_name='Date')),
                ('author_username', models.CharField(max_length=255, verbose_name='Author Username')),
                ('message', models.TextField(verbose_name='Message')),
                ('api_url', models.URLField(verbose_name='API URL')),
                ('html_url', models.URLField(verbose_name='HTML URL')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
