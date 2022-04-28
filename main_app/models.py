from django.db import models
from django.urls import reverse

LOCATION = (
    ('U', 'Upstairs Media Room'),
    ('D', 'Downstairs Living Room'),
    ('B', 'Borrowed')
)

class Snack(models.Model):
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=100)

class Movie(models.Model):  # Note that parents are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    genre =  models.CharField(max_length=100)
    location =  models.CharField(
        max_length=1,
        choices=LOCATION,
        default=LOCATION[0][0],
        )
    series = models.CharField(max_length=100)
    stock = models.IntegerField()
    snacks = models.ManyToManyField(Snack)

    def __str__(self):
        return f"Movie: {self.name}. ID: {self.id}."
    
    def get_absolute_url(self):

        return reverse('detail', kwargs={'movie_id': self.id})

STATUS = (
    ('O', 'Outstanding'),
    ('L', 'Late'),
    ('R', 'Returned'),
    ('D', 'Damaged'),
    ('V', 'Resolved'),
)

class Rental(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('rental date')
    returned = models.CharField(
        max_length=1,
        choices=STATUS,
        default=STATUS[0][0]
    )

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"Renter Name: {self.name}. ID: {self.id}."
    
    class Meta:
        ordering = ['-date']

# class Person(models.Model):
#     name = models.CharField(max_length=50)
#     phone = models.IntegerField()
#     rentals = models.ManyToManyField(Rental)
    
#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('people_detail', kwargs={'pk': self.id})


        
# class Borrowers (for a many to many maybe?)