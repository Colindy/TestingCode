from name_function import get_formatted_name

print("Please enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a first name: ")
    if last == 'q':
        break
    middle = input ("\nPlease give me a middle name.  If you have no middle name, simply hit ENTER: ")
    if middle == 'q':
        break
    
    
    formatted_name = get_formatted_name(first, last, middle)
    print(f"\tNealtly formatted name: {formatted_name}.")
