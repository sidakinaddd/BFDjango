"""todo URL Configuration

The `urlpatterns` list routes URLs to viewscol. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function viewscol
    1. Add an import:  from my_app import viewscol
    2. Add a URL to urlpatterns:  path('', viewscol.home, name='home')
Class-based viewscol
    1. Add an import:  from other_app.viewscol import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_.urls')),
    path('api/', include('main.urls')),
    path('onlineShop/',include('onlineShop.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
