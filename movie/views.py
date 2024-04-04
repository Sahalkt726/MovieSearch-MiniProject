from django.shortcuts import render,redirect,get_object_or_404
from . models import Movie,Favourite
from django . contrib . auth import authenticate,login,logout
from . forms import LoginForm
from django.contrib.auth.decorators import login_required
from . forms import CustomUserCreationForm



# Create your views here.
def index(request):
    return render(request,'index.html')


@login_required(login_url='login')
def movie(request):
     movies=Movie.objects.all()
     return render(request,'movie.html',{'movies':movies})


def MovieDetail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'moviedetail.html', {'movie': movie})


def user_signup(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request,"signup.html",{'form':form})



def user_login(request):
    form=LoginForm(request.POST)
    if form.is_valid():
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('movie')
    else:
        form=LoginForm()
    return render(request,"login.html",{'form':form})



def user_logout(request):
    logout(request)
    return redirect ('login')



def favourites(request):
    fav=Favourite.objects.filter(user=request.user)
    return render(request,'favourites.html',{'fav':fav})




def add_to_favourites(request,pk):
     movie=get_object_or_404(Movie,pk=pk)
     if not Favourite.objects.filter(user=request.user,movie=movie).exists():
          Favourite.objects.create(user=request.user,movie=movie)
     return redirect('favourites')


def remove_from_favourites(request,pk):
     Favourite.objects.filter(user=request.user,movie__pk=pk).delete()
     return redirect('favourites')





def search_result(request):
    query = request.GET.get('q')

    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = []

    return render(request, 'searchresult.html', {'movies': movies, 'query': query})
