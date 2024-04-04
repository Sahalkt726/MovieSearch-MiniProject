from django.db import models


# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=255)
    release_date=models.DateField()
    description=models.TextField(max_length=1000)
    plot=models.TextField()
    poster=models.ImageField(upload_to='media')

    def __str__(self):
        return self.title
    

class Favourite(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title
    

