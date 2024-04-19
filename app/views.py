from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo, PersonalInfo, Education, Project
from faker import Faker 

###############################################

def home(request):
    return render(request, 'home.html')

def todo1(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo1')
    form = TodoForm()
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo1.html', page)

def todo2(request):
    return render(request, 'todo2.html')

def remove1(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo1')

def cv(request):
    return render(request, 'index.html')

def save_resume(request):
    if request.method == "POST":
        # Extracting form data
        name = request.POST.get('name', '')
        about = request.POST.get('about', '')
        age = request.POST.get('age', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        skill = request.POST.get('skill', '')

        # Creating PersonalInfo instance
        personal_info = PersonalInfo.objects.create(
            name=name,
            about=about,
            age=age,
            email=email,
            phone=phone,
            skill=skill,
        )

        # Creating Education instance
        degree1 = request.POST.get('degree1', '')
        college1 = request.POST.get('college1', '')
        year1 = request.POST.get('year1', '')
        education = Education.objects.create(
            personal_info=personal_info,
            degree=degree1,
            college=college1,
            year=year1
        )

        # Creating Project instance
        title = request.POST.get('title', '')
        duration = request.POST.get('duration', '')
        description = request.POST.get('description', '')
        achievement1 = request.POST.get('ach1', '')
        achievement2 = request.POST.get('ach2', '')
        project = Project.objects.create(
            personal_info=personal_info,
            title=title,
            duration=duration,
            description=description,
            achievement1 = achievement1,
            achievement2 = achievement2,
        )

        # Rendering different templates based on button clicked
        if "submit_button" in request.POST:
            if request.POST["submit_button"] == "page1":
                return render(request, 'resumne.html', {'personal': personal_info, 'project': project, 'education': education})
            elif request.POST["submit_button"] == "page2":
                return render(request, 'resumne2.html', {'personal': personal_info, 'project': project, 'education': education})

    return redirect('cv') 

def fake_data(request):
    fake = Faker()
    # if request.method == 'GET':
        # Creating fake data
    personal_info = PersonalInfo.objects.create(
		name=fake.name(),
		about=fake.text(),
		age=fake.random_number(digits=2),
		email=fake.text(),
		phone=fake.phone_number(),
		skill=fake.text(),
	)

    education = Education.objects.create(
		personal_info=personal_info,
		degree=fake.text(),
		college=fake.text(),
		year=fake.text(),
	)
    project = Project.objects.create(
		personal_info=personal_info,
		title=fake.text(),
		duration=fake.text(),
		description=fake.text(),
        achievement1=fake.text(),
        achievement2=fake.text(),
	)
    return render(request, 'index.html', {'personal': personal_info, 'project': project, 'education': education})
