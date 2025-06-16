from django.urls import path
from .views import hello_world , hello_chadni 

urlpatterns = [
    path('', hello_world),
    path('chadni/',hello_chadni)
]
