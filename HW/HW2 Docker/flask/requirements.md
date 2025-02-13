** Project Description ** 

This project is going to create a version control system where merges are managed by memes. The product is called GiggleGit and it's managed by the startup CodeChuckle. Additionally there is a new tool named SnickerSync that "merges with a snicker", a meme-based Git diff tool. 


** Agile ** 

Theme: Get GiggleGit demo into a stable enough alpha to start onboarding some adventurous clients

Epic: Onboarding experience

User Story 1: As a vanilla git power-user that has never seen GiggleGit before, I want to learn more about how this tool works so I can understand how merges are managed by memes. 

User Story 2: As a team lead onboarding an experienced GiggleGit user, I want to configure and help my team setup so that they can properly and efficiently collaborate using this tool. 

User Story 3: As a newly onboarded developer that has never used GiggleGit, I want to familiarize myself with it's functionalities and workflow so that I can use it in my own work. 

Task: Look through the database and understand how the data related to merges and memes is stored. 

    Ticket 1: Analyze database structure and document schema 

        - review the existing database schema, commits, branches and code by next week and document your findings. 

    Ticket 2: write a setup guide to help onboard other new members 

        - Create a short guide of your findings after familiarizing yourself with the database and include instructions on where to start and how to onboard for any newbies. 

This is not a user story. Why not? What is it? As a user I want to be able to authenticate on a new machine 

** this is not a user story because it doesn't specify well enough who the user is and why they want to do this task. There's no information about the goal or motivation of the user so we don't know why they want to authenticate on a new machine. 


** Formal requirements ** 

Goal: Create an easy to use and engaging Git diff tool that enhances the merge experience by integrating meme-based syncing. 

Non-goal: use an API to integrate some AI-generated memes into the sync. 

Non-functional requirement 1: Security 

    Functional requirement: 
        - Set up user authentication for user credentials
        - Encrypt and store all user data to make sure it's protected 

Non-functional requirement 1: repeatability 

    Functional requirement: 
        - Implement an versioned algorithm that randomly selects a meme out of a library 
        - Log sync results for debugging and reproducibility

