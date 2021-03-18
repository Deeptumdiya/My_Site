from django.db import models

# Create your models here.
class Products(models.Model):
    """Create A Product model to add the products"""
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category',on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'uploads/products/')


    @staticmethod
    def get_product_by_id(category_id):
        """Get the products on the basis of product id"""
        if category_id:
            return Products.objects.filter(category = category_id)
        else:
            return Products.objects.all()


class Category(models.Model):
    """Define Category to filter the products on the basis of it"""
    name  =  models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    

class Customer(models.Model):
    """Create Customer model to login and signup for customer"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    
    def register(self):
        self.save()

    @staticmethod
    def getcustomer_by_email(email):
        try: 
            return Customer.objects.get(email = email)
        except:
            return False
    
            
    def isExists(self):
        if  Customer.objects.filter(email=self.email):
            return True
        return False