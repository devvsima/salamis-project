from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from .models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    result = (
        Products.objects.annotate(rank=SearchRank(vector=vector, query=query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )  # выводит по мере схожести товара

    result = result
