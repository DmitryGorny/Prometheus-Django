from django.shortcuts import render

from DjangoPrometheus.models import Article


def main(request):
    articles = Article.objects.exclude(is_draft=True)
    print(articles)
    return render(request, 'main.html', {'articles': articles})


def article(request, pk):
    article = Article.objects.get(pk=pk)

    args = {
        'author': article.author,
        'header': article.header,
        'text': article.text,
        'created_at': article.created_at
    }

    return render(request, 'article.html', {'article': article})

