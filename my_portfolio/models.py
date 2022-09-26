from django.db import models

from account.validators import valid_file_size
from blog.validators import valid_images

class Study(models.Model):
    class Meta: 
        verbose_name_plural = 'Studies'
    where = models.CharField(max_length=100, help_text="Required")
    specialize = models.CharField(max_length=100, help_text="Required")
    description = models.TextField(max_length=250, null=True)
    degree = models.CharField(max_length=80, blank=True, null=True)
    from_date = models.DateField(help_text="Required")
    to_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.where} | Specialize: {self.specialize}"
    

class Experiance(models.Model):
    class Meta:
        verbose_name_plural = 'Experiances'
    company = models.CharField(max_length=120, help_text="Required")
    specialize = models.CharField(max_length=100, help_text="Required")
    description = models.TextField(max_length=250, null=True)
    technalogies = models.CharField(max_length=200, help_text="Required!!! \n\
        Example: Python, Django, DRF, Js, Web Socket ...")
    from_date = models.DateField(help_text="Required")
    to_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Company: {self.company} | Specialize: {self.specialize}"


class PortfolioCategory(models.Model):
    class Meta:
        verbose_name_plural = "Portfolio Categories"
    title = models.CharField(max_length=60, help_text="Required")
    slug = models.CharField(max_length=30, help_text="Required!!! \n\
        Slug should be shorter than title \
        \nExample: \n\
        Title: Web development \nSlug: Web")
    def __str__(self):
        return self.title

    def get_all_portfolios(self):
        return self.portfolio_set.all()



class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = 'Portfolios'
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, help_text="Required")
    title = models.CharField(max_length=120, help_text="Required")
    link = models.CharField(max_length=250, help_text="Required")
    image = models.ImageField(upload_to = 'images/portfolio_images', help_text="Required",\
        validators=[valid_images, valid_file_size])
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title  
     
    

