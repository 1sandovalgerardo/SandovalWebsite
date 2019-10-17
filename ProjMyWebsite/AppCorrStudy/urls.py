from django.conf.urls import url
from AppCorrStudy import views

app_name = 'corrstudy'

urlpatterns = [url(r'^$', views.CorrStudyView.as_view(), name='corrstudy')]
