from xml.dom.minidom import CharacterData
from django.urls import path, include
from .views.list import CharactorList
from .views.detail import CharactorDetail
from .views.sidebar import Sidebar
from .views.forms import Form
from .views.delete import Delete
from .views.update import Update
urlpatterns = [
    path('list/', CharactorList.as_view(), name='list'),
    path('detail/<int:pk>', CharactorDetail.as_view(), name='detail'),
    path('sidebar/', Sidebar.as_view(), name='sidebar'),
    path('form/', Form.as_view(), name='form'),
    path('delete/<int:pk>', Delete.as_view(), name='delete'),
    path('update/<int:pk>', Update.as_view(), name='update'),
]
