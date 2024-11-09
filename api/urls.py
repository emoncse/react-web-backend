from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SliderListView, ServiceListView, ProjectListView, TestimonialListView, ContactCreateView

router = DefaultRouter()
router.register('sliders', SliderListView, basename='slider')
router.register('services', ServiceListView, basename='service')
router.register('projects', ProjectListView, basename='project')
router.register('testimonials', TestimonialListView, basename='testimonial')
router.register('contact', ContactCreateView, basename='contact')


urlpatterns = [
    path(r'', include(router.urls)),
]
