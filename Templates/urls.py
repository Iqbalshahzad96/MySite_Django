from django.urls import path
from Templates import views

# Templates tagging

app_name = "Templates"


urlpatterns = [
    path('',views.base, name='base'),
    path('relative/',views.relative, name='relative'),
    path('other/',views.other, name='other'),
]