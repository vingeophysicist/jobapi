from django.urls import path
from jobapp.api.views import JobOfferdetailAPIView, JobOfferListCreateAPIView



urlpatterns = [
    path("jobs/", JobOfferListCreateAPIView.as_view(), name = "job_list"),
    path("jobs/<int:pk>/", JobOfferdetailAPIView.as_view(), name = "job_detail")

]