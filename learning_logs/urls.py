#定义learning_logs的URL模式
from django.conf.urls import url
from . import views
#r让Python将接下来的字符串视为原始字符串
#请求的URL与前述正则表达式匹配时,Django将调用views.index
#第三个实参将这个URL模式的名称 指定为index，让我们能够在代码的其他地方引用它
urlpatterns=[
url(r'^$',views.base,name='base'),
url(r'^index/$',views.index,name='index'),
url(r'^topics/$',views.topics,name='topics'),
#这个表达式的第二部分 （/(?P<topic_id>\d+)/）与包含在两个斜杠内的整数匹配，
#并将这个整数存储在一个名为topic_id的实参中。这部分表达式两边的括号捕获URL
#中的值；?P<topic_id>将匹配的值存储到topic_id中
url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
# 用于添加新主题的网页
url(r'^new_topic/$', views.new_topic, name='new_topic'),
# 用于添加新条目的页面
url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
# 用于编辑条目的页面
url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,name='edit_entry'),
url(r'^delete_entry/(?P<entry_id>\d+)/$', views.delete_entry,name='delete_entry'),
url(r'^edit_topic/(?P<topic_id>\d+)/$', views.edit_topic,name='edit_topic'),
]