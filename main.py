from __future__ import print_function, unicode_literals
from InquirerPy import prompt
import markdown
from rich.console import Console
from rich.progress import track
from rich import print
import time
from modules import ask_questions_for_project
from modules import questions_for_name_and_color

console = Console()

# Call the first function in modules.py
responses = questions_for_name_and_color()

# print a message formatting it with the response colour word in the chosen colour using rich
print(f"\n[{responses['color'].lower()}]{responses['name']}[/{responses['color'].lower()}] let's create a README file! 🚀\n")


# Call the second function in modules.py
answers = ask_questions_for_project()

# Create some variables
md_text = "New"
file_path = "./README.md"
                            
# Format the markdown content
markdown_string = f"""\
![Image of coding and computers](./special1.jpg)

# Project Title:

{answers['project_title']}

---

# **What is this project about?**

{answers['project_description']}

---

# **How do I install this project?:**

{answers['project_installation']}

---

# **How do I use this project?**

{answers['usage_information']}

---

# **Licence Type:**

{answers['license_type']}

---

# **Author name:**

{answers['author_name']}

---

# **Contact Details:**

{answers['contact_details']}

"""

# Use a try / except to write to the markdown file README.md and indicate if successful or not
try:
    with open(file_path, 'w') as file:
        file.write(markdown_string)

    # Generate a progress bar using rich
    for step in track(range(10), description="[cyan]Processing..."):
        time.sleep(0.01)

    print(f"✅ Updated the README.md file.")           

except IOError:
    print(f"There was a problem writing to the file.")

# Use a try / except to open and read the Markdown file README.md, covert to HTML, save to README.html file and indicate if successful
try:

    # Read the Markdown file
    with open("./README.md", "r", encoding="utf-8") as f:
        markdown_text = f.read()

    # Convert Markdown to HTML
    import markdown
    html_content = markdown.markdown(
        markdown_text,
        extensions=['fenced_code']
    )

    # Wrap in a basic HTML template
    html_page = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Converted Markdown</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 2rem; }}
                pre code {{ background: #f4f4f4; padding: 0.5rem; display: block; }}
            </style>
    </head>
    <body background-color="#ffffff" font-color="#000000">
        {html_content}
    </body>
    </html>
    """
    # Generate a progress bar using rich
    for step in track(range(25), description="[cyan]Processing..."):
        time.sleep(0.01)
    
    print("Converting the md file to HTML code...")
    
    # Save to an HTML file
    with open("./README.html", "w", encoding="utf-8") as f:
        f.write(html_page)
    
    # Generate a progress bar using rich
    for step in track(range(25), description="[cyan]Processing..."):
        time.sleep(0.01) # Simulate work being done

    print("Saving the new HTML code...")
    print("✅ Success! Converted the README.md → README.html")

except IOError:
    print(f"There was a problem writing to the file.")









    

