from django.urls import path
from . import views

urlpatterns = [
    path('formpage/',views.form_name_view, name='form_name'),
]
