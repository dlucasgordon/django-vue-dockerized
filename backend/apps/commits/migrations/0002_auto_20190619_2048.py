# Generated by Django 2.1.1 on 2019-06-19 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitbucketcommit',
            name='date',
            field=models.DateTimeField(verbose_name='Timestamp'),
        ),
        migrations.AlterField(
            model_name='githubcommit',
            name='date',
            field=models.DateTimeField(verbose_name='Timestamp'),
        ),
    ]
