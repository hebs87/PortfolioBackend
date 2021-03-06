# Generated by Django 3.1.7 on 2021-04-02 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_auto_20210331_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetails',
            name='facebook_url',
            field=models.URLField(default='https://www.facebook.com/hebs87'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='github_url',
            field=models.URLField(default='https://github.com/hebs87'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='instagram_url',
            field=models.URLField(default='https://www.instagram.com/hebs87/'),
            preserve_default=False,
        ),
    ]
