from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from ghost_post.models import Post
from ghost_post.utils import post_filters


# Create your views here.

def landing_view(request):
    return HttpResponseRedirect(reverse('homepage', kwargs={'post_filter': 'all'}))


def homepage_view(request, post_filter):
    if post_filter == 'boasts':
        posts = Post.objects.filter(is_roast=False).order_by('-created')
    elif post_filter == 'roasts':
        posts = Post.objects.filter(is_roast=True).order_by('-created')
    else:
        posts = Post.objects.all().order_by('-created')

    return render(request,
                  'index.html',
                  {
                      'posts': posts,
                      'filters': post_filters,
                      'active_filter': post_filter.title()
                  })


def post_vote_view(request, post_filter, action, post_id):
    post = Post.objects.get(id=post_id)
    if action == 'upvote':
        post.up_votes += 1
    else:
        post.down_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage', kwargs={'post_filter': post_filter}))
