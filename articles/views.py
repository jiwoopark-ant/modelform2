from django.shortcuts import render,redirect
from . models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    articles=Article.objects.all()

    context={
        'articles': articles,
    }

    return render(request,'index.html',context)


def detail(request,id):
    # 모든 경우
    #1.get: form만들어서 html문서 사용자에게 return
    #2. POST invalid date :데이터 검증에 실패한경우
    #3. POST valid date: 데이터 검증에 서옹한경우
    article=Article.objects.get(id=id)

    context={
        'article': article,
    }

    return render(request,'detail.html',context)


def create(request):
    
    if request.method =='POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',id=article.id)
        
        
    #사용자가 데이터를 입력할수 있도록 빈종이 리턴
    else:
        form=ArticleForm()

    context={
        'form': form,
    }

    return render(request,'create.html',context)

def delete(request,id):
    article= Article.objects.get(id=id)

    article.delete()

    return redirect('articles:index')

def update(request,id):
    article=Article.objects.get(id=id)

    #updayr
    if request.method=='POST':
        #articleform 역할은 html구성..?
        form=ArticleForm(request.POST,instance=article)

        if form.is_valid():
            form.save()
            return redirect('articles:detail',id=article.id)

    #edit create 빈종이와 비슷 다만 추가로 입력해놓은 기사 제목 내용이 들어가있는 빈종이
    else:
        form=ArticleForm(instance=article)

    context= {
        'form':form,
    }

    return render(request,'update.html',context)