from app import archon_description
import textwrap

def run():
    while True:
        archon_name = input("Enter the Archon's name:").lower()

        if archon_name == 'exit':
            break

        description = archon_description(archon_name)

        # Set the maximum width for wrapping the description
        console_width = 80

        # Use textwrap to wrap the description text
        wrapped_description = textwrap.fill(description, width=console_width)

        print("\n" + wrapped_description + "\n")

if __name__ == "__main__":
    run()
