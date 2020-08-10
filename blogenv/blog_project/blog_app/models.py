from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blog(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    blog_title=models.CharField(max_length=200, verbose_name='Put a Title')
    slug=models.SlugField(max_length=100,unique=True)
    blog_content=models.TextField(verbose_name='What is in your mind?')
    blog_image=models.ImageField(upload_to='blog_pics', verbose_name='image')
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-publish_date']

    def __str__(self):
        return self.blog_title
class comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    blog=models.ForeignKey(blog, on_delete=models.CASCADE, related_name='bolg_comment')
    comments=models.TextField(verbose_name='comment')
    comment_date=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-comment_date']

    def __str__(self):
        return self.comments
class like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_like')
    blog=models.ForeignKey(blog, on_delete=models.CASCADE, related_name='blog_like')
    def __str__(self):
        return str(self.user) +" liked "+ str(self.blog)

