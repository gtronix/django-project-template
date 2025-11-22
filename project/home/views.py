from django.shortcuts import render

def home(request):
    """
    Simple homepage
    """
    context = {
        'site_name': 'Site Name',
        'page_title': 'Home Page',
        'content_title': 'Home Content',
        'content_message': 'Welcome Home'
    }
    return render(request, 'home/home.html', context)
