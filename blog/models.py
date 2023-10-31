from django.db import models
from django.urls import reverse

# Create your models here.\
choices = (
    ("Draft","Draft"),
    ("Published","Published"),
    ('Archived','Archived'),
)

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug=models.SlugField()

    class Meta:
        ordering =('title',)
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s' % self.slug
    
    
class Post(models.Model):
    category=models.ForeignKey(Category,related_name='posts',on_delete=models.CASCADE)
    title= models.CharField(max_length=255)
    intro = models.TextField(max_length=500)
    slug = models.SlugField()
    image = models.ImageField(upload_to="media", blank=True)
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=choices, max_length=255)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ('-publish_date',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/%s' % (self.category.slug,self.slug)



class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)
        
    def __str__(self):
        return self.name

