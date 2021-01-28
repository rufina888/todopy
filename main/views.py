from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Book
from .models import ToDo
# Create your views here.
def homepage (request):
    return render (request, "index.html")

def test (request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def add (request):
    return render(request, "add.html")

def change (request):
    return render(request, "change.html")

def delete (request):
    return render(request, "delete.html")

def books (request):
    books_list=Book.objects.all()
    return render(request, "book.html", {"books_list": books_list})
def add_book(request):
    form=request.POST
    text=form["book_text"]
    subtitle=form["book.subtitles"]
    description=form["book.description"]
    price=form["book.price"]
    genre=form["book.genre"]
    author=form["book.author"]
    year=form["book.year"]
    book=Book(text=text, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year,)
    book.save()
    return redirect(books)
