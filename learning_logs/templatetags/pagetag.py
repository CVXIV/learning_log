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
		page_ele='<button style="color:dodgerblue;" class="btn btn-default active" onclick=window.location.href="?page=%s">%s</button>'%(loop_page,loop_page)
	else:
		page_ele='<button style="color:dodgerblue;" class="btn btn-default" onclick=window.location.href="?page=%s">%s</button>'%(loop_page,loop_page)
	return page_ele