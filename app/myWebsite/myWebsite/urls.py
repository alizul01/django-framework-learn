from django.contrib import admin
from django.urls import path, include
from . import views
from blog import views as blogViews
from about import views as aboutViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('about/', aboutViews.about),
    path('', views.index)
]
