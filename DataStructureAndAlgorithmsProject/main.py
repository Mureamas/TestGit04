from Sorting.BinarySearchTree import BinarySearchTree
from Sorting.TextProcessing import text_processing


# Function to print the Binary Search Tree visualization
def print_binary_search_tree():
    print("Binary Search Tree:")
    print("           15")
    print("        /     \\")
    print("       8        24")
    print("      / \\     /   \\")
    print("    4     11  19    28")
    print("   / \\    \\       /")
    print("  2   6     13     25")
    print("       \\   /")
    print("        7  12")


if __name__ == "__main__":
    while True:
        print("\nSelect a function:")
        print("1. Binary Search Tree")
        print("2. Text Processing")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Print the Binary Search Tree visualization
            print_binary_search_tree()

            # Create a Binary Search Tree
            bst = BinarySearchTree()
            # Insert some keys
            keys = [15, 8, 24, 4, 11, 19, 28, 2, 6, 13, 25, 7, 12]
            for key in keys:
                bst.insert_key(key)

            # Prompt the user to search for a key in the Binary Search Tree
            search_key = int(input("Enter a key to search for: "))
            result = bst.search_key(search_key)
            if result:
                print(f"Key {search_key} found in the tree.")
            else:
                print(f"Key {search_key} not found in the tree.")

        elif choice == "2":


            # Sample text for processing
            sample_text = "Text processing is an important part of natural processing language processing. " \
                          "It involves various techniques to analyze and manipulate text data."

            # Perform text processing
            result = text_processing(sample_text)

            # Print word frequency
            print("Word Frequency:")
            for word, freq in result.items():
                print(f"{word}: {freq}")

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")
