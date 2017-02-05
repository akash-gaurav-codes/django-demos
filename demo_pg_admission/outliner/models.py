from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Entry(models.Model):
	heading = models.CharField(max_length=140)
	text    = models.TextField(blank=True, null=True)
	parent  = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(blank=True, null=True)
	deleted = models.BooleanField(default=False)

	def __str__(self):
		return (self.heading)