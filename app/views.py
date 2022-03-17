from typing import List
from uuid import uuid4, UUID

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.car.car import Car

cars: List[Car] = [
    Car(id=uuid4(), model="Audi A6", speed=350, color="green"),
    Car(id=uuid4(), model="Camry", speed=240, color="red"),
    Car(id=uuid4(), model="Model Y", speed=350, color="yellow"),
    Car(id=uuid4(), model="Honda", speed=210, color="yellow"),
]


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", context={
        "cars": cars
    })


def delete(request: HttpRequest, id: str) -> HttpResponse:
    global cars
    cars = [car for car in cars if car.id != UUID(id)]
    return redirect("/")


def add_car(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        cars.append(
            Car(
                id=uuid4(),
                model=request.POST.get("model", ""),
                speed=request.POST.get("speed", ""),
                color=request.POST.get("color", ""),
            )
        )
    return redirect('/')