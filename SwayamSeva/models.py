from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, \
    PermissionsMixin, Permission
from django.utils.itercompat import is_iterable
from django.utils.translation import gettext_lazy as _
from .IndirectUseFiles.manager import UserManager
from django.core.validators import RegexValidator


class UserDetails(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='Aadhaar', max_length=12, primary_key=True)
    EMAIL = models.EmailField(verbose_name='Email', max_length=127)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    about = models.TextField(_('about'), max_length=500, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['EMAIL', 'first_name', 'last_name']
    EMAIL_FIELD = 'EMAIL'
    objects = UserManager()

    class META:
        db_table = 'User'

    def __str__(self):
        return self.username

    def has_perms(self, perm_list, obj=None):
        if not is_iterable(perm_list) or isinstance(perm_list, str):
            raise ValueError('perm_list must be an iterable of permissions.')
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_lable):
        return True


class Profile(models.Model):
    user = models.OneToOneField(UserDetails, related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')

    def __str__(self):
        return self.pro_user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


class CompleteUserDetails(models.Model):
    Sex = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    UDid = models.AutoField(primary_key=True)
    Aadhaar = models.OneToOneField('UserDetails', related_name='CUD_set', on_delete=models.CASCADE)
    F_name = models.CharField(max_length=50)
    M_name = models.CharField(max_length=50, null=True)
    L_name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=6, choices=Sex)
    DOB = models.DateField()
    Father_name = models.CharField(max_length=100)
    Mother_name = models.CharField(max_length=100)
    Address_L1 = models.CharField(max_length=50)
    Address_L2 = models.CharField(max_length=50, null=True)
    City = models.CharField(max_length=60)
    State = models.CharField(max_length=60)
    Pincode = models.IntegerField()
    Date_Submitted = models.DateTimeField(verbose_name='Date Submitted', auto_now_add=True)

    class Meta:
        db_table = 'CompleteUserDetails'


class Documents(models.Model):
    Did = models.AutoField(primary_key=True)
    Uid = models.OneToOneField('UserDetails', related_name='Doc_set', on_delete=models.CASCADE)
    Pan_no = models.CharField(max_length=15, null=True)
    BPL_no = models.CharField(max_length=15, null=True)
    Ration_no = models.CharField(max_length=15, null=True)
    Mobile_no = models.CharField(max_length=10, null=True)
    Voter_id = models.CharField(max_length=15, null=True)
    Electricity_bill = models.CharField(max_length=20, null=True)
    Bank_Acc_no = models.CharField(max_length=17, null=True)
    IFSC_Code = models.CharField(max_length=12, null=True)
    MICR_Code = models.CharField(max_length=15, null=True)
    Bank = models.CharField(max_length=30, null=True)
    Branch = models.CharField(max_length=30, null=True)
    Date_Submitted = models.DateTimeField(verbose_name='Date Submitted', auto_now_add=True)

    class Meta:
        db_table = 'Documents'


class Schemes(models.Model):
    status_choices = (
        ('Pending', 'Pending'),
        ('In Process', 'In Process'),
        ('Approved', 'Approved'))
    Sid = models.AutoField(primary_key=True)
    Scheme_Name = models.CharField(max_length=15)
    Aadhaar = models.ForeignKey('UserDetails', on_delete=models.CASCADE)
    Status = models.CharField(max_length=15, verbose_name='Status', choices=status_choices, default='Pending')
    Date_Applied = models.DateTimeField(verbose_name='Date Applied', auto_now_add=True)

    class Meta:
        unique_together = (('Scheme_Name', 'Aadhaar'),)
        db_table = 'Schemes'
