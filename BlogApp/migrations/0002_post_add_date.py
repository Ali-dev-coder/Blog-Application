# Generated by Django 3.2.5 on 2021-12-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]