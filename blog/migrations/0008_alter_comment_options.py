# Generated by Django 4.1 on 2022-09-26 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_disliked_users_alter_post_liked_users_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-writed_at'], 'verbose_name_plural': 'Comments'},
        ),
    ]