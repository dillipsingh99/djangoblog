from django.db import models
from django.urls import reverse 
from django.conf import settings
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1000, null=True, blank=True)
    body = RichTextUploadingField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to ='bloguploads/')
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE,related_name='blog_posts')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): # new
        return reverse('blog_detail', args=[str(self.id)])



class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name = 'comments')
    comment = models.CharField(max_length=500)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now = True)
    

    def __str__(self):
        return self.comment[ :20]

    def get_absolute_url(self):
        return reverse('home')