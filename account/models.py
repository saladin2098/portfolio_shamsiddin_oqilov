from this import d
from django.db import models

from .validators import valid_file_size, valid_file_type_cv

class OwnerInfo(models.Model):
    first_name = models.CharField(max_length=30, help_text="mustn't be empty")
    last_name = models.CharField(max_length=30, blank=True, null=True)
    age = models.PositiveBigIntegerField(blank=True, null=True)
    specialize = models.CharField(max_length=80, help_text="mustn't be empty")
    description = models.TextField(max_length=250, help_text="mustn't be empty")
    country = models.CharField(max_length=60, help_text="mustn't be empty")
    city = models.CharField(max_length=60, help_text="mustn't be empty")
    lives_in = models.CharField(max_length=120, help_text="mustn't be empty")
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female')
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    image = models.ImageField(upload_to='images/owner_profile', blank=True, null=True)
    cv = models.FileField(upload_to='owner_cv', validators=[valid_file_type_cv, valid_file_size],\
        blank=True, null=True, help_text="Available file types: (.pdf, .doc, .docx) \n\
        max file size: 1.5 mb")
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.first_name


class OwnerSkill(models.Model):
    type = models.CharField(max_length=25, help_text='example: coding, soft')
    title = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created_at']
    
    def __str__(self) -> str:
        return self.title


class SocialLink(models.Model):
    class Meta:
        ordering = ['-created_at']

    name = models.CharField(max_length=50)
    link = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    



