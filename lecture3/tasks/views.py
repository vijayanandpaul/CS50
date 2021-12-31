from django.shortcuts import render

tasks = ["Foo", "bar", "baz", "Doe"]

# Create your views here.
def index(request):

    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
    
