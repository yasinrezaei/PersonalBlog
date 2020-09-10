from django.urls import path
from .views import home,detail,about,category
#برای اینکه بتونیم مدیا هارو در قسمت ادمین ببینیم
from django.conf import settings
from django.conf.urls.static import static
#----------------------------------------------------


app_name="blog"
urlpatterns = [
    path('',home,name="home"),
    path('article/<slug:slug>',detail,name="detail"),
    path('category/<slug:slug>',category,name="category"),
    path('about',about,name="about")

]
#فقط برای حالت دیباگ از این قسمت استفاده میکنیم برای دیپلوی کردن خیر
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#-----------------------------------------------------