books = [30000, 50000, 100000]
with open("books.txt", "w") as f:
    total = 0
    for i, price in enumerate(books, start=1):
        f.write(f"Book {i}:{price}\n")
        total += price
    f.write(f"Tong:{total}")