import datetime
from celery import shared_task
from django.conf import settings

from testsuite.models import Test, TestResult


@shared_task
def run_slow(idx):
    test = Test.objects.get(id=idx)
    print(test.title)
    print('Really done!')


@shared_task()
def cleanup_outdated_testruns():
    outdated_tests = TestResult.objects.filter(
        is_completed=False,
        datetime_run__lte=datetime.datetime.now() - datetime.timedelta(seconds=settings.SESSION_COOKIE_AGE)
    )
    outdated_tests.delete()

    print('Outdated testresults deleted!')
