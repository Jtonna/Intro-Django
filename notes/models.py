from django.db import models
from uuid import uuid4

# Create your models here.
class Note(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=500, blank=True)
	sidenote = models.TextField(max_length=50, blank=True)
	# Adding a key recorder
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	
