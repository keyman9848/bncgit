"""xmjc_analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# 配置加载静态页面
from django.conf import settings
from django.conf.urls.static import static

from analysis import views as analysis_views
# 导入子文件夹下py
from analysis.visualtools import echarts as analysis_echarts

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 页面url配置
    url(r'^$', analysis_views.index,name='index'), # 站点信息
    url(r'^index/$', analysis_views.index,name='index'),# 首页
    # 导航栏链接配置
    url(r'^xmjf/$', analysis_views.xmjf,name='xmjf'), # 项目经费
    url(r'^xmksh/$', analysis_echarts.xmksh,name='xmksh'), # 项目可视化测试

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)