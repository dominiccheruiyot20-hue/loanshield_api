from django.urls import path
from .views import check_doc
urlpatterns = [path('check/', check_doc)]

