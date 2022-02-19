from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=255, unique=True)
#     phone_number = models.IntegerField(max_length=10) #TODO: validate phone number here
#     password = models.CharField(max_length=200, validators=[MinLengthValidator(8)])
#     user_type = models.CharField(max_length=50)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     #FIXME: Error here while defining User model
#     manager_id = models.ForeignKey(self, on_delete=models.CASCADE)
#     created_at = models.DateTimeField('Joined At',auto_now_add=True)

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name
    
# class Leads(models.Model):
#     name = models.CharField(max_length=255)
#     email_address = models.EmailField(max_length=255, unique=True)
#     #FIXME: validate phone number here
#     phone_number = models.IntegerField(max_length=10) 
#     created_at = models.DateTimeField('Created At',auto_now_add=True)
#     state = models.CharField(max_length=8)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Remarks(models.Model):
#     created_at = models.DateTimeField('Created At',auto_now_add=True)
#     remark = models.CharField(max_length=1023)
#     user_id = models.ForeignKey(User, on_delete=models.SET_NULL)
#     lead_id = models.ForeignKey(Leads, on_delete=models.SET_NULL)

#     def __str__(self):
#         remark =  self.created_at.strftime("%Y-%m-%d %H:%M:%S")+ ' : ' + self.user_id.first_name + ' to '+ self.lead_id.name
#         return remark


