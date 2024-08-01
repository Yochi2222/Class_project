from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Book

def book_list(request):
    """
    View function to display a list of books.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered book list template.

    Raises:
        None

    """

    # Retrieve all books from the database and order them by title
    book_list = Book.objects.all().order_by('title')

    # Create a paginator object to paginate the book list, showing 10 books per page
    paginator = Paginator(book_list, 10)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the books for the requested page
        books = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver the first page
        books = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page of results
        books = paginator.page(paginator.num_pages)

    # Render the book list template with the books as context data
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def search_books(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query) | \
                Book.objects.filter(author__icontains=query) | \
                Book.objects.filter(isbn__icontains=query)
    else:
        books = Book.objects.all()
    
    return render(request, 'book_list.html', {'books': books, 'query': query})

from django.shortcuts import render, redirect
from .models import Book

def add_book(request):
    if request.method == 'POST':
        # Retrieve the form data
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        publication_date = request.POST.get('publication_date')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        # Create a new book object
        book = Book(
            title=title,
            author=author,
            isbn=isbn,
            publication_date=publication_date,
            price=price,
            quantity=quantity
        )
        
        # Save the book object to the database
        book.save()
        
        # Redirect to the book detail page
        return redirect('book_detail', pk=book.pk)
    
    return render(request, 'add_book.html')