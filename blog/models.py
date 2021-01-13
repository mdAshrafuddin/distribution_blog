from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html

# Create your models here.
STATUS = (
    (0, 'Darft'),
    (1, 'Published')
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField(max_length=100)
    # image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ManyToManyField(Categories)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now=True)
    updated_on  = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to='images/', null=True, blank=True)

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            _thumbnail = get_thumbnail(self.thumbnail,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="100px" height="50px">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""
    
    class meta:
        ordering = ['-title']

    def __str__(self):
        return self.title  

class Categories(models.Model):
    name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now=True)
    updated_on  = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=80)
    created_on = models.DateTimeField(auto_now=True)
    updated_on  = models.DateTimeField(auto_now=True)


class Post_comment(models.Model):
    name = models.CharField(max_length=80)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='Comment_Post')
    short_content = models.TextField()
    image = models.ImageField()
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on  = models.DateTimeField(auto_now=True)
