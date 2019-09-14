
from django.shortcuts import render
from .models import Post
import operator

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

    return render(request, 'insta/main.html', {
        'posts':posts,
    })