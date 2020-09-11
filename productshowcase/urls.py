from django.contrib import admin
from django.urls import path
from product.views import *
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'Sri Sai'
admin.site.site_title = 'Sri Sai'
admin.site.index_title = 'Sri Sai administration'


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home, name = "home"),
    path("about/",About, name= 'about'),
    path("contact/",Contact, name= 'contact'),
    path("gallery/",Gallery, name= 'gallery'),
    path("shop/",Shop, name= 'shop'),
    path("info/",Info, name= 'info'),
    path("product_details/<int:p_id>/", Product_details_page, name="product_details"),
    path("blog/",Blog, name= 'blog'),
    path("productshowcase/",Product_Show_Case, name= 'productshowcase'),
    path("product_description_page/",Product_Description_Page, name= 'product_description_page'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
