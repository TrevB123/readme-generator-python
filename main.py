from __future__ import print_function, unicode_literals
from InquirerPy import prompt
from InquirerPy.base.control import Choice
import markdown
import json
import os
from rich.console import Console
from rich.table import Table
from rich.progress import track
import time
from rich import print

from modules import ask_questions_for_project

console = Console()

# Get user input with Inquirer
# Display a formatted message with Rich

while True:

    questions = [
            {"type": "input", "name": "name", "message": "What is your name?"},
            {"type": "input", "name": "color", "message": "What is your favourite colour? (Blue, Red, Green, Purple)"},
            ]

    responses = prompt (questions)

    print(responses)



    # Extracting all dictionary values
    # Using loop + keys()
    res = []
    for key in responses.keys() :
        res.append(responses[key])

    # printing result
    # print("The list of values is : " +  str(res))

    validColors_str = [] 
    validColors_str.append("blue")
    validColors_str.append("red")
    validColors_str.append("green")
    validColors_str.append("purple")
    validColors_str.append("Blue")
    validColors_str.append("Red")
    validColors_str.append("Green")
    validColors_str.append("Purple")

    # print("The list of values is : " +  str(validColors_str))


    if res[1] == "blue":
        print (f"✅ Great choice! You picked [blue]Blue[/blue]")
        break
    elif res[1] == "green":
        print (f"✅ Great choice! You picked [green]Green[/green]")
        break
    elif res[1] == "red":
        print (f"✅ Great choice! You picked [red]Green[/red]")
        break
    elif res[1] == "purple":
        print (f"✅ Great choice! You picked [purple]Purple[/purple]")
        break
    elif res[1] == "Green":
        print (f"✅ Great choice! You picked [green]Green[/green]")
        break
    elif res[1] == "Red":
        print (f"✅ Great choice! You picked [red]Red[/red]")
        break
    elif res[1] == "Purple":
        print (f"✅ Great choice! You picked [purple]Purple[/purple]")
        break
    elif res[1] == "Blue":
        print (f"✅ Great choice! You picked [blue]Blue[/blue]")
        break
    else:
        print (f"❌ Please try again – don't forget to choose only from Blue, Red, Green, Purple.\n")          


"""
questions = [
{"type": "input", "name": "name", "message": "What is your name?"},
{"type": "input", "name": "color", "message": "What is your favourite colour? (Blue, Red, Green, Purple)"},
]
answers = prompt (questions)

print(answers)


 
    try: 
        console.print( 
            f"Hello,[bold {answers['color']}] {answers ['name']}![/bold {answers['color']}]",
        style=answers["color"]
        )
    except: color = ('blue', 'red', 'green', 'purple')
    console.print("Invalid input! Please enter a valid color (blue, red, green, purple).")
    else: color != ('blue', 'red', 'green', 'purple')
    console.print("Thank you")

"""
# print a message formatting it with the response color word in the chosen color using rich

print(f"[{responses['color'].lower()}]{responses['name']}[/{responses['color'].lower()}] let's create a README file! 🚀\n")
# print(f"Hey, [{answers['color']}]{answers['name']} [/{answers['color']}] let's create a README file 🚀\n")


"""
questions = [
    {
        "type": "input", 
        "message": "Enter a project title:", 
        "name": "project_title"
    },
    
    {
        "type": "input",
        "message": "Enter a project description:",
        "name": "project_description"
    },
    
    {
        "type": "input",
        "message": "Project installation instructions:",
        "name": "project_installation"
    },
    
    {
        "type": "input",
        "message": "What can this project be used for?",
        "name": "usage_information"
    },

    {
        "type": "list",
        "name": "license_type",
        "message": "License type (choose from below):",
        "choices": ["MIT License", "GNU General Public License (GPL)", "GNU Lesser General Public License (LGPL)", "Apache License 2.0", "Mozilla Public License 2.0 (MPL 2.0)", "BSC License"],
    },

    {
        "type": "input",
        "message": "Author name:",
        "name": "author_name"
    },

    {
        "type": "input",
        "message": "Please supply contact details (e.g. email address):",
        "name": "contact_details"
    },    
    ]


# Create results
answers = prompt(questions)

# ReadmeData = results.values



print(json.dumps(answers, indent=2))
print(answers.keys())
print(answers.values())
"""

