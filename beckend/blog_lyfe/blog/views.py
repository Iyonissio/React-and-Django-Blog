from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView , RetrieveAPIView
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer

class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class BlogPostDestaqueView(ListAPIView):
    queryset = BlogPost.objects.all().filter(destaque=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class BlogPostCategoriaView(APIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format = None):
        data = self.request.data
        categoria = data['categoria']
        queryset = BlogPost.objects.order_by('-date_created').filter(categoria__iexact=categoria)

        serializer = BlogPostSerializer(queryset, many=True)

        return Response(serializer.data)

