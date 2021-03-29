#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# import pandas as pd
# from store.models import Book

# def importBook():
#     bookTable = pd.read_csv('bookTable.txt')
#
#     for i in range(4):
#         row = bookTable.iloc[i]
#         # print(row[bookTable.columns[1]])
#
#         addDB = Book(bookid=row[bookTable.columns[0]], title=row[bookTable.columns[1]], isbn=row[bookTable.columns[2]]
#                      , author=row[bookTable.columns[3]], category=row[bookTable.columns[4]],
#                      description=row[bookTable.columns[5]], cover_picture=row[bookTable.columns[6]],
#                      year=row[bookTable.columns[7]], buy_price=row[bookTable.columns[8]],
#                      sell_price=row[bookTable.columns[9]], edition=row[bookTable.columns[10]],
#                      quantity=row[bookTable.columns[11]], rating=row[bookTable.columns[12]],
#                      publisher=row[bookTable.columns[13]], minimum_threshold=row[bookTable.columns[14]]
#                      )
#         addDB.save()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_bookstore.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)



if __name__ == '__main__':
    main()
