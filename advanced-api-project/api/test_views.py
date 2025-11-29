from django.test import TestCase
from .models import Book, Author
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Jurgen")
        
        self.book1 = Book.objects.create(title='Flask Introduction', publication_year=2022, author=self.author)
        self.book2 = Book.objects.create(title='Swift Introduction', publication_year=2020, author=self.author)
    
    # test list view
    def test_book_list_view(self):
        response = self.client.get(reverse("book-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "api/book_list.html")

        books = response.context["books"]
        self.assertEqual(list(books), [self.book1, self.book2])
    
    # test search functionality
    def test_list_view_search(self):
        response = self.client.get(reverse("book-list"), {"search": "Swift Introduction"})

        books = response.context["books"]
        self.assertEqual(list(books), [self.book2])
    
    # test ordering functionality
    def test_list_view_ordering(self):
        response = self.client.get(reverse("book-list"), {"order": "publication_year"})

        books = list(response.context["books"])
        self.assertEqual(books, [self.book2, self.book1])
    
    # test the detailView
    def test_book_detail_view(self):
        response = self.client.get(reverse("book-info", args=[self.book1.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "api/book_detail.html")

        book = response.context["book"]
        self.assertEqual(book, self.book1)
    
    # test the createview
    def test_book_create_view(self):
        response = self.client.post(reverse('book-create'), {
            "title": "Psychology 101",
            "publication_year": 2019,
            "author": self.author.id,
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.count(), 3)
        self.assertTrue(Book.objects.filter(title="Psychology 101").exists())
    
    # test the updateview
    def test_book_update_view(self):
        response = self.client.post(reverse("book-update", args=[self.book1.id]), {
            "title": "Flask API Python Introduction",
            "author": self.author.id,
        })

        self.assertEqual(response.status_code, 302)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Flask API Python Introduction")
    
    # test the deleteview
    def test_book_delete_view(self):
        response = self.client.post(reverse("book-delete", args=[self.book2.id]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())
    
    # test book retrieval
    # def test_book_retrieval(self):
    #     book = Book.objects.get(title="Flask Introduction")

    #     # assert the correct book has been returned
    #     self.assertEqual(book.title, "Flask Introduction")
    #     self.assertEqual(book.publication_year, 2022)
    #     self.assertEqual(book.author, self.author)
    
    # test book update logic
    # def test_book_update(self):
    #     pass
    
    # test book destroy logic
    # def test_Book_Destroy(self):
    #     pass
    
    # test book and author serializers

    # 