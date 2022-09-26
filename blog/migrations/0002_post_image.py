# Generated by Django 4.1 on 2022-08-06 18:06

import account.validators
import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='images/posts/', validators=[account.validators.valid_file_size, blog.validators.valid_images]),
        ),
    ]
