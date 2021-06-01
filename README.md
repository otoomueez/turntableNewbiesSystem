# turntablNewbiesSystem
A project for the management of Turntabl TLC and Internship programmes.

	This is a simple web app created for all interested in working as interns with Turntabl or
	anyone who is done with school and is looking forward to do their service with Turntabl to 
	be able to apply for the TLC training program.

Overview

	An online system where programmers (software engineers) can register for TLC and Internship programs. 
	Also An administrator has the permission to view applicants' 	
	details and send responses to applicants.

Goals

	For easy access of application to applicants
	Easy access to applicants details
	Easy to sort between applicants (Intern & TLC)
	Easy to contact applicants


Specifications

    Functional Requirements

       UI
       Homepage
  
	  - Nav bar
		  - Registration form links
		- Turntabl Contacts
			- Official website link
			- LinkedIn
			- Twitter
		- Admin Login
	- Homepage Content
		- Explaining TLC
		- Explaining Intern 
    -  Form 
    	- Input details 
    	- Submit button
		    - Prompt
    - Admin Panel
    	- Nav bar
		- Details of Admin
			- Content Section
					- Display table

Backend

	  - Database
		- Table

	- Server
		- Configuration of database and UI

Tools/Technologies

	  - Python
		- Flask
		- Jinja
    - SQLite
	  - HTML
    - CSS
	  - JavaScript
    
MILESTONES

    I.UI
      Homepage
      Form
      Admin Panel
   II. Server
   
    1.Setting Routes/Paths
    2.Function for taking inputs in form
    3.Class for database functions
      set_data_to_admin(data, table_name)
      set_data_to_db(data, table_name)
      get_data(table_name)
      
   III. Database (Applicants.db)
   
      Table for Applicants
