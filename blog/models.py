
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

from .validators import valid_images
from account.validators import valid_file_size
# Create your models here.

class PostCategory(models.Model):
    class Meta:
        verbose_name_plural = 'post categories'
    title = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    class Meta:
        verbose_name_plural = "Posts"
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    image =models.ImageField(upload_to='images/posts/', validators=[valid_file_size, valid_images], null=True)
    description = RichTextUploadingField()
    viewers = models.ManyToManyField(User, blank=True, related_name="viewers")

    liked_users = models.ManyToManyField(User, blank=True, related_name='liked_users')
    disliked_users = models.ManyToManyField(User, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_all_comments(self):
        return self.comment_set.all()
    
    def get_last_3_comments(self):
        return self.comment_set.all().order_by('-writed_at')[:2]
    
    def get_all_liked_users(self):
        return self.liked_users.all()
    
    def get_all_disliked_users(self):
        return self.disliked_users.all()

    def get_total_views(self):
        return self.viewers.count()

    def get_related_posts(self):
        r_posts = None
        posts = Post.objects.filter(category=self.category)
        if len(posts) > 3:
            posts = posts[-3:]
        return posts

    def get_best_clothest_post(self):
        posts = Post.objects.filter(category = self.category)
        max_views = 0
        final_post = None
        for post in posts:
            if max_views <= len(post.viewers.all()):
                max_views = len(post.viewers.all())
                if post.id != self.id:    
                    final_post = post
        return final_post


class Comment(models.Model):
    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ["-writed_at"]
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)

    writed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"User: {self.user} | Text: {self.text[:20]}"


