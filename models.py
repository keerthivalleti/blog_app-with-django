from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225)
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['date_added']



# Create your models here.
