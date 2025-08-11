# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import JobViewSet

# router = DefaultRouter()
# router.register(r'jobs', JobViewSet)

# urlpatterns = [
#     path('', include(router.urls)),  # ✅ No extra 'api/' here
# ]

from django.urls import path
from .views import (
    ResumeUploadView,
    compatible_jobs_page,
    groq_match,
)
from .resume_views import get_resume
from .job_views import get_job

urlpatterns = [
    path("upload_resume/", ResumeUploadView.as_view(), name="resume-upload"),
    path("find_jobs/", groq_match, name="find-compatible-jobs"),
    path("find_jobs_page/", compatible_jobs_page, name="find-compatible-jobs-page"),
    path("get_resume/", get_resume, name="get-resume"),
    path("get_job/", get_job, name="get-job"),
]
