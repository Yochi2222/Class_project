"""
URL configuration for AIBookmanage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # The path 'admin/' maps to the Django admin site.
    path('admin/', admin.site.urls),
    
    # The path '' (empty string) maps to the bookmanage app's URLs.
    # This includes all the URLs defined in the 'bookmanage.urls' module.
    path('', include('bookmanage.urls')),
    path('', include('authentication.urls')),

]
