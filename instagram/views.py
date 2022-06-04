from django.shortcuts import render

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

