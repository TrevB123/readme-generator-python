from InquirerPy import prompt

def ask_questions_for_project():

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

  return answers

        






# Formatting the readme file

"""readme_content = f# {project_title}

## Description
{description}

## Installation
{installation}

## Usage
{usage}

## Contributing
{contributing}

## License
{license_info}
"""

"""# Function to append to an existing readme.md file
def append_file (): {
with open("README.md", "a") as f:
  f.write("Now the file has more content!")
  

  #open and read the file after the appending:
with open("README.md") as f:
  print(f.read())
}

# Function to write to readme.md file
def write_file () {
    with open("README.md", mode="w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("README.md") as f:
  print(f.read())
}

# Function to create a new empty readme.md file
def new_file () {
    f = open("README.md", "x")
}




def format_readmefile(address):

    address1 = address["address1"]
    address2 = address["address2"]
    address3 = address["address3"]
    town = address["town"]
    post_code = address["post_code"]
    county = address["county"]

    # Format the address as one long string
    formatted_address = address1
    if address2:
        formatted_address += ", " + address2
    if address3:
        formatted_address += ", " + address3

    formatted_address += ", " + town
    if county:
        formatted_address += ", " + county

    formatted_address += ", " + post_code

    return formatted_address
    """
