from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Skill, Service, Project, ContactRequest
from .forms import ContactForm



def home(request):
    skills = Skill.objects.all()
    services = Service.objects.all()
    return render(request, 'portfolio/home.html', {'skills': skills, 'services': services})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})

@login_required
def contact_requests(request):
    contact_requests = ContactRequest.objects.order_by('-created_at')
    return render(request, 'portfolio/contact_requests.html', {'contact_requests': contact_requests})


@login_required
def delete_contact_request(request, pk):
    contact_request = get_object_or_404(ContactRequest, pk=pk)
    if request.method == 'POST':
        contact_request.delete()
        return redirect('contact_requests')
    return render(request, 'portfolio/delete_contact_request.html', {'contact_request': contact_request})
