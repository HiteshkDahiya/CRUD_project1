from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import StudentForm
from .models import StudentRegistration
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    template = loader.get_template('enroll/enroll.html')
    if request.method == 'POST':
        stu = StudentForm(request.POST)
        if stu.is_valid():
            nm = stu.cleaned_data['name']
            em = stu.cleaned_data['email']
            ps = stu.cleaned_data['password']
            user = StudentRegistration(name = nm, email = em, password = ps)
            user.save()
            return HttpResponseRedirect('/')

    else:
        stu = StudentForm()

    data = StudentRegistration.objects.all()
    context = {
        'stu': stu,
        'data': data
    }
    return HttpResponse(template.render(context,request))

def delete(request,id):
    if request.method == 'POST':
        pi = StudentRegistration.objects.get(id = id)
        pi.delete()
        return HttpResponseRedirect('/')

def update(request,id):
    if request.method == "POST":
        pi = StudentRegistration.objects.get(pk=id)
        stu = StudentForm(request.POST, instance=pi)
        if stu.is_valid():
            stu.save()
            return HttpResponseRedirect('/')
    else:
        pi = StudentRegistration.objects.get(pk=id)
        stu = StudentForm(instance=pi)


    return render(request,'enroll/update.html',{'stu':stu,'pi':pi})
