from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(fecha_publicada__lte=timezone.now()).order_by('fecha_publicada')
    return render(request, 'Blog/post_list.html',{'posts':posts})
