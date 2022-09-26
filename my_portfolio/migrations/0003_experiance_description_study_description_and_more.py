# Generated by Django 4.1 on 2022-08-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0002_alter_portfolio_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiance',
            name='description',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='study',
            name='description',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='degree',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]