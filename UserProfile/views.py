from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# core/views.py

from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  
            post.save()
            return redirect('some_success_url')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})



def success_page(request):
    return render(request, 'success_page.html', {'user': request.user})


def create_post_view(request):
   
    if(request.method == "POST"):
        caption = request.POST['caption']
        description = request.POST['description']
        print(caption,description)
        return HttpResponse("hello create_post_view")
    else:
        return render(request,'authentication/index1.html')
