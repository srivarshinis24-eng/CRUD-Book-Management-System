
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html',
                  {'books': books})

def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        Book.objects.create(
            title=title,
            author=author,
            price=price
        )
        return redirect('book_list')

    return render(request, 'book_form.html')

def book_update(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.price = request.POST.get('price')
        book.save()
        return redirect('book_list')

    return render(request, 'book_form.html',
                  {'book': book})

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()

    return redirect('book_list')


# Create your views here.
