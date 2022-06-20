from django.shortcuts import render, redirect
from blogapp.forms.blog import blogForm
from django.contrib import messages
from blogapp.models.blog.blog import Blog
from django.contrib.auth.decorators import login_required
from ....models.user.user import User

# Create your views here.

def blogPage(request, pk):
    title = 'Blog Django'

    blog = Blog.objects.get(id=pk)

    context = {
        'title': title,
        'blog': blog,
        
    }

    return render(request, 'pages/blog/blog.html', context)


@login_required(login_url= 'login')
def createBlogPage(request):
    title = 'Create a Blog'
    form = blogForm()

    
    if request.method == "POST":
        form = blogForm(request.POST)
        if form.is_valid():    
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('home')
        else:
            messages.error(request, 'Create blog failed')

    context = {
        'title': title,
        'form': form    
    }

    return render(request, 'pages/blog/create.html', context)

@login_required(login_url= 'login')
def userBlogPage(request, pk):
    title = 'My Blogs'
    author = User.objects.get(id=pk)
    blog = Blog.objects.filter(user_id=author.id)

    context = {
        'title': title,
        'user': author,
        'blog': blog
    }

    return render(request, 'pages/blog/userBlog.html', context)
    
@login_required(login_url= 'login')
def updateBlogPage(request, pk):
    title = 'Update Blogs'
    page = 'update'
    blog = Blog.objects.get(id=pk)
    form = blogForm(instance=blog)

    if request.method == "POST":
        form = blogForm(request.POST, instance=blog)
        if form.is_valid():    
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('my-blog',blog.user_id)
        else:
            messages.error(request, 'Update failed')


    context = {
        'title': title,
        'page': page,
        'form': form,
    }

    return render(request, 'pages/blog/create.html', context)
    
@login_required(login_url= 'login')
def deleteBlogPage(request, pk):
    title = 'Delete Blogs'
    blog = Blog.objects.get(id=pk)
    form = blogForm(instance=blog)

    if request.method == 'POST':
        blog.delete()
        return redirect('my-blog', blog.user_id)


    context = {
        'title': title,
        'blog': blog,
        'form': form,
    }

    return render(request, 'pages/blog/delete.html', context)