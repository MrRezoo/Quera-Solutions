from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from app.models import Movie, Seat, Ticket


def list_movies(request):
    return render(request, 'app/movies.html', {
        'movies': Movie.objects.all()
    })


def list_seats(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.exclude(ticket__movie_id=movie_id)  # 2 query
    return render(request, 'app/seats.html', {
        'movie': movie,
        'seats': seats
    })


def reserve_seat(request, movie_id, seat_id):
    if not request.user.is_authenticated:
        next_url = reverse('list_seats', args=[movie_id])
        # redirect to login page with next url list_seats
        return redirect(reverse('login') + '?next=' + next_url)

    Ticket.objects.create(
        user_id=request.user.id,
        movie_id=movie_id,
        seat_id=seat_id
    )
    return redirect('list_seats', movie_id=movie_id)


def stats(request):
    from django.http import HttpResponseForbidden
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    stats = Ticket.objects.values('seat__number').annotate(total=Count('seat__number'))

    return JsonResponse(
        {"stats": list(stats)}
    )


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("list_movies")
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
