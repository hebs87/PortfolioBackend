# Generated by Django 3.1.7 on 2021-03-31 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_auto_20210331_2346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='date',
            new_name='date_from',
        ),
        migrations.AddField(
            model_name='education',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
    ]
