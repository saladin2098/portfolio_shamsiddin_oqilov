# Generated by Django 4.1 on 2022-08-26 06:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_remove_like_post_remove_like_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='disliked_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='liked_users',
            field=models.ManyToManyField(blank=True, related_name='liked_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='viewers',
            field=models.ManyToManyField(blank=True, related_name='viewers', to=settings.AUTH_USER_MODEL),
        ),
    ]