from datetime import datetime
from random import sample
from string import ascii_letters

from django.db import models


class Image(models.Model):
    def generate_link_for_images():
        random_str = ''.join(sample(ascii_letters, 7))
        datetime_now = datetime.now().strftime('%Y''%m''%d''%H''%M''%S''%f')
        return random_str + datetime_now

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=generate_link_for_images())

    def __str__(self):
        return self.title
