from rest_framework.response import Response
from rest_framework import status
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from leetcode.models import User,Results
from leetcode.api.serializers import ResultsSerializer,UserSerializer


from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404



from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
import jwt, datetime
from rest_framework.permissions import IsAdminUser






# class ProfileViewSet(ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     lookup_field = 'username'

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# class LoginView(APIView):
#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']

#         user = User.objects.filter(username=username).first()

#         if user is None:
#             raise AuthenticationFailed('User not found!')

#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect password!')

#         payload = {
#             'id': user.username,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }

#         token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

#         data = {
#             'jwt': token
#         }
#         return Response(data)


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        refresh = RefreshToken.for_user(user)

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(data)


# class IsUserOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow users to edit their own profile data.
#     """

#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD, or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         # Write permissions are only allowed to the user who owns the profile.
#         return obj == request.user


# class UserView(APIView):
#     permission_classes = [IsAuthenticated, IsUserOrReadOnly]

#     def get(self, request):
#         if request.user.is_authenticated:
#             serializer = UserSerializer(request.user)
#             return Response(serializer.data)
#         else:
#             return Response({'message': 'User not authenticated!'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        user.auth_token.delete()
        return Response({'message': 'success'})



class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = get_object_or_404(User, username=request.user.username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request):
        user = get_object_or_404(User, username=request.user.username)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    
    def delete(self, request):
        user = get_object_or_404(User, username=request.user.username)
        user.delete()
        return Response(status=204)


class ResultsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class = ResultsSerializer
    queryset = Results.objects.all()
    
# class ProfileListAV(APIView):
    
#     def get(self,request):
#         profile=Profile.objects.all()
#         serializer=ProfileSerializer(profile,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
        
# class ProfileDetailAV(APIView):
    
#     def get(self,request,pk): 
#         try:
#             question=Profile.objects.get(pk=pk)
#         except Profile.DoesNotExist:
#             return Response({'Error': 'not found'},status=status.HTTP_404_NOT_FOUND)    
#         serializer=ProfileSerializer(question)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         question=Profile.objects.get(pk=pk)
#         serializer= ProfileSerializer(question,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
#     def delete(self,request,pk):
#         question=Profile.objects.get(pk=pk)
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
     
    

# class ResultListAV(APIView):
    
#     def get(self,request):
#         questions=Results.objects.all()
#         serializer=ResultsSerializer(questions,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=ResultsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
      
# class ResultDetailAV(APIView):  
    
#     def get(self,request,pk): 
#         try:
#             question=Results.objects.get(pk=pk)
#         except Results.DoesNotExist:
#             return Response({'Error': 'not found'},status=status.HTTP_404_NOT_FOUND)    
#         serializer=ResultsSerializer(question)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         question=Results.objects.get(pk=pk)
#         serializer= ResultsSerializer(question,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
#     def delete(self,request,pk):
#         question=Results.objects.get(pk=pk)
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
            

# @api_view(['GET','POST'])
# def question_list(request):
    
#     if request.method == 'GET':
    
#         questions=Questions.objects.all()
#         serializer=QuestionsSerializer(questions,many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer= QuestionsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        

# @api_view(['GET','PUT','DELETE'])
# def question_details(request,pk):
#     if request.method == 'GET':
#         try:
#             question=Questions.objects.get(pk=pk)
#         except Questions.DoesNotExist:
#             return Response({'Error': 'Question not found'},status=status.HTTP_404_NOT_FOUND)    
#         serializer=QuestionsSerializer(question)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         question=Questions.objects.get(pk=pk)
#         serializer= QuestionsSerializer(question,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
#     if request.method == "DELETE":
#         question=Questions.objects.get(pk=pk)
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
            
        
        
        
    
    