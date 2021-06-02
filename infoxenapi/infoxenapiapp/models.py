from django.db import models

# Create your models here.
'''Create API(GET, POST) in Django REST Framework for saving and retrieving the latest verified sources of leads for oxygen cylinders in Delhi.
Fields:- Address, Business Name, Person Name (optional), Contact, Verified Status, TimeStamp
Please make sure that the latest and verified leads are prioritized with pagination.
Please push the codes to Github and share the git url.
1. Write a program to flatten the nested list.
Input:- [1, [2, 3, [4, 5, 6], [ 7, [ 8, 9, [10, 11], 12] ]]]
Output:- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

class OxygenCylinder(models.Model):
    Address = models.CharField(max_length=255,blank=False,null=False)
    Business_Name = models.CharField(max_length=255,blank=False,null=False)
    Person_Name = models.CharField(max_length=255)
    Contact = models.CharField(max_length=13,null=False,blank=False)
    Verified_Status = models.BooleanField(default=False)
    TimeStamp = models.DateTimeField(auto_now_add=True)
