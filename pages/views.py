from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

from .models import Women
from .permissions import IsAdminOrReadOnly
from .serializers import WomenSerializer



class WomenPogination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10000




class WomenAPIViews(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = WomenPogination



class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )


class WomenAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )


#
# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer



# class WomenAPIView(APIView):
#
#     def get(self, request, pk=None):  # pk ni qabul qilish kerak
#         if pk is None:
#             women = Women.objects.all()
#             serializer = WomenSerializer(women, many=True)
#             return Response({'posts': serializer.data})
#         else:
#             woman = get_object_or_404(Women, pk=pk)
#             serializer = WomenSerializer(woman)
#             return Response({'post': serializer.data})
#
#
#     # def get(self, request):
#     #     w = Women.objects.all()
#     #     return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'posts': serializer.data})
#
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': "Method PUT not aallowed"})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': "Object does not exist "})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'posts': serializer.data})
#


    # def delete(self,request, *args, **kwargs):
    #     pk = kwargs.get('pk', None)
    #     if not pk:
    #         return Response({'error': "Method DELETE not aallowed"})
    #
    #     return Response({'posts': 'delete post' + str(pk)})









