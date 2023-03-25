from django.shortcuts import render, HttpResponse

@staticmethod
def Home(request):
    return render(request,"index.html")
    # return html(request, "index")

def html(request, filename):
    context = {"filename": filename,
               "collapse": ""} 
    if filename in ["buttons", "cards"]:
        context["collapse"] = "components"
    if filename in ["utilities-color", "utilities-border", "utilities-animation", "utilities-other"]:
        context["collapse"] = "utilities"
    if filename in ["404", "blank"]:
        context["collapse"] = "pages"
    return render(request, f"{filename}.html", context=context)

def searchByF(self):
    return HttpResponse("This is Search by Filter Page!")

def searchByM(self):
    return HttpResponse("This is Search by Map page!")

def dashboard(self):
    return HttpResponse("This is User Dashboard Page!")

def calc(self):
    return HttpResponse("This is Rent Calculator!")