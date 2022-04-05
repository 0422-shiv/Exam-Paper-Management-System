from django.urls import path
from . import views

urlpatterns = [

    path('', views.DataUploadView.as_view(), name="DataUpload"),
    path('update-data/<int:id>', views.UpdateDataUploadView.as_view(), name="UpdateDataUploadView"),
    path('delete-data/<int:id>', views.DeleteDataView, name="DeleteDataView")

]