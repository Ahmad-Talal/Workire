from django.db import models

# Create your models here.
class Company(models.Model):
    Name = models.CharField(max_length=100, null=True,unique=True)
    Location = models.CharField(max_length=100, null=True)
    WebSite = models.URLField(null=True)
    About = models.TextField(null=True)
    TeamSize = models.IntegerField(null=True)
    logo = models.ImageField(null= True,blank=True, default='default.jpg')
    Categories = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ['-id']



class Category(models.Model):
    Name = models.CharField(max_length=100,null=True,unique=True)
    Description = models.CharField(null=True,max_length=300)
    SEO_NAME = models.CharField(null=True,max_length=100)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ['-id']


class Job(models.Model):
    Position = models.TextField(null=True,blank=True)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True)
    AdvertiserName = models.CharField(max_length=100,null=True,blank=True)
    AdvertiserType = models.CharField(max_length=100,null=True,blank=True)
    SenderReference = models.TextField(null=True,blank=True)
    DisplayReference = models.TextField(null=True,blank=True)
    PostDate = models.DateTimeField(null=True,blank=True)
    Classification = models.TextField(null=True,blank=True)
    SubClassification = models.TextField(null=True,blank=True)
    Description = models.TextField(null=True,blank=True)
    Country = models.CharField(max_length=100,null=True,blank=True)
    Location = models.CharField(max_length=100,null=True,blank=True)
    Area = models.CharField(max_length=100,null=True,blank=True)
    PostalCode = models.TextField(null=True,blank=True)
    ApplicationURL = models.URLField(null=True,blank=True)
    DescriptionURL = models.URLField(null=True,blank=True)
    Language = models.TextField(null=True,blank=True)
    ContactName = models.TextField(null=True,blank=True)
    EmploymentType = models.TextField(null=True,blank=True)
    StartDate = models.DateTimeField(null=True,blank=True)
    Duration = models.TextField(null=True,blank=True)
    WorkHours = models.TextField(null=True,blank=True)
    SalaryCurrency = models.TextField(null=True,blank=True)
    SalaryMinimum = models.TextField(null=True,blank=True)
    SalaryMaximum = models.TextField(null=True,blank=True)
    SalaryPeriod = models.TextField(null=True,blank=True)
    SalaryAdditional = models.TextField(null=True,blank=True)
    JobSource = models.TextField(null=True,blank=True)
    JobSourceURL = models.URLField(null=True,blank=True)
    VideoLinkURL = models.URLField(null=True,blank=True)
    AdditionalClassification1 = models.TextField(null=True,blank=True)
    AdditionalClassification2 = models.TextField(null=True,blank=True)
    AdditionalClassification3 = models.TextField(null=True,blank=True)
    AdditionalClassification4 = models.TextField(null=True,blank=True)
    LogoURL = models.ImageField(null=True,default='default.jpg')
    JobType = models.TextField(null=True)

    def __str__(self):
        return self.Position

    class Meta:
        ordering = ['-id']


class Blog(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank=True)
    addDate = models.DateField(auto_now_add=True)
    BlogUrl = models.CharField(null=True,blank=True,max_length=100)
    Description = models.CharField(max_length=150,null=True,blank=True)
    KeyWord = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
