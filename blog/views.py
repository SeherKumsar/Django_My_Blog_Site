from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "machine-learning",
        "image": "machine-learning.png",
        "author": "Seher",
        "date": date(2023, 9, 28),
        "title": "Machine Learning",
        "excerpt": "Machine Learning: A Brief Introduction",
        "content": """
          Machine learning is a subfield of artificial intelligence that enables computers to automatically perform certain tasks by learning from data. 
          Thanks to machine learning, computers can quickly and effectively perform tasks that humans cannot do or that take too much time.

          The importance of machine learning is that it offers solutions to many problems we face today and makes our lives easier. 
          For example, smart assistants developed with machine learning can respond to our voice or written commands and 
          perform operations such as making an appointment, playing music, reading news. Image processing systems developed with machine learning can perform tasks such as face recognition, 
          license plate recognition, object recognition and can be used in areas such as security, health and education. 
          Natural language processing systems developed with machine learning have capabilities such as understanding, translating, summarizing and producing texts, 
          and can be used in areas such as communication, entertainment and education.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Seher",
        "date": date(2024, 3, 10),
        "title": "Why I Love Programming?",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Did you ever spend hours searching that one error in your code? 
          Yep - that's what happened to me yesterday, but I'm not complaining. 
          In fact, I love programming and I think it's one of the best skills you can have in this digital age. 
          Let me tell you why.

          First of all, programming is fun. It's like solving puzzles, but with endless possibilities and creativity. 
          You can make anything you want with code, from websites to games to apps to robots. 
          You can also express yourself through code, by choosing your own style, tools and languages. 
          Programming is a form of art, and you are the artist.
        """
    },
    {
        "slug": "algorithms",
        "image": "algorithm.png",
        "author": "Seher",
        "date": date(2023, 8, 5),
        "title": "What is Algorithm?",
        "excerpt": "An algorithm is a step-by-step design of a solution to solve a specific problem or achieve a specific goal.",
        "content": """
          What is an algorithm, you ask? Well, an algorithm is a set of instructions or rules that tells a computer how to solve a problem or perform a task. 
          For example, if you want to sort a list of numbers from smallest to largest, 
          you can use an algorithm that compares each pair of numbers and swaps them if they are in the wrong order. 
          This way, you can arrange the numbers in ascending order.

          Algorithms are everywhere in our daily lives. 
          When you use a search engine like Bing, you are using an algorithm that finds the most relevant web pages for your query. 
          When you use a GPS navigation system, you are using an algorithm that calculates the shortest route to your destination. 
          When you play a video game, you are using an algorithm that controls the behavior of the characters and the environment.

        """
    }
]

def get_date(post):
  return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date) # tüm post listesini sırala
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
      "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
      "post": identified_post
    })