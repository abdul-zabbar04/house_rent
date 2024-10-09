from rest_framework import serializers
from posts.models import PostModel, ReviewModel
from filterings.models import Category, District

class PostSerializer(serializers.ModelSerializer):
    category= serializers.SlugRelatedField(many= True, slug_field='slug', queryset= Category.objects.all())
    district= serializers.SlugRelatedField(many= False, slug_field='slug', queryset= District.objects.all())
    image_url = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model= PostModel
        fields= '__all__'
        read_only_fields=['owner', 'on_created', 'on_updated', 'is_published', 'is_order', 'is_accepted']

    def create(self, validated_data):
        image_url = validated_data.pop('image_url', None)
        validated_data['owner'] =  self.context['request'].user
        post = PostModel.objects.create(**validated_data)
        if image_url:
            post.image_url = image_url
            post.save()
        return post
           

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= ReviewModel
        fields= ['name', 'user_full_name', 'created_on', 'rating', 'body']
        read_only_fields=['name', 'user_full_name', 'created_on']