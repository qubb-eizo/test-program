# Generated by Django 3.2.6 on 2021-08-07 17:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsuite', '0003_alter_question_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='is_correct',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='testresultdetails',
            name='is_correct',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
    ]