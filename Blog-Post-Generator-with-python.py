# At first, Import "os" library & define BLOG_DIR as a variable.
import os
BLOG_DIR = "blogs"

# Save a blog post to a file.
def save_blog(title,content):
    if not os.path.exists(BLOG_DIR):
        os.makedirs(BLOG_DIR)
    filename = os.path.join(BLOG_DIR, f"{title}.txt")
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Blog '{title}' saved successfully!")

# View blogs.
def view_blogs():
    if not os.path.exists(BLOG_DIR) or not os.listdir(BLOG_DIR):
        print("No blogs found.")
        return
    print("\nAvailable blogs: ")
    for file in os.listdir(BLOG_DIR):
        print(f"- {file[:-4]}")

# Preview blogs.

def preview_blog(title):
    filename = os.path.join(BLOG_DIR, f"{title}.txt")
    try:
        with open(filename, 'r') as file:
            print("\n" + file.read())
    except FileNotFoundError:
        print("Blog not found.")        




# Main program.
def main():
    while True:
        print("\nBlog post Generator")
        print("1. Create blog")
        print("2. View blogs")
        print("3. Preview blog")
        print("4. Exit")
        choice = input("Please enter an option: ")
        if choice == '1':
            title = input("Please enter blog title: ")
            content = input("Please enter blog content: ")
            save_blog(title,content)
        elif choice == '2':
            view_blogs()
        elif choice == '3':
            title = input("Please enter blog title to preview:  ")
            preview_blog(title)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.Try again.")

# Run main dictionary.
if __name__ == "__main__":
    main()

