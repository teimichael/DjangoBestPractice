from django.urls import path
from rest_framework import routers

from service.controllers.user import UserController
from service.view_controllers.index import IndexViewController
from service.view_controllers.upload import UploadViewController
from service.view_controllers.user import UserViewController

# View controller URL patterns
urlpatterns = [
    path('', IndexViewController.view, name='index'),
    path('user', UserViewController.view, name='user'),
    path('upload', UploadViewController.view, name='upload'),
]

# API Controller URL patterns
router = routers.DefaultRouter()
router.register(r'users', UserController)

urlpatterns += router.urls
