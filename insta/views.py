
from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Post, Comment, Like
import operator
from django.contrib.auth.decorators import login_required

def main(request):
    posts = Post.objects.all()
    sort = request.GET.get('sort', '')

    if sort == 'new':
        posts = Post.objects.all()
    elif sort == 'like_up':
        ordered_posts ={}
        post_list = Post.objects.all()
        for post in post_list:
            ordered_posts[post] = post.like_count
        post_list = sorted(ordered_posts.items(), key=operator.itemgetter(1), reverse=True)
        posts = []
        for post in post_list:
            posts.append(post[0])
    elif sort == 'like_down':
        ordered_posts ={}
        post_list = Post.objects.all()
        for post in post_list:
            ordered_posts[post] = post.like_count
        post_list = sorted(ordered_posts.items(), key=operator.itemgetter(1), reverse=False)
        posts = []
        for post in post_list:
            posts.append(post[0])

    try:
        liked_post = Like.objects.filter(user=request.user).values_list('post__id', flat=True)
    except:
        liked_post = None

    return render(request, 'insta/main.html', {
        'posts':posts,
        'liked_post':liked_post
    })

@login_required
def like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method =='POST':
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
        except:
            Like.objects.create(user=request.user, post=post)

    return redirect('main')