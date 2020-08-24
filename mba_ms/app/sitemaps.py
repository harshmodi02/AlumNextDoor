from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post
 
 
class PostSitemap(Sitemap):    
    changefreq = "weekly"
    priority = 0.9
    protocol = "https"
 
    def items(self):
        return Post.objects.all()
 
    def lastmod(self, obj):
        return obj.publish_date


class StaticViewSiteMap(Sitemap):

    protocol = "https"
    
    def items(self):
        return ['home', 'blog-page', ]

    def location(self, item):
        return reverse(item)