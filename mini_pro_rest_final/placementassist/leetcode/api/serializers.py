from leetcode.models import Results,User

from rest_framework import serializers



class ResultsSerializer(serializers.ModelSerializer):
    
    #leng_name = serializers.SerializerMethodField()
    
    class Meta:
        model= Results
        fields="__all__"
  
class UserSerializer(serializers.ModelSerializer):
    results = ResultsSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['username','rollno' ,'email', 'password','results']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
  
# class ProfileSerializer(serializers.ModelSerializer):
#     results = ResultsSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = Profile
#         fields = ('username','email', 'semester', 'results')
#         extra_kwargs = {
#             'url': {'view_name': 'profile-detail', 'lookup_field': 'username'}
#         } 
        
#     def validate_username(self, value):
#         """
#         Check if the username already exists in the database
#         """
#         if self.instance:  # allow updating the existing instance
#             return value
#         if Profile.objects.filter(username=value).exists():
#             raise serializers.ValidationError('username already exists')
#         return value   
        
# class ProfileSerializer(serializers.ModelSerializer):
    
#     results=ResultsSerializer(many=True,read_only=True)
    
#     class Meta:
#         model=Profile
#         fields="__all__"        
        # fields=['id','name','difficulty']
        # exclude = ['name']
        
    # def get_leng_name(self,object):
    #     return len(object.name)  
        
    # def validate(self,data):
    #      if data["name"]==data["difficulty"]:
    #          raise serializers.ValidationError("name and diff shoul not be same")
    #      else:
    #          return data
    # def validate_name(self,value):
    #     if len(value)<= 1:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value    
    

# def name_length(value):
#     if len(value)<=1:
#         raise serializers.ValidationError("short name")


# class QuestionsSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_length])
#     difficulty=serializers.CharField()
#     active=serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Questions.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name= validated_data.get('name',instance.name)
#         instance.difficulty= validated_data.get('difficulty',instance.difficulty)
#         instance.active= validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     def validate(self,data):
#         if data["name"]==data["difficulty"]:
#             raise serializers.ValidationError("name and diff shoul not be same")
#         else:
#             return data
#     # def validate_name(self,value):
#     #     if len(value)<= 1:
#     #         raise serializers.ValidationError("Name is too short")
#     #     else:
#     #         return value
        

    