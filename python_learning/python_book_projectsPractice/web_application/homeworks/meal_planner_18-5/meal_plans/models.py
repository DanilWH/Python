from django.db import models

class Time(models.Model):
    time = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.time

class Plan(models.Model):
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    plan = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.plan) > 50:
            return f'{self.plan[:50]}...'
        else:
            return self.plan