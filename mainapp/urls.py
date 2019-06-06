from django.urls import path
from .views import *

urlpatterns = [
    path('', mainpage, name='mainpage_url'),
    path('writemess/', MessageCreate.as_view(), name='create_mess_url'),
    path('viewmessages/', LoginCell.as_view(), name='login_cell_url')
]