
from multiprocessing import context
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from .models import Post, Comment, Profile, Follow
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.generic import RedirectView
from .forms import RegForm,PostForm,UpdateUserProfileForm,UpdateUserForm,CommentForm
from .emails import send_email





def signup(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            f_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=f_password)
            send_email(username,user.email)
            login(request, user)
            return redirect('home')
    else:
        form = RegForm()
    return render(request, 'registration/signup.html', {'form': form})


def signin(request):
    pass



@login_required(login_url='login')
def signout(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def index(request):
    images = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    context = {
        'images': images,
        'form': form,
        'users': users,

    }
    return render(request, 'plata/index.html', context)



@login_required(login_url='login')
def profile(request, username):
    images = request.user.profile.posts.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateUserProfileForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'prof_form': profile_form,
        'images': images,

    }
    return render(request, 'plata/profile.html', context)


@login_required(login_url='login')
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_posts = user_prof.profile.posts.all()
    
    followers = Follow.objects.filter(followed=user_prof.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False
    context = {
        'user_prof': user_prof,
        'user_posts': user_posts,
        'followers': followers,
        'follow_status': follow_status
    }
    
    return render(request, 'plata/user_profile.html', context)


def unfollow(request, to_unfollow):
    if request.method == 'GET':
        user_profile2 = Profile.objects.get(pk=to_unfollow)
        unfollow_d = Follow.objects.filter(follower=request.user.profile, followed=user_profile2)
        unfollow_d.delete()
        return redirect('user_profile', user_profile2.user.username)


def follow(request, to_follow):
    if request.method == 'GET':
        user_profile3 = Profile.objects.get(pk=to_follow)
        follow_s = Follow(follower=request.user.profile, followed=user_profile3)
        follow_s.save()
        return redirect('user_profile', user_profile3.user.username)


@login_required(login_url='login')
def search_profile(request):
    
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        print(results)
        message = f'name'
        context = {
            'results': results,
            'message': message
        }
        return render(request, 'plata/results.html', context)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'plata/results.html', {'message': message})



@login_required(login_url='login')
def post_comment(request, id):
    image = get_object_or_404(Post, pk=id)
    is_liked = False
    if image.likes.filter(id=request.user.id).exists():
        is_liked = True
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            savecomment = form.save(commit=False)
            savecomment.post = image
            savecomment.user = request.user.profile
            savecomment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    context = {
        'image': image,
        'form': form,
        'is_liked': is_liked,
        'total_likes': image.total_likes()
    }
    return render(request, 'plata/single_post.html', context)



def like_post(request):
    # image = get_object_or_404(Post, id=request.POST.get('image_id'))
    image = get_object_or_404(Post, id=request.POST.get('id'))
    is_liked = False
    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)
        is_liked = False
    else:
        image.likes.add(request.user)
        is_liked = False

    context = {
        'image': image,
        'is_liked': is_liked,
        'total_likes': image.total_likes()
    }
    if request.is_ajax():
        html = render_to_string('plata/like.html', context, request=request)
        return JsonResponse({'form': html})

class PostLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        id = self.kwargs.get('id')
        print(id)
        obj = get_object_or_404(Post, pk=id)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user in obj.likes.all():
            obj.likes.remove(user)
        else:
            obj.likes.add(user)
        return url_


class PostLikeAPIToggle(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id=None, format=None):
        # id = self.kwargs.get('id')
        obj = get_object_or_404(Post, pk=id)
        url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        liked = False
        if user in obj.likes.all():
            liked = False
            obj.likes.remove(user)
        else:
            liked = True
            obj.likes.add(user)
        updated = True
        data = {

            'updated': updated,
            'liked': liked,
        }
    
        return Response(data)