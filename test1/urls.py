from django.urls import path, include
from .views import double, new_double

urlpatterns = [
    path('', double, name='double'),
    path('new', new_double, name='new_double'),

]