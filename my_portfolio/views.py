from django.http import FileResponse
from django.shortcuts import render

from .models import Experiance, Study, Portfolio, PortfolioCategory
from account.models import OwnerInfo, SocialLink
from blog.models import Post
# Create your views here.

# def home2(request):
#     owner_info = OwnerInfo.objects.all().last()
#     education = Study.objects.all()
#     portfolio_categories = PortfolioCategory.objects.all()
#     portfolo = Portfolio.objects.all()
#     experience = Experiance.objects.all()
#     social_links = SocialLink.objects.all()
#     print(social_links)

#     context = {
#         'owner_info': owner_info,
#         'education': education,
#         'portfolio_category': portfolio_categories,
#         'portfolio': portfolo,
#         'experience': experience,
#         'social_links': social_links,
#     }
#     return render(request, 'html/index.html', context)


def home1(request):
    try:
        owner_info = OwnerInfo.objects.all().last()
    except:
        owner_info=None
    education = list(Study.objects.all().order_by('-created_at'))
    portfolio_categories = PortfolioCategory.objects.all()
    portfolio = Portfolio.objects.all()
    experience = list(Experiance.objects.all().order_by('-created_at'))
    posts = list(Post.objects.all().order_by('-created_at'))
    if len(posts) > 3:
        posts = posts[-3:]
    social_links = SocialLink.objects.all()

    context = {
        'owner_info': owner_info,
        'education': education,
        'portfolio_category': portfolio_categories,
        'portfolio': portfolio,
        'experience': experience,
        'posts': posts,
        'social_links': social_links,
    }
    return render(request, 'html/index_2.html', context)


def download_cv(request, pk):
    file = OwnerInfo.objects.get(id=pk).cv
    response = FileResponse(file)
    return response
