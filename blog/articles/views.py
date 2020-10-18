from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from secrets import token_urlsafe
import json
from .forms import *


# Create your views here.

def home(request):
    # --- Get the Articles for the front-page ---
    recent_articles = Article.objects.all().order_by('-date')[1:4]
    main_article = Article.objects.order_by('-date').first()

    context = {
        "recent_articles": recent_articles,
        "main_article": main_article,
    }
    return render(request, 'articles/home.html', context)


@login_required
def add_article(request):
    if request.method == "POST":
        form = Add_Article_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {
                "form": Add_Article_Form(),
                "message": "Successfully Added Article"}
            return render(request,
                          'articles/add-article.html',
                          context)
        else:
            return render(request,
                          'articles/add-article.html',
                          {"form": Add_Article_Form()}
                          )
    else:
        form = Add_Article_Form()
        context = {
            'form': form
        }
        return render(request,
                      'articles/add-article.html',
                      context)


def all_articles(request):
    return render(request, 'articles/homev2.html')


def article_page(request, url):
    article = Article.objects.get(url=url)

    # Read content from the file
    f = article.content
    f.open('r')
    content = f.read()
    f.close()

    # Get all the comments
    comments = Comment.objects.filter(article=article).all()

    context = {
        "article": article,
        "content": content,
        "comments": comments
    }
    return render(request, 'articles/article-page.html', context)


@csrf_exempt
def add_subscriber(request):
    if request.method == "POST":
        try:
            # Get name and email from the post request
            data = json.loads(request.body)
            name = data['name']
            email = data['email']

            # Check to see if email is already taken
            try:
                email_exists = Subscriber.objects.get(email=email)
            except:
                email_exists = None
            if email_exists:
                raise Exception('Email is already subscribed')

            # Generate a subscriber ID (16 random alphanumeric)
            subscriber_id = token_urlsafe(16)
            # Create the subscriber
            subscriber = Subscriber(
                name=name,
                email=email,
                subscriber_id=subscriber_id
            )
            subscriber.save()

            response = {
                "message": "success"
            }
        except Exception as e:
            response = {
                "message": "error",
                "errorMessage": e.__str__(),
            }
        finally:
            return JsonResponse(response)
    else:
        return HttpResponse(404) #TODO: see if this works


def subscriber_preferences(request, subscriber_id):
    try:
        subscriber_obj = Subscriber.objects.get(subscriber_id=subscriber_id)
    except:
        subscriber_obj = None

    context = {
        'subscriber': subscriber_obj
    }
    return render(request, 'articles/subscriber_preferences.html', context)


@csrf_exempt
def subscriber_preferences_fetch(request):

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data['email']
            name = data['name']
            active = data['active']

            subscriber_obj = Subscriber.objects.get(email=email)
            subscriber_obj.name = name
            subscriber_obj.active = active
            subscriber_obj.save()

            response = {
                "message": "success"
            }

        except Exception as e:
            response = {
                "message": "error",
                "errorMessage": e.__str__()
            }
        finally:
            return JsonResponse(response)


