from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(fecha_publicada__lte=timezone.now()).order_by('fecha_publicada')
    return render(request, 'Blog/post_base.html',{'posts':posts})

def post_nuevo(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicada = timezone.now()
            post.save()
            return redirect('/')
        
    else:
        form = PostForm()
    return render(request,'Blog/post_editar.html',{'form':form})

def post_editar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = PostForm(instance=post)
    return render(request, 'Blog/post_editar.html', {'form': form})

def post_borrado(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.delete()
    return redirect('/')