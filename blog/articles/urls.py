"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('add-article/', views.add_article, name="add-article"),
    path('articles/', views.all_articles, name='articles'),
    path('articles/<str:url>', views.article_page),
    path('subscriptions/add_subscriber', views.add_subscriber),
    path('subscriptions/preferences/<str:subscriber_id>', views.subscriber_preferences),
    path('subscriptions/save-preferences', views.subscriber_preferences_fetch)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
