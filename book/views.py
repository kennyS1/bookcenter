from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib import messages

# Create your views here.
def bookIndex(request):
    # 获取所有书籍记录
    books = Book.objects.all()
    return render(request, "bookIndex.html", {'books' : books})

def addBook(request):

    if request.method == "POST":
        # 接收表单数据
        bookName = request.POST.get("bookName")
        picture = request.FILES.get("picture")
        price = request.POST.get("price")
        info = request.POST.get("info")

        book = Book(
            bookName=bookName,
            picture=picture,
            price=price,
            info=info,
        )
        book.save()

        messages.success(request, '书籍添加成功！')

    return render(request, 'addbook.html')

def updateBook(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        bookName = request.POST.get("bookName")
        picture = request.FILES.get("picture")
        price = request.POST.get("price")
        info = request.POST.get("info")

        # 只更新发生变化的字段
        if bookName != book.bookName and bookName:
            book.bookName = bookName

        if picture:  # 只有上传了新图片才更新
            book.picture = picture

        if price:
            if price != book.price:
                book.price = price

        if info and info != book.info:
            book.info = info


        # 修改后重新save一次
        book.save()

        messages.success(request, '书籍信息修改成功！')

    return render(request, 'bookUpdate.html', {
        'book': book,
        'book_id': book_id  # 传递 book_id
    })

def deleteBook(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        messages.success(request, '书籍删除成功！')
        return redirect('bookIndex')
    return redirect('bookIndex')





