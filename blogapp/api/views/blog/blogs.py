from rest_framework.decorators import api_view
from rest_framework.response import Response
from blogapp.models.blog.blog import Blog
from blogapp.api.serializers.blog.blog import BlogSerializer

@api_view(['GET'])
def getBlogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data) 