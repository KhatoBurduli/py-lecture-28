from django.shortcuts import render

from human.forms import HumanForm


# Create your views here.
def human_list(request):

    return render(request, 'human_list.html', {"form": HumanForm})