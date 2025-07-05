from django.urls import path

from book import views

urlpatterns = [
    path('', views.SelectBooksView.as_view(), name="SelectAllBooks"),
    path('<int:pk>', views.SelectBooksView.as_view(), name="SelectOneBook"),
    path('add', views.AddBookView.as_view(), name="AddBooks"),
    path('delete/<int:pk>', views.DeleteBookView.as_view(), name="DeleteBook")

]