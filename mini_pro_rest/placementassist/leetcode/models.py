from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class Profile(models.Model):
#     email=models.EmailField(max_length=50)
#     username=models.CharField(max_length=30)
#     semester=models.CharField(max_length=30)
    
#     def __str__(self):
#         return self.username




# Create your models here.
# class User(AbstractUser):
#     name = models.CharField(max_length=255)
#     rollno=models.CharField(max_length=255,primary_key=True)
#     email = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     username = None

#     USERNAME_FIELD = 'rollno'
#     REQUIRED_FIELDS = []
    
# # class Profile(models.Model):
# #     username = models.CharField(max_length=30, primary_key=True)
# #     email = models.EmailField(max_length=50)
# #     semester = models.CharField(max_length=30)

# #     def __str__(self):
# #         return self.username 
    
# class Results(models.Model):
#     testname=models.CharField(max_length=30)
#     oops=models.IntegerField()
#     dbms=models.IntegerField()
#     cn=models.IntegerField()
#     os=models.IntegerField()
#     profile_username=models.ForeignKey(User,on_delete=models.CASCADE,related_name="results")
#     created=models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.testname


class User(AbstractUser):
    username = models.CharField(max_length=255, primary_key=True)
    rollno = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

    #USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Results(models.Model):
    testname = models.CharField(max_length=30)
    oops = models.IntegerField()
    dbms = models.IntegerField()
    cn = models.IntegerField()
    os = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="results")
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.testname
