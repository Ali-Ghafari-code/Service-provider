from django.db.models import Count
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'


def site_header_partial(request):
    user = request.user
    full_name = user.fullname if user.is_authenticated else None  # Assuming the full name is stored in a field named 'full_name'
    context = {
        'full_name': full_name,
    }
    return render(request, 'shared/site_header_section.html', context)


def site_footer_partial(request):
    return render(request, 'shared/site_footer_section.html', {})
