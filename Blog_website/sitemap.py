from django.contrib.sitemaps import  Sitemap
from django.shortcuts import *

from blog.models import *

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()
    
class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(status="Published")
    
    def lastmod(self,obj):
        return obj.publish_date