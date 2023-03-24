from django.shortcuts import render, HttpResponse

@staticmethod
def Home(request):
    return render(request,'index.html')
    # return HttpResponse("This is the Homepage!")


def searchByF(self):
    return HttpResponse("This is Search by Filter Page!")

def searchByM(self):
    return HttpResponse("This is Search by Map page!")

def dashboard(self):
    return HttpResponse("This is User Dashboard Page!")

def calc(self):
    return HttpResponse("This is Rent Calculator!")