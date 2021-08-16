from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Max, Sum


class User(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='pics')
    avr_score = models.PositiveIntegerField(null=True, blank=True)
    tests_list_passed = models.PositiveIntegerField(null=True, blank=True)

    def update_score(self):
        self.avr_score = self.test_result.aggregate(score=Sum('avr_score')).get('score')
        return self.avr_score

    def test_last_run(self):
        if self.test_result.count() != 0:
            return self.test_result.last().datetime_run
        else:
            return "________"

    def num_runs(self):
        num_runs = self.test_result.count()
        return num_runs
