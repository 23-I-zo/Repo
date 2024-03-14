#Initialize an empty lists, sets and dictionary (List for title, set for authors and dictonary for both)
books_list = []
authors_set = set()
books_dic = {}

#Add books 
books_list.append("Python Programming") #append for list
authors_set.add("John Smith") #add for set
books_dic["Python Programming"] = "John Smith" 

books_list.append("Data Structures and Algorithms")
authors_set.add("Jane Doe")
books_dic["Data Structures and Algorithms"] = "Jane Doe"

books_list.append("Machine Learning Basics")
authors_set.add("Alice Johnson")
books_dic["Machine Learning Basics"] = "Alice Johnson"

#Search for the book
search_title = input("Enter the title of the book your searching: ")
if search_title in books_list:
    print(f"Book found! Author: {books_dic[search_title]}")
else:
    print("Book not found!")

#Display all books
print("List of Books:")
for book in books_list:
    print(book)

#Remove book
remove_title = input("Enter the title of the book to remove or else enter to skip: ")
if remove_title in books_list:
    remove_author = books_dic[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dic[remove_title]
    print("Book removed successfully!")
    print("Books available: ", books_list)

else:
    print("Book not found!")