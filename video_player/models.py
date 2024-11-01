from django.db import models


class Video(models.Model):
    video_name = models.TextField()
    video_file = models.FileField(upload_to="media/videos")
    image_file = models.ImageField(upload_to="media/videoImages")

    def __str__(self):
        return self.video_name


# Create your models here.
