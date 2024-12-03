from django.shortcuts import render

def jinja_print(request):
    context = {
        'names': ['pavan', 'vinod', 'suresh'],
        'ages': [22, 24, 28],
    }
    return render(request, 'jinja_print.html', context)
