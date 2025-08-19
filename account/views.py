from django.shortcuts import render

def custom_404(refresh, exception):
    return render(request, '404.html', status=404)
