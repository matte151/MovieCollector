from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Movie:  # Note that parents are optional if not inheriting from another class
  def __init__(self, name, genre, location, series, days_rented):
    self.name = name
    self.genre = genre
    self.location = location
    self.series = series
    self.days_rented = days_rented

movies = [
  Movie('Avengers', 'Action', 'Upstairs', 'Marvel', 0),
  Movie('Spiderman', 'Action', 'Downstairs', 'Marvel', 0),
  Movie('Stardust', 'Action', 'Matt Rented', '', 4)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Movie Goer!</h1>')

def about(request):
    return render(request, 'about.html')

def movies_index(request):
  return render(request, 'movies/index.html', { 'movies': movies })