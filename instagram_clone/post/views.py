from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from post.models import Stream, Post, Tag, Likes
from post.forms import NewPostForm
from django.contrib.auth.decorators import login_required
from authy.models import Profile
from comment.models import Comment
from comment.forms import CommentForm


# Create your views here.
@login_required
def index(request):
    user = request.user
    posts = Stream.objects.filter(user=user)

    group_ids = []

    for post in posts:
        group_ids.append(post.post_id)

    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')

    favorited = False
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=user)
        # For the color of the favorite button

        if profile.favorites.filter(id__in=group_ids).all().exists():
            favorited = True

    template = loader.get_template('index.html')

    context = {
        'post_items': post_items,
        'favorited': favorited,
    }

    return HttpResponse(template.render(context, request))


@login_required
def NewPost(request):
    user = request.user.id
    tags_objs = []

    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tags_form = form.cleaned_data.get('tags')

            tags_list = list(tags_form.split(','))
            for tag in tags_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_objs.append(t)

            p, created = Post.objects.get_or_create(picture=picture, caption=caption, user_id=user)
            p.tags.set(tags_objs)
            p.save()
            return redirect('index')

    else:
        form = NewPostForm()

    context = {
        'form': form,
    }

    return render(request, 'newpost.html', context)


@login_required
def PostDetails(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    profile = Profile.objects.get(user=user)
    favorited = False

    # comment
    comments = Comment.objects.filter(post=post).order_by('date')

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=user)
        # For the color of the favorite button

        if profile.favorites.filter(id=post_id).exists():
            favorited = True

    # Comments Form
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = user
            comment.save()
            return HttpResponseRedirect(reverse('postdetails', args=[post_id]))
    else:
        form = CommentForm()

    template = loader.get_template('post_detail.html')

    context = {
        'post': post,
        'favorited': favorited,
        'profile': profile,
        'form': form,
        'comments': comments,
    }

    return HttpResponse(template.render(context, request))


@login_required
def tags(requst, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags=tag).order_by('-posted')
    template = loader.get_template('tag.html')
    context = {
        'posts': posts,
        'tag': tag,
    }

    return HttpResponse(template.render(context, requst))


@login_required
def like(requst, post_id):
    user = requst.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes

    liked = Likes.objects.filter(user=user, post=post).count()
    if not liked:
        like = Likes.objects.create(user=user, post=post)
        # like.save()
        current_likes = current_likes + 1

    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1

    post.likes = current_likes
    post.save()

    return HttpResponseRedirect(reverse('postdetails', args=[post_id]))


@login_required
def likeIn(requst, post_id):
    user = requst.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes

    liked = Likes.objects.filter(user=user, post=post).count()
    if not liked:
        like = Likes.objects.create(user=user, post=post)
        current_likes = current_likes + 1

    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1

    post.likes = current_likes
    post.save()

    return redirect('index')


@login_required
def favorite(requst, post_id):
    user = requst.user
    post = Post.objects.get(id=post_id)
    profile = Profile.objects.get(user=user)

    if profile.favorites.filter(id=post_id).exists():
        profile.favorites.remove(post)

    else:
        profile.favorites.add(post)

    return HttpResponseRedirect(reverse('postdetails', args=[post_id]))


@login_required
def favoriteIn(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    profile = Profile.objects.get(user=user)

    if profile.favorites.filter(id=post_id).exists():
        profile.favorites.remove(post)


    else:
        profile.favorites.add(post)

    return redirect('index')

# @login_required
# def explore(request):
#     users = Profile.objects.all()
#     posts = Post.objects.all()
#
#     context = {
#         'users': users,
#         'posts': posts,
#     }
#     template = loader.get_template('explore.html')
#     HttpResponse(template.render(context, request))
