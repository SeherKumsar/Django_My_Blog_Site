# from datetime import date

from django.shortcuts import render, get_object_or_404

from .models import Post # dummy veriler yerine admin panelden çekilen veriler

# all_posts = [
    
# ]

# def get_date(post):
#   return post['date']

# Create your views here.


def starting_page(request):
    # Django negatif indekslemeyi desteklemediği için [-3:] kullanamayız
    latest_posts = Post.objects.all().order_by("-date")[:3] # Python daki tüm verileri sorgulayarak bulmak yerine bu şekilde tek seferde [:3] yaptığımızda sadece istenilen veriler hızlıca gelir
    # sorted_posts = sorted(all_posts, key=get_date) # tüm post listesini sırala
    # latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
      "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })


def post_detail(request, slug):
    # identified_post = next(post for post in all_posts if post['slug'] == slug)
    # identified_post = Post.objects.get(slug=slug)
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
      "post": identified_post,
      "post_tags": identified_post.tag.all()
    })

