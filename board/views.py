from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Post
from .forms import PostForm

# def post_list(request):
# 	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
# 	return render(request, 'board/post_list.html', {'posts':showPost, 'pages':showPage})

def main(request):
	return redirect('board.views.post_list', nowPage=1)

def post_list(request, nowPage):

	# 모든 포스트
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

	# 총 포스트 23개
	allPost = posts.count()

	# 현재페이지
	nowPage = int(nowPage)

	# 글 몇개씩 자를지
	cutNum = 16

	# 페이지 몇개씩 자를지
	pageCut = 5

	if allPost%cutNum > 0 :
		lastPageNum = round(allPost/cutNum+0.5)
	else: lastPageNum = int(allPost/cutNum)

	if nowPage > 2:
		startPageNum = nowPage-2
	else: startPageNum = 1

	print('startPageNum ======', startPageNum)
	print('lastPageNum ======', lastPageNum)

	showPost = []
	showPage = []

	if startPageNum <= lastPageNum-4:
		for x in range(pageCut):
		 	showPage.append(startPageNum+x)
	else:
		for x in range(pageCut):
			showPage.append((lastPageNum-4)+x)

	# 전체글수 - 마지막페이지 전 페이지까지의 글 ///// 마전페 ~ (전체글수 - 마전페글)

	if nowPage==lastPageNum:
		for x in range(allPost-cutNum*(lastPageNum-1)):
			showPost.append(posts[(cutNum*(nowPage-1))+x])
	else:
		for x in range(cutNum):
			showPost.append(posts[(cutNum*(nowPage-1))+x])

	print('showPage ====', showPage)
	print('showPost ====', showPost)

	return render(request, 'board/post_list.html', {'posts':showPost, 'pages':showPage, 'nowPage':nowPage})


def post_detail(request, pk, nowPage):
	post = get_object_or_404(Post, pk=pk)
	nowPage = int(nowPage)
	return render(request, 'board/post_detail.html', {'post':post, 'nowPage':nowPage})

def post_new(request, nowPage):
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
			return redirect('board.views.post_detail', pk=post.pk, nowPage=nowPage)
	else:
		form = PostForm()
	return render(request, 'board/post_edit.html', {'form':form, 'nowPage':nowPage})


def post_edit(request, pk, nowPage):
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
    return render(request, 'board/post_edit.html', {'form': form, 'nowPage':nowPage})


def post_delete(request, pk, nowPage):
	post = get_object_or_404(Post, pk=pk)
	post.delete()

	return redirect('board.views.post_list', nowPage=nowPage)

