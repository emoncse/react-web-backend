from rest_framework import viewsets
from .models import Slider, Service, Project, Testimonial, Contact
from .serializers import SliderSerializer, ServiceSerializer, ProjectSerializer, TestimonialSerializer, \
    ContactSerializer


class SliderListView(viewsets.ReadOnlyModelViewSet):
    model_name = Slider
    serializer_class = SliderSerializer

    def get_queryset(self):
        return self.model_name.objects.all()

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        return self.serializer_class


class ServiceListView(viewsets.ReadOnlyModelViewSet):
    model_name = Service
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return self.model_name.objects.all()

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        return self.serializer_class


class ProjectListView(viewsets.ReadOnlyModelViewSet):
    model_name = Project
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.model_name.objects.all()

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        return self.serializer_class


class TestimonialListView(viewsets.ReadOnlyModelViewSet):
    model_name = Testimonial
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        return self.model_name.objects.all()

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        return self.serializer_class


class ContactCreateView(viewsets.ModelViewSet):
    model_name = Contact
    serializer_class = ContactSerializer

    def get_queryset(self):
        return self.model_name.objects.all()

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        return self.serializer_class
