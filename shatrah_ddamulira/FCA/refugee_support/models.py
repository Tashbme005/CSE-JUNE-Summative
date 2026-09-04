from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Refugee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50,  blank=False, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=50, blank=False, validators=[MinLengthValidator(2)])
    date_of_birth = models.DateField(blank=False)
    place_of_birth = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], blank=False)
    nationality = models.CharField(max_length=50, blank=False, choices=[('Ugandan', 'Ugandan'), ('Kenyan', 'Kenyan'), ('Tanzanian', 'Tanzanian'), ('Burundian', 'Burundian'), ('Rwandanese', 'Rwandanese'), ('Somali', 'Somali'),('South Sudanese', 'South Sudanese')])
    marital_status = models.CharField(max_length=20, choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), ('Windowed', 'Windowed')], blank=False)
    settlement_camp = models.CharField(max_length=100, blank=False, choices=[('Gulu settlement camp', 'Gulu settlement camp'), ('Arua settlement camp', 'Arua settlement camp'), ('Mbarara settlement camp', 'Mbarara settlement camp'), ('Kasese settlement camp', 'Kasese settlement camp'), ('Busia settlement camp', 'Busia settlement camp'), ('Mbale settlement camp', 'Mbale settlement camp'), ('Kigezi settlement camp', 'Kigezi settlement camp')])
    date_of_joining_settlement_camp = models.DateField(blank=False)
    