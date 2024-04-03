from queue import LifoQueue
backward_history = LifoQueue()   #backward and forward history for the navigation of history
forward_history = LifoQueue()
current_page = None   # None indicates theres nothing in the current page

#visit functions
NoOfVisits = int(input("enter the number of url history: "))

print("Enter the URLs to visit: ")
for i in range(NoOfVisits):
    url = input("URL: ")
    print(f"visiting {url} ")
    backward_history.put(current_page)
    current_page = url

#dsplay current page
print(f"current page: {current_page}")

#Go back
while input("Do you want to go back? (yes/no): ").lower() == 'yes':
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"Going back to {current_page}")
    else:
        print("No prevous page avialabe.")

#Go forward
while input("Do you want to go forward? (yes/no): ").lower() == 'yes':
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f'Going forward to {current_page}')
    else:
        print('No forward page avialabe.')
        