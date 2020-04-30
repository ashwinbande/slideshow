from django.db import models
from django.contrib.auth.models import User


class Presentation(models.Model):
    name = models.CharField(max_length=72, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Presentation'

    def __str__(self):
        return self.name


def get_image_saving_path(instance, filename):
    return f'{instance.presentation.id}/images/{filename}'


def get_audio_saving_path(instance, filename):
    return f'{instance.presentation.id}/audio/{filename}'


class Slide(models.Model):
    name = models.CharField(max_length=72, blank=False, null=False)
    image = models.ImageField(upload_to=get_image_saving_path)
    audio = models.FileField(upload_to=get_audio_saving_path)
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


AGREEMENT_CHOICES = [
    ('AA', 'Agree'),
    ('DA', 'Disagree'),
    ('PA', 'Partial Agree'),
]


class FeedBack(models.Model):
    name = models.CharField(max_length=72, blank=False, null=False)
    mobile = models.CharField(max_length=12, blank=False, null=False)
    email = models.EmailField()
    agreement = models.CharField(choices=AGREEMENT_CHOICES, max_length=2)
    suggestion = models.TextField()
    comment = models.TextField()
    slide = models.ForeignKey(Slide, on_delete=models.CASCADE)

    def __str__(self):
        return f'Feedback by {self.name}'
