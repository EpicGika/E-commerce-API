from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from .filters import ProductsFilter
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def get_all_products(request):
    
    filterset = ProductsFilter(request.GET, queryset=Product.objects.all().order_by('name'))
    paginator = PageNumberPagination()
    paginator.page_size = 2
    count = filterset.qs.count()

    queryset = paginator.paginate_queryset(filterset.qs, request)
    serializer = ProductSerializer(queryset, many=True)
    context = {"products": serializer.data, "Number of products":count}
    return Response(context)


@api_view(['GET'])
def get_by_id_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, many=False)

    return Response({'product': serializer.data})