"""
class reproDetails:

    def __init__(self, project_name, project_description, project_installation, usage_information, licence_type, author_name, contact_details):
            self.project_name = project_name
            self.project_description = project_description
            self.project_installation = project_installation
            self.usage_information = usage_information
            self.licence_type = licence_type
            self.author_name = author_name
            self.contact_details = contact_details

    def __str__(self):
            # Format the data in a markup-like style.
            return (
                f"project_name = {self.project_name}\n"
                f"project_description = {self.project_description}\n"
                f"project_installation = {self.project_installation}\n"
                f"usage_information = {self.usage_information}\n"
                f"licence_type = {self.licence_type}\n"
                f"author_name = {self.author_name}\n"
                f"contact_details = {self.contact_details}\n"
                )
    
    def __formatting__(self):
                # Format the data in a markup-like style.
                return (
                f"Project Name = {self.project_name}\n"
                f"Project Description = {self.project_description}\n"
                f"Project Installation = {self.project_installation}\n"
                f"Usage Information = {self.usage_information}\n"
                f"Licence Type = {self.licence_type}\n"
                f"Author Name = {self.author_name}\n"
                f"Contact Details = {self.contact_details}\n"
                )

formatted = reproDetails.__formatting__

print(formatted)


def append_file ():
    e = int("abc")
    file_path = "./README.md"
    try:
        with open(file_path, 'a') as file:
            file.write("# Project Name")
            file.write("## Project Description:")
            file.write({reproDetails.__formatting__()})
            file.write("## Project Installation")
            file.write("## Usage Information")
            file.write("## Licence Type")
            file.write("## Author Name")
            file.write("## Contact Details")
    except IOError as e:
        print(f"An error occurred: {e}")


"""


# Call the function in modules.py
answers = ask_questions_for_project()


md_text = "New"
file_path = "./README.md"
                            
# Some markdown content
markdown_string = f"""\
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


try:
    with open(file_path, 'w') as file:
        file.write(markdown_string)

    # Generate a progress bar using rich
    for step in track(range(10), description="[cyan]Processing..."):
        time.sleep(0.01) # Simulate work being done

    print(f"✅ Updated the README.md file.")           

except IOError:
    print(f"There was a problem writing to the file.")


"""
try:
    import markdown
    markdown.markdownFromFile(input="./README.md", output="./README.html")

except IOError:
    print(f"There was a problem writing to the file.")


    # Wrap HTML in a basic template
    html_page = f
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>User Profile</title>
    </head>
    <body>
    {html_content}
    </body>
    </html>
    


    print("\n--- Rendered HTML ---\n", html_page)
    

    # Save the HTML file
    with open('README.html', 'w', encoding='utf-8') as f:
        f.write(html_page)
        


print(f"✅ Markdown successfully converted to HTML in the HTML file.")



# Convert Markdown to HTML
    html_content = markdown.markdown(markdown_string)

# Read the Markdown file
    with open("./README.md", "r") as md_file:
        markdown_content = md_file.read()

try:
    import markdown
    html = markdown.markdown(markdown_string)
    print("\n--- Rendered HTML ---\n", html)
except ImportError:
    pass


    html_string = markdown.markdown(markdown_string)
    print(html_string)

    with open(file_path, 'w') as file:
        file.write(markdown_string)

        print(f"All done with the .md file.")           

except IOError: e
        
"""



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

    # Wrap in a basic HTML structure
    

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
    <body>
        {html_content}
    </body>
    </html>
    """
    # Generate a progress bar using rich
    for step in track(range(25), description="[cyan]Processing..."):
        time.sleep(0.01) # Simulate work being done
    
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









    

