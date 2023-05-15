from django.urls import path
from .views import upload_csv, map_csv, lead_list,LeadList, LeadDetail

app_name = 'lead_app'
urlpatterns = [
    path('', upload_csv, name='upload_csv'),
    path('map', map_csv, name='map_csv'),
    path('leads', lead_list, name='lead_list'),
 
    path('api/leads', LeadList.as_view(), name='lead_list_api'),
    path('api/leads/<int:pk>', LeadDetail.as_view(), name='lead_detail_api'),
]     
