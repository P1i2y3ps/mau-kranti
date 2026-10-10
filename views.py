
from django.shortcuts import render, get_object_or_404
from .models import Journalist, News, ContactMessage


def home(request):
    journalist = Journalist.objects.first()

    news_list = News.objects.all().order_by('-published_date')

    # Homepage News Slider
    slider_news = News.objects.all().order_by('-published_date')[:5]

    trending_news = News.objects.filter(
        is_trending=True
    ).order_by('-published_date')

    categories = (
        News.objects
        .exclude(category='')
        .values_list('category', flat=True)
        .distinct()
    )

    return render(request, 'news/home.html', {
        'journalist': journalist,
        'news_list': news_list,
        'slider_news': slider_news,
        'trending_news': trending_news,
        'categories': categories,
    })


def news_detail(request, id):
    news = get_object_or_404(News, id=id)

    return render(request, 'news/detail.html', {
        'news': news
    })


def videos(request):
    videos = News.objects.exclude(video='')

    return render(request, 'videos.html', {
        'videos': videos
    })


def about(request):
    return render(request, 'about.html')


def gallery(request):
    gallery = News.objects.exclude(
        image=''
    ).order_by('-published_date')

    return render(request, 'gallery.html', {
        'gallery': gallery
    })


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        return render(request, 'contact.html', {
            'success': 'आपका संदेश सफलतापूर्वक भेज दिया गया है।'
        })

    return render(request, 'contact.html')


def categories(request):
    categories = (
        News.objects
        .exclude(category='')
        .values_list('category', flat=True)
        .distinct()
    )

    selected_category = request.GET.get('category')

    if selected_category:
        category_news = News.objects.filter(
            category=selected_category
        ).order_by('-published_date')
    else:
        category_news = News.objects.none()

    return render(request, 'categories.html', {
        'categories': categories,
        'category_news': category_news,
        'selected_category': selected_category,
    })