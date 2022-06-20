from rest_framework.serializers import ModelSerializer
from blogapp.models.blog.blog import Blog

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'