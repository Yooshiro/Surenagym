from django.db import models

# Create your models here.
    
class Akhbar(models.Model):
    title=models.CharField(max_length=50,verbose_name="عنوان خبر")
    thumbnail=models.ImageField(verbose_name="تامنیل خبر",help_text="عکس با فرمت PNG و در اندازه 415 * 291 پیکسل باشد")
    thumbnail_2=models.ImageField(verbose_name="تامنیل خبر 2",help_text="عکس با فرمت PNG و در اندازه 415 * 291 پیکسل باشد",null=True,blank=True)
    mini_thumbnail=models.ImageField(verbose_name="تامنیل کوچک خبر",help_text="عکس با فرمت PNG و در اندازه 90 * 86 پیکسل باشد")
    short_text=models.CharField(max_length=4000,verbose_name="متن کوتاه",help_text="توضیح کوتاه در مورد خبر")
    day=models.IntegerField(default=1,verbose_name="روز")
    month=models.CharField(max_length=15,default="مرداد",verbose_name="ماه")
    year=models.IntegerField(default=1403,verbose_name="سال")
    text_1=models.CharField(max_length=4000,null=True,blank=True,verbose_name="متن خبر 1")
    text_2=models.CharField(max_length=4000,null=True,blank=True,verbose_name="متن خبر 2")
    text_3=models.CharField(max_length=4000,null=True,blank=True,verbose_name="متن خبر 3")
    text_4=models.CharField(max_length=4000,null=True,blank=True,verbose_name="متن خبر 4")
    image=models.ImageField(verbose_name="عکس مرتبط با خبر",help_text="عکس با فرمت PNG و در اندازه 960 در 504 پیکسل باشد",null=True,blank=True)
    safhe_khabar=models.CharField(max_length=15,editable=True,null=True,verbose_name="صفحه خبر")

    def __str__(self):
        return self.title
    
class Info(models.Model):
    phone_number=models.IntegerField(verbose_name="تلفن همراه")
    email=models.EmailField(verbose_name="ایمیل")
    telegram_id=models.CharField(verbose_name="آیدی تلگرام",max_length=60)
    instagram_id=models.CharField(verbose_name="آیدی اینستاگرام",max_length=60)
    twitter_id=models.CharField(verbose_name="آیدی توییتر",max_length=60)
    logo=models.ImageField(verbose_name="لوگو",help_text="لوگوی مخصوص سایت")
    instagram_image_1=models.ImageField(null=True,blank=True,help_text="عکس با فرمت PNG و در اندازه 162 در 162 پیکسل باشد")
    instagram_image_2=models.ImageField(null=True,blank=True,help_text="عکس با فرمت PNG و در اندازه 162 در 162 پیکسل باشد")
    instagram_image_3=models.ImageField(null=True,blank=True,help_text="عکس با فرمت PNG و در اندازه 162 در 162 پیکسل باشد")
    instagram_image_4=models.ImageField(null=True,blank=True,help_text="عکس با فرمت PNG و در اندازه 162 در 162 پیکسل باشد")
    instagram_image_5=models.ImageField(null=True,blank=True,help_text="عکس با فرمت PNG و در اندازه 162 در 162 پیکسل باشد")
    instagram_image_6=models.ImageField(null=True,blank=True,help_text="عکس با فرمت PNG و در اندازه 162 در 162 پیکسل باشد")
    header_address=models.CharField(verbose_name="آدرس بالای صفحه",max_length=100,null=True,blank=True)
    footer_address=models.CharField(verbose_name="آدرس پایین صفحه",max_length=120,null=True,blank=True)

    def __str__(self):
        return self.telegram_id
    
class Shahrie_1(models.Model):
    title=models.CharField(max_length=30,verbose_name="عنوان")
    price=models.CharField(max_length=30,verbose_name="شهریه")

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name=models.CharField(max_length=50,verbose_name="نام")
    email=models.EmailField(max_length=70,verbose_name="ایمیل")
    phone_number=models.CharField(max_length=15,verbose_name="شماره تلفن")
    title=models.CharField(max_length=50,verbose_name="عنوان")
    message=models.TextField(verbose_name="متن پیام")

    def __str__(self):
        return self.title