from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)  # Stores a person's first name
    last_name = models.CharField(max_length=50)   # Stores a person's last name
    bio = models.TextField(default="No bio!")     # Stores a longer text (default value if not filled)
    is_programmer = models.BooleanField(blank=True)  # True/False field
    date_of_birth = models.DateField()            # Stores a date (YYYY-MM-DD)
    number_of_cars = models.IntegerField(null=True)  # Can be left blank (null in DB)
    email = models.EmailField(null=False)         # Stores an email (must be filled)
    height = models.FloatField()                  # Decimal numbers (e.g., 1.75 meters)
    profile_picture = models.FileField(upload_to="profiles/")  # Upload path for files (optional)

    class Meta:
        ordering = ["id"]                         # Default sort order
        db_table = "PersonAsWeSaid"               # Custom database table name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BankAccount(models.Model):
    owner = models.OneToOneField(Person, on_delete=models.CASCADE)
    # If the Person is deleted, the BankAccount is deleted too.


class Friend(models.Model):
    person = models.ManyToManyField(Person)
    # Many friends can be linked to many people.
    # No on_delete needed for ManyToManyField.


class Painting(models.Model):
    painter = models.ForeignKey(Person, on_delete=models.CASCADE)
    # If the Person is deleted, the Painting is deleted too.


