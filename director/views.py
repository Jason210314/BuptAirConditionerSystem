from django.shortcuts import render

# Create your views here.
def director(request):
    if request.method == 'GET':
        print(request.user)
        return render(request, 'director/index.html')

def forms(request):
    date = [i for i in range(8, 15)]
    if request.method == 'GET':
        print(request.user)
        return render(request, 'director/forms.html', {'date': date})