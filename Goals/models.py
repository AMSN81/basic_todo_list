from django.db import models
from django.contrib.auth import get_user_model,get_user
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class todo(models.Model):

    class priorty_choices(models.TextChoices):
        crit = "1", "critical"
        high = "2", "high"
        mid = "3", "mid"
        low = "4", "low"    

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    priorty = models.CharField(max_length=1, choices=priorty_choices.choices, default=priorty_choices.mid)
    progress = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])

    def __str__(self) -> str:
        return self.name
    
    @property
    def progress_percent(self):
        return f'%{self.progress}'
