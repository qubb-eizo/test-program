from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Max, Sum


class User(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='pics')
    avr_score = models.PositiveIntegerField(null=True, blank=True)
    tests_list_passed = models.PositiveIntegerField(null=True, blank=True)

    def update_score(self):
        self.avr_score = self.test_result.aggregate(points=Sum('avr_score'))

    def test_last_run(self):
        last_run = self.test_result.order_by('id').last()
        return last_run.datetime_run
