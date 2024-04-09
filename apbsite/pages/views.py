from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from.models import WpOptions


def index(request):
    options=WpOptions.objects.all()
    context = {"options": options,}
    return render(request, "pages/index.html", context)

def about(request):
    return render(request, "pages/about.html")

def gallery(request):
    return render(request, "pages/gallery.html")


# def index(request):
#     options_list = WpOptions.objects.order_by("option_id")[:5]
#     output = ", ".join([o.option_name + ": " + o.option_value for o in options_list])
#     return HttpResponse(output)


def detail(request, option_id):
    return HttpResponse("You're looking at option %s." % option_id)
