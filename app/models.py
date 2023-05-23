from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contact(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    subject=models.CharField(max_length=250)
    email=models.CharField(max_length=50)
    message=models.TextField()
    pic=models.ImageField(upload_to='img/',default="")

    class Meta:
        db_table="contact"

class featured(models.Model):
    BOOKTYPE=(
        ('New Arrival','New Arrival'),
        ('English','English'),
        ('Hindi','Hindi'),
        ('Punjabi','Punjabi'),
        ('Best Seller','Best Seller'),
        ('Featured','Featured'),
        ('Action','Action'),
        ('Adventure','Adventure'),
       )
    name=models.CharField(max_length=100)
    description=models.TextField()
    photo=models.ImageField(upload_to='featured/')
    mrp=models.FloatField()
    sellingprice=models.FloatField()
    author=models.CharField(max_length=100,default="")
    isbn=models.CharField(max_length=50,default="")
    no_of_pages=models.CharField(max_length=20,default="")
    publisher=models.CharField(max_length=100,default="")
    publishdate=models.CharField(max_length=20,default="")
    booktype=models.CharField(max_length=50,default="",blank=True,null=True,choices=BOOKTYPE)

    class Meta:
        db_table="featured"
    def __str__(self):
        return self.name

    

class arrivals(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    photo=models.ImageField(upload_to='arrivals/')
    mrp=models.FloatField()
    sellingprice=models.FloatField()
    author=models.CharField(max_length=100,default="")
    isbn=models.CharField(max_length=50,default="")
    no_of_pages=models.CharField(max_length=20,default="")
    publisher=models.CharField(max_length=100,default="")
    publishdate=models.CharField(max_length=20,default="")

    class Meta:
        db_table="arrivals"

class english(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    photo=models.ImageField(upload_to='english/')
    mrp=models.FloatField()
    sellingprice=models.FloatField()
    author=models.CharField(max_length=100,default="")
    isbn=models.CharField(max_length=50,default="")
    no_of_pages=models.CharField(max_length=20,default="")
    publisher=models.CharField(max_length=100,default="")
    publishdate=models.CharField(max_length=20,default="")

    class Meta:
        db_table="english"

class punjabi(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    photo=models.ImageField(upload_to='punjabi/')
    mrp=models.FloatField()
    sellingprice=models.FloatField()
    author=models.CharField(max_length=100,default="")
    isbn=models.CharField(max_length=50,default="")
    no_of_pages=models.CharField(max_length=20,default="")
    publisher=models.CharField(max_length=100,default="")
    publishdate=models.CharField(max_length=20,default="")

    class Meta:
        db_table="punjabi"

class hindi(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    photo=models.ImageField(upload_to='hindi/')
    mrp=models.FloatField()
    sellingprice=models.FloatField()
    author=models.CharField(max_length=100,default="")
    isbn=models.CharField(max_length=50,default="")
    no_of_pages=models.CharField(max_length=20,default="")
    publisher=models.CharField(max_length=100,default="")
    publishdate=models.CharField(max_length=20,default="")

    class Meta:
        db_table="hindi"

class faq(models.Model):
    question=models.TextField()
    answer=models.TextField()

    class Meta:
        db_table="faq"

class blog(models.Model):
    name=models.CharField(max_length=100,default="")
    photo=models.ImageField(upload_to='blog/',default="")
    description=models.TextField( default="")
    postby=models.CharField(max_length=100,default="")
    poston=models.CharField(max_length=100,default="")

    class Meta:
        db_table="blog"

class review(models.Model):
    Userid=models.ForeignKey(User,on_delete=models.CASCADE)
    featuredid=models.ForeignKey(featured, on_delete=models.CASCADE)
    feedback=models.CharField(max_length=500)
    rating=models.CharField(max_length=50)
    class Meta:
        db_table="review"

       