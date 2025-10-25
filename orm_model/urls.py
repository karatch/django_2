from django.urls import path

from orm_model.views import index

urlpatterns = [
    path('', index, name='index'),
]