from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image
class Skills(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='projects')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return f'{self.name} - {self.author.email}'

class Contacts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField()
    telegram = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedn = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.user.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    whois = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skills, related_name='skills')
    projects = models.ManyToManyField(Projects, related_name='projects')
    contacts = models.ManyToManyField(Contacts, related_name='contacts')
    internship = models.CharField(max_length=70)
    image = models.ImageField(default="default.png", upload_to="profile_pics")

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.width>300 or img.height>300:
            output = (300, 300)
            img.thumbnail(output)
            img.save(self.image.path)


    def __str__(self):
        return self.user.email


class JobApplying(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=100)
    requirements = models.TextField()
    company_info = models.TextField()
    contacts = models.ForeignKey(Contacts, on_delete=models.SET_DEFAULT, default='')
    opportunities = models.TextField()

    class Meta:
        verbose_name = 'Job Applying'
        verbose_name_plural = 'Job Applyings'

    def __str__(self):
        return self.user.email


class News(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpeg", upload_to="news_pics")

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.name
