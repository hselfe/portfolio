# Generated by Django 2.1 on 2018-10-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='fulltext',
            field=models.TextField(default='Text goes here'),
            preserve_default=False,
        ),
    ]
