from django.db import models
from django.contrib.auth.models import User
class Topic(models.Model):
	text=models.CharField(max_length=20)
	date_added=models.DateTimeField(auto_now_add=True)
	public=((0,'Private'),(1,'Public'));
	topic_ispublic=models.IntegerField(choices=public,default='Private')
	owner = models.ForeignKey(User)
	def __str__(self):
		return self.text
class Entry(models.Model):
	topic = models.ForeignKey(Topic)
	text=models.TextField()
	date_added=models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural='entries'
	def __str__(self):
		if len(self.text)>50:
			return self.text[:50]+"..."
		else:
			return self.text
