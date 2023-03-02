
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Post(models.Model):

    title = models.CharField(max_length=170 , unique = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    slug = models.SlugField(max_length = 100, unique = True)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    uploaded_date = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to = "images" ,blank = True, null = True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    name = models.CharField(max_length = 120)
    comment = models.TextField(max_length = 1000)
    created_date = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.name

    

