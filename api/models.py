from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField()

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    client_name = models.CharField(max_length=200)
    feedback = models.TextField()

    def __str__(self):
        return self.client_name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
