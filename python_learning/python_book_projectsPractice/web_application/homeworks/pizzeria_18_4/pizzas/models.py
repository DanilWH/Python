from django.db import models

class Pizza(models.Model):
    """Information about a pizza name, got from user."""
    name = models.CharField(max_length=50)

    def __str__(self):
        """Returns a string value of a pizza name."""
        return self.name

class Toping(models.Model):
    """Information about name topings of a pizza that is associated with a 
    pizza name."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'topings'

    def __str__(self):
        """Returns a string value of a toping name."""
        return self.name