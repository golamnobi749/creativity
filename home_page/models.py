from django.db import models
from django.contrib.auth.models import User
# Create your models here.



# Create your models here.
STATUS_CHOICES = (
    ('TS', 'tshirt'),
    ('JP','jeans pants'),
    ('BS', 'boys shirt'),
    ('LE','lehenga'),
    ('BO','borkha'),
    ('WD','winter dress'),
    ('PH','phone'),
    ('LP','laptop'),
    ('EL','electic'),
    ('JF','just for'),
                  )
class Product(models.Model):
    title = models.CharField(max_length=255)
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    courrent_price = models.DecimalField(max_digits=6,decimal_places=2)
    meta_title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    category = models.CharField( choices=STATUS_CHOICES,max_length=16)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product/images/', null=True)

    
    def __str__(self):
        return str(self.id)
ADDRESS_CHOICES =(
    ("dhaka", "dhaka"),
    ("Rajshahi", "Rajshahi"),
("chittagong","Chittagong"),
('khulna','khulna'),
("Sylhet","Sylhet"),
('pabna','pabna'),

)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(choices = ADDRESS_CHOICES, max_length=100)
    house_building = models.CharField(max_length=30)
    zipcode = models.IntegerField()
def __str__(self):
    return str(self.id)

class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=9,decimal_places=2)
    def __str__(self):
     return str(self.id)
STATUS_CHOICES=(
    ('Pending','Pending'),
    ('Out for Delivery','Out For Delivery'),
    ('Delivered','Delivered'),
    ("Cancelled","Cancelled"),
    ("Completed","Completed"),
    ("Processing","Processing")

)
class OrderPlace(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=16 , choices=STATUS_CHOICES)
    quantity = models.PositiveIntegerField(default=1)
    location = models.CharField(max_length=16)
    order_date = models.DateTimeField(auto_now_add=True)


    







