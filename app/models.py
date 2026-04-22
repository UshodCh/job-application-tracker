from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class jobappli(models.Model):
    choices=[  ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Offer', 'Offer'),
        ('Rejected', 'Rejected'), ]
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comname = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=choices, default='Applied')
    apldate = models.DateField()
    link = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline=models.DateField(blank=True, null=True)

    def __str__(self):
       return f"{self.comname} - {self.title}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    skills = models.TextField(help_text="e.g. Python, Django, React")
    bio = models.TextField(blank=True)
    def __str__(self):
        return f"{self.user.username}'s Profile"
    