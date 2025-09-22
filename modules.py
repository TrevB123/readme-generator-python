from InquirerPy import prompt


def questions_for_name_and_color():

# Get initial user input
# First asking two questions as an extra idea to practice formatting using rich
    while True:

        questions = [
                {"type": "input", "name": "name", "message": "What is your name?"},
                {"type": "input", "name": "color", "message": "What is your favourite colour? (Blue, Red, Green, Purple)"},
                ]

        responses = prompt (questions)

        # Extract all dictionary values
        # Using loop + keys()
        res = []
        for key in responses.keys() :
            res.append(responses[key])

        # printing result test
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

        # printing results test...
        # print("The list of values is : " +  str(validColors_str))

        # Conditional if, elif and else statments to identify which colour was typed (or not in the else statement). This only allows one of the four colour choices listed to be accepted
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

    return responses


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

        
