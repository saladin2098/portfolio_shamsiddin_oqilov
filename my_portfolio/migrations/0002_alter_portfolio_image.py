# Generated by Django 4.1 on 2022-08-06 18:06

import account.validators
import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(help_text='Required', upload_to='images/portfolio_images', validators=[blog.validators.valid_images, account.validators.valid_file_size]),
        ),
    ]
