from django.urls import path
from . import views
from .views import BlogPostDetailView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap, StaticViewSiteMap

sitemaps = {
    'posts': PostSitemap,
    'static': StaticViewSiteMap
}

urlpatterns = [
    path('', views.index, name="home"),
    path('sitemap.xml', sitemap, {'sitemaps' : sitemaps } , name='sitemap'),
    path('robots.txt',TemplateView.as_view(template_name="app/robots.txt", content_type="text/plain"),),
    path('blog/<int:pk>', views.BlogPostDetailView, name="blog-detail" ),
    path('AlumniListView/', views.AlumniListView, name='AlumniListView'),
    path('GetSchools/', views.GetSchools, name='GetSchools'),
    path('GetIndustries/', views.GetIndustries, name='GetIndustries'),
    path('blogs/', views.BlogPageView, name='blog-page'),
]