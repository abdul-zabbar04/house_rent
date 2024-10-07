from rest_framework import serializers
from posts.models import PostModel, ReviewModel
from filterings.models import Category, District

class PostSerializer(serializers.ModelSerializer):
    category= serializers.SlugRelatedField(many= True, slug_field='slug', queryset= Category.objects.all())
    district= serializers.SlugRelatedField(many= False, slug_field='slug', queryset= District.objects.all())
    class Meta:
        model= PostModel
        # fields= ['id', 'on_created', 'on_updated', 'title', 'bedrooms', 'bathrooms', 'balcony', 'floor_number', 'additional_information', 'image', 'category', 'owner', 'available_from', 'rent', 'district', 'area']
        fields= '__all__'
        read_only_fields=['owner', 'on_created', 'on_updated', 'is_published', 'is_order', 'is_accepted']

    def create(self, validated_data):
        validated_data['owner'] =  self.context['request'].user
        return super().create(validated_data)
           

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= ReviewModel
        fields= ['name', 'user_full_name', 'created_on', 'rating', 'body']
        read_only_fields=['name', 'user_full_name', 'created_on']