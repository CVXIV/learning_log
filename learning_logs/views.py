from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404,HttpResponse
#reverse接收url中的name作为第一个参数
#不带参数的：{%url'name'%}
#带参数的：参数可以是变量名 {%url'name' 参数 %} 
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Topic,Entry,IMG
from .forms import TopicForm,EntryForm,IMGForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models.deletion import ProtectedError
from django.views.decorators.csrf import csrf_exempt
import json
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\','/')
def index(request):
	#主页
	return render(request,'learning_logs/index.html')
#对于某些页面，只允许已登录的用户访问它们
#@login_required
def base(request):
	return render(request,'learning_logs/base.html')
def topics(request):
	if request.user.is_authenticated():
		topics=Topic.objects.filter(owner=request.user).order_by('date_added')
	else:
		topics=Topic.objects.filter(topic_ispublic=1).order_by('date_added')
	context={'topics':topics}
	return render(request,'learning_logs/topics.html',context)
#@login_required
def topic(request, topic_id, page_no):
	#显示单个主题及其所有的条目
	#现在，如果你请求不存在的主题（例如/topics/999999/），将看到404错误页面
	topic = get_object_or_404(Topic, id=topic_id)
	if request.user.is_authenticated():
		check_topic_owner(request,topic)
	else:
		if topic.topic_ispublic==0:
			raise Http404
	#确认请求的主题属于当前用户
	#date_added前面的减号指定按降序排列
	entries = topic.entry_set.order_by('-date_added')
	capacity=3
	paginator=Paginator(entries,capacity)
	page=request.GET.get('page')
	try:
		entry=paginator.page(page)
	except PageNotAnInteger:
		try:
			entry = paginator.page(int(page_no))
		except EmptyPage:
			if int(page_no)>1:
				entry = paginator.page(int(page_no)-1)
			else:
				entry=paginator.page(1)
	except EmptyPage:
		entry=paginator.page(paginator.num_pages)
	context = {'topic': topic, 'entries': entry}
	return render(request, 'learning_logs/topic.html',context)
@login_required
def edit_topic(request,topic_id):
	topic = get_object_or_404(Topic, id=topic_id)
	check_topic_owner(request,topic)
	if request.method!='POST':
		#初次请求，使用当前条目填充表单
		form=TopicForm(instance=topic)
	else:
		form=TopicForm(instance=topic,data=request.POST)
		if form.is_valid:
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id,0]))
	context={'topic':topic,'form':form}
	return render(request,'learning_logs/edit_topic.html', context)
@login_required
def new_topic(request):
	#未提交数据，创建一个新表单
	if request.method!='POST':
		form=TopicForm()
	#POST提交的数据，对数据进行处理
	else:
		form=TopicForm(request.POST)
		if form.is_valid():
			new_topic=form.save(commit=False)
			new_topic.owner=request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))
	context={'form':form}
	return render(request,'learning_logs/new_topic.html',context)
@login_required
def new_entry(request,topic_id):
	topic = get_object_or_404(Topic, id=topic_id)
	check_topic_owner(request,topic)
	if request.method!='POST':
		form=EntryForm()
	else:
		form=EntryForm(data=request.POST)
		if form.is_valid():
			new_entry=form.save(commit=False)
			new_entry.topic=topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id,0]))
	context={'topic':topic,'form':form}
	return render(request, 'learning_logs/new_entry.html', context)
@login_required
def edit_entry(request,entry_id,page_no):
	entry=get_object_or_404(Entry,id=entry_id)
	topic=entry.topic
	check_topic_owner(request,topic)
	if request.method!='POST':
		#初次请求，使用当前条目填充表单
		form=EntryForm(instance=entry)
	else:
		form=EntryForm(instance=entry,data=request.POST)
		if form.is_valid:
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id,page_no]))
	context={'entry':entry,'topic':topic,'form':form,'page_no':page_no}
	return render(request,'learning_logs/edit_entry.html', context)
@login_required
def dele_entry(request,entry_id,page_no):
	entry=get_object_or_404(Entry,id=entry_id)
	topic=entry.topic
	check_topic_owner(request,topic)
	try:
		entry.delete()
	except ProtectedError:
		dele_img(request,entry_id)
		entry.delete()
	return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id,page_no]))
@login_required
def dele_topic(request,topic_id):
	topic = get_object_or_404(Topic, id=topic_id)
	check_topic_owner(request,topic)
	try:
		Topic.objects.filter(id=topic_id).delete()
	except ProtectedError:
		entries=Entry.objects.filter(topic=topic)
		for entry in entries:
			dele_img(request,entry.id)
		Topic.objects.filter(id=topic_id).delete()
	return HttpResponseRedirect(reverse('learning_logs:topics'))
def check_topic_owner(request,topic):
	if topic.owner!=request.user:
		raise Http404
@login_required
def uploadImg(request,entry_id,page_no):
	entry=get_object_or_404(Entry, id=entry_id)
	topic=entry.topic
	if request.method == 'POST':
		form = IMGForm(request.POST,request.FILES)
		if form.is_valid():
			img=form.save(commit=False)
			import time,random
			ext=os.path.splitext(img.img.name)[1]
			img.img.name=time.strftime('%Y%m%d%H%M%S')+'_%d' % random.randint(0,100)+ext
			img.entry=entry
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:show_img', args=[entry.id, page_no]))
	else:
		form=IMGForm()
	context={'form':form,'topic':topic,'entry':entry,'page_no':page_no}
	return render(request, 'learning_logs/uploadImg.html',context)
@login_required
def deleAllImg(request,entry_id):
	dele_img(request,entry_id)
	result={}
	return HttpResponse(json.dumps(result), content_type="application/json")
@login_required
@csrf_exempt
def deleImg(request):
	entry_id=request.POST['entry_id']
	img_id=request.POST['img_id']
	dele_img(request,entry_id,img_id)
	result={}
	return HttpResponse(json.dumps(result), content_type="application/json")
@login_required
def showImg(request,entry_id,page_no):
	entry=get_object_or_404(Entry, id=entry_id)
	topic=entry.topic
	check_topic_owner(request,topic)
	imgs = IMG.objects.filter(entry=entry)
	context = {'imgs':imgs, 'topic': topic, 'entry': entry, 'page_no': page_no}
	return render(request, 'learning_logs/showImg.html', context)
def dele_img(request,entry_id,img_id=None):
	entry = get_object_or_404(Entry, id=entry_id)
	topic = entry.topic
	check_topic_owner(request, topic)
	if img_id is None :
		imgs = IMG.objects.filter(entry=entry)
	else:
		imgs = IMG.objects.filter(entry=entry, id=img_id)
	for img in imgs:
		filename = BASE_DIR + img.img.url
		if os.path.exists(filename):
			os.remove(filename)
	imgs.delete()