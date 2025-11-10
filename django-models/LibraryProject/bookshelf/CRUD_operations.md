> [!IMPORTANT]
> This markdown contains all the code as required by task Two where Django models are being implemented.

## Import the model
>>> from bookshelf.models import Book

## Create an instance of the model
>>> book_two = Book(title="1984", author="George Orwell", publication_year=1949)

## Save the created instance into the database
>>> book_two.save()

## Check all the instances of the model
>>> Book.objects.all()

## Retrieve a specific instance from the database
>>> book_two = Book.objects.get(pk=2)

## Update the title field of the instance
>>> book_two.title = "Nineteen Eighty-Four"

## Save the updates into the database to make them persistent
>>> book_two.save()

## Retrieve the database records to confirm they are updated
>>> Book.objects.get(pk=2)
