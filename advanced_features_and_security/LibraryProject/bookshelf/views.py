from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Article
from django.contrib.auth.decorators import permission_required
from .forms import ArticleForm

# Create your views here.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    data = list(Article.objects.values())
    return JsonResponse({"articles": data})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_article(request):
    title = request.GET.get("title")
    body = request.GET.get("body")
    article = Article.objects.create(title=title, body=body)
    return JsonResponse({"message": "Article created", "id": article.id})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.title = request.GET.get("title", article.title)
    article.body = request.GET.get("body", article.body)
    article.save()
    return JsonResponse({"message": "Article updated"})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_article(request, article_id):
    Article.objects.get(id=article_id).delete()
    return JsonResponse({"message": "Article deleted"})

def createArticle(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'form_example.html', {'form':form})