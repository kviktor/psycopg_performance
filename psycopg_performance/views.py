import random

from faker import Faker

from django.shortcuts import render, redirect

from .models import (
    Author,
    Book,
)


def generate(request):
    if request.method == "POST":
        quantity = int(request.POST.get("quantity") or 10)

        # generate 10 authors
        author_ids = []
        for _ in range(10):
            faker = Faker()
            first, last = faker.name().split(" ", 1)
            author = Author.objects.create(
                first_name=first,
                last_name=last,
                age=random.randint(18, 99),
                metadata={
                    "text": faker.text(),
                },
            )
            author_ids.append(author.id)

        for _ in range(quantity):
            faker = Faker()
            Book.objects.create(
                author_id=random.choice(author_ids),
                title=faker.text().split(" ", 6)[0],
                metadata={
                    "meta": faker.text(),
                },
            )

        return redirect("/")

    return render(request, "generate.html")


def index(request):
    books = Book.objects.order_by("-id")
    return render(request, "index.html", {"books": books})
