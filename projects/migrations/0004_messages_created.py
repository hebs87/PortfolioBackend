# Generated by Django 3.1.7 on 2021-04-02 01:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]