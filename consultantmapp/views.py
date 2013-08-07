# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from consultantmapp.models import Consultant
from consultantmapp.models import ConsSkill
from consultantmapp.models import Skill
from consultantmapp.models import Contact
from django.views import generic



def consultant_list(request):
    latest_consultant_list = Consultant.objects.all().order_by('consname')
    context = {'latest_consultant_list': latest_consultant_list}
    return render(request, 'consultant_list.html',context)

#    def index(request):
 #   latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
  #  context = {'latest_poll_list': latest_poll_list}
   # return render(request, 'polls/index.html', context)


    
def search_form(request):
    return render(request, 'search_form.html')

def consultant_view(request, consultant_id):
    consultant_record = Consultant.objects.filter(id=consultant_id)
    consultant_skills = ConsSkill.objects.filter(consultant=consultant_id)
    consultant_contacts = Contact.objects.filter(cosultant=consultant_id).order_by('-contactdate')[:5]
    context = {'consultant_record': consultant_record, 'consultant_skills': consultant_skills, 'consultant_contacts': consultant_contacts}

    return render(request, 'consultant_view.html',context)


    #test comment for git