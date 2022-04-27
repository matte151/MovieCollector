from django.shortcuts import render, redirect

# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Movie
from .forms import RentalForm


# This is no longer needed once the models.py part is used.
# class Movie:  # Note that parents are optional if not inheriting from another class
#   def __init__(self, name, genre, location, series, stock):
#     self.name = name
#     self.genre = genre
#     self.location = location
#     self.series = series
#     self.stock = stock

# movies = [
#   Movie('Avengers', 'Action', 'Upstairs', 'Marvel', 1),
#   Movie('Spiderman', 'Action', 'Downstairs', 'Marvel', 1),
#   Movie('Stardust', 'Action', 'Matt Rented', '', 2)
# ]

class MovieCreate(CreateView):
  model = Movie
  fields = '__all__'

class MovieUpdate(UpdateView):
  model = Movie
  fields = ['genre', 'location', 'series','stock']

class MovieDelete(DeleteView):
  model = Movie
  success_url = '/movies/'

# Define the home view
def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def movies_index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', { 'movies': movies })

def movies_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  rental_form = RentalForm()
  return render(request, 'movies/detail.html', {'movie': movie, 'rental_form': rental_form})

def add_rental(request, movie_id):
   # create a ModelForm instance using the data in request.POST
  form = RentalForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_rental = form.save(commit=False)
    new_rental.movie_id = movie_id
    new_rental.save()
  return redirect('detail', movie_id=movie_id)
