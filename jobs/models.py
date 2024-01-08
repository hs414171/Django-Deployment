from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    company = models.CharField(max_length=255)
    salary_per_month = models.FloatField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
        db_table = 'JobInfo'

    def __str__(self):
        return self.title