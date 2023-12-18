from django.db import models
import os


# Model to represent a Carousel. Which in reality is just a grouping of slides
class Carousel(models.Model):
    key = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)


# Model to represent each slide of the carousel, includes fields that would be coded in html for
# higher levels of custimizability.
class Slide(models.Model):
    key = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=120)
    label = models.CharField(max_length=120, blank=True)
    caption = models.CharField(max_length=120, blank=True)
    image = models.ImageField(upload_to="slides")
    duration = models.DecimalField(max_digits=7, decimal_places=1, default=10)
    parent = models.ForeignKey(Carousel, on_delete=models.CASCADE, related_name="slide")

    def dur_millis(self):
        if self.duration is not None:
            return self.duration * 1000
        else:
            return None

    def image_name(self):
        if self.image is not None:
            return os.path.basename(self.image.url)
        else:
            return None
