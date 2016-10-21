from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User


from .models import Post
from .forms import PostForm

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	
	allPost = post.count()
	cutNum = 4
	pageNum = 3

	if allPost%cutNum > 0 :
		lastNum = round(allPost/cutNum+0.5)
	else lastNum = allPost/cutNum

	# showPost = posts[x] for x in range(lastNum)
	showPost = []

	for x in range(lastNum):
		showPost.appand(posts[x])


	return render(request, 'board/post_list.html', {'posts':showPost})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'board/post_detail.html', {'post':post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			if request.user:
				# post.author = User.objects.create_user('anonymous'+str(User.objects.all().count()), 'aa@aa.com', '1234')
				post.author = User.objects.get(username='anonymous')

			else:
				post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('board.views.post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'board/post_edit.html', {'form':form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.author = User.objects.get(username='anonymous')
            post.published_date = timezone.now()
            post.save()
            return redirect('board.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'board/post_edit.html', {'form': form})


def post_delete(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()

	return redirect('board.views.post_list')



