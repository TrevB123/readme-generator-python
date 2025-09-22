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

        
