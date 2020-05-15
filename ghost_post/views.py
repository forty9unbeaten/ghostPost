from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.core import exceptions
from ghost_post.models import Post
from ghost_post.utils import post_filters, post_sorters
from ghost_post.forms import NewPostForm


# Create your views here.

def landing_view(request):
    return HttpResponseRedirect(
        reverse('homepage',
                kwargs={
                    'post_filter': 'all',
                    'post_sort': 'created'
                })
    )


def homepage_view(request, post_filter, post_sort):

    # get posts from db in accordance with url parameter
    if post_filter == 'boasts':
        posts = Post.objects.filter(is_roast=False)
    elif post_filter == 'roasts':
        posts = Post.objects.filter(is_roast=True)
    else:
        posts = Post.objects.all()

    # sort query set of posts based on url parameter
    if post_sort == 'created':
        posts = posts.order_by('-created')
    else:
        posts = posts.extra(
            select={'vote_order': 'up_votes + down_votes'}).order_by('-vote_order')

    return render(request,
                  'index.html',
                  {
                      'posts': posts,
                      'filters': post_filters,
                      'active_filter': post_filter,
                      'sorters': post_sorters,
                      'active_sort': post_sort
                  })


def post_vote_view(request, action, post_id):
    post = Post.objects.get(id=post_id)

    # increase upvote or downvote based on url path parameter
    if action == 'upvote':
        post.up_votes += 1
    else:
        post.down_votes += 1
    post.save()

    # redirect to detail page
    return HttpResponseRedirect(reverse(
        'details',
        kwargs={
            'post_id': post_id
        }
    ))


def new_post_view(request):
    # POST request handling
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            is_roast = False
            if data['boast_or_roast'] == 'roast':
                is_roast = True

            # create new databse record and save
            new_post = Post(
                is_roast=is_roast,
                content=data['content']
            )
            new_post.save()

            # redirect to confirmation page
            return render(request,
                          'createConfirm.html',
                          {
                              'id': new_post.secret_id,
                              'host': request.get_host()
                          })

    # GET request handling
    form = NewPostForm()
    return render(request, 'newPost.html', {'form': form})


def post_detail_view(request, post_id):
    # POST request handling
    if request.method == 'POST':
        post = Post.objects.get(secret_id=post_id)
        post.delete()
        return HttpResponseRedirect(reverse('home_landing'))

    # GET request handling
    try:
        post = Post.objects.get(id=post_id)
        can_delete = False
    except ValueError:
        post = Post.objects.get(secret_id=post_id)
        can_delete = True

    return render(
        request,
        'postDetail.html',
        {
            'post': post,
            'can_delete': can_delete
        })
