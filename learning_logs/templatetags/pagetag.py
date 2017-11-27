from django.utils.html import format_html
from django import template
register = template.Library()
@register.simple_tag
def circle_page(curr_page,loop_page,num_pages):
	if curr_page<=3:
		if loop_page<=5:
			page_ele=format_page(curr_page,loop_page)
		else:
			return ''
	elif num_pages-curr_page>=2:
		if abs(loop_page-curr_page)<=2:
			page_ele=format_page(curr_page,loop_page)
		else:
			return ''
	else:
		if loop_page>num_pages-5:
			page_ele=format_page(curr_page,loop_page)
		else:
			return ''
	return format_html(page_ele)
def format_page(curr_page,loop_page):
	if curr_page==loop_page:
		page_ele='<li class="active"><a style="text-decoration:none;outline:none;" href="?page=%s">%s</a></li>'%(loop_page,loop_page)
	else:
		page_ele='<li><a style="text-decoration:none;outline:none;" href="?page=%s">%s</a></li>'%(loop_page,loop_page)
	return page_ele