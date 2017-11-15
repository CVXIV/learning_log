from django import forms
from .models import Topic,Entry
class TopicForm(forms.ModelForm):
	class Meta:
		model=Topic
		fields=['text','topic_ispublic']#只显示model中指定的字段
		#让Django不要为字段text生成标签
		labels={'text':'TopicName','topic_ispublic':'Public Or Not'}
class EntryForm(forms.ModelForm):
	class Meta:
		model=Entry
		fields=['text']
		labels={'text':''}
		widgets={'text':forms.Textarea(attrs={'cols':80})}