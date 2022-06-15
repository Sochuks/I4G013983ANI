from django.shortcuts import render

# Display Welcome to Blog on website
def blog(request):
    return render(request, 'blog.html', {})
