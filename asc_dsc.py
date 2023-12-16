num_seq = input("Enter the numbers: ")
print("For ascending and descending order type 'asc' & 'desc' respectively")
choice = input("Give your choice: ")

num_list = list(map(float, num_seq.split()))

if choice == "asc":
    num_list.sort()
    print(num_list)
elif choice == "desc":
    num_list.sort(reverse=True)
    print(num_list)
else:
    print("Invalid choice")