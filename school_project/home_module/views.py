from django.db.models import Count
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'


def site_header_partial(request):
    # setting = SiteSetting.objects.filter(is_main_setting=True).first()
    # category = ProductCategory.objects.filter(is_active=True)
    # child_category = ChildCategory.objects.filter(is_active=True)
    # context = {
    #     'site_setting': setting,
    #     'category': category,
    #     'child_category': child_category,
    # }
    return render(request, 'shared/site_header_section.html', {})


def site_footer_partial(request):
    return render(request, 'shared/site_footer_section.html', {})
