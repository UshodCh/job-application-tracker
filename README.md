JobTrack — Job Application Tracker

A full-stack web application to help job seekers track their applications, generate AI-powered cover letters, and stay on top of deadlines.

Live Demo: job-application-tracker-gcbo.onrender.com


Features


User Authentication — Secure registration and login with email validation
Application Tracking — Add, edit, delete and search job applications
Status Management — Track applications across Applied, Interview, Offer and Rejected stages
Deadline Tracking — Set deadlines and get visual overdue alerts
AI Cover Letter Generator — Generate personalized cover letters using Google Gemini API
Analytics Dashboard — Visual charts showing application status breakdown
Email Notifications — Welcome email on registration via Gmail SMTP
User Profiles — Store your name, skills and bio for cover letter generation



Tech Stack

LayerTechnologyBackendDjango 6.0, PythonDatabasePostgreSQL (Supabase)FrontendHTML, CSS, JavaScriptChartsChart.jsAIGoogle Gemini APIEmailGmail SMTPDeploymentRenderVersion ControlGit + GitHub


Screenshots

Dashboard

Clean analytics dashboard showing application stats and status overview chart.

Application List

Searchable and filterable table with overdue deadline highlighting.

AI Cover Letter Generator

Paste any job description and get a personalized cover letter instantly.


Getting Started Locally

Prerequisites


Python 3.12+
Git


Installation


Clone the repository


bashgit clone https://github.com/UshodCh/job-application-tracker.git
cd job-application-tracker


Create and activate virtual environment


bashpython -m venv vel
vel\Scripts\activate  # Windows


Install dependencies


bashpip install -r requirements.txt


Create .env file in the root directory


SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
GEMINI_API_KEY=your_gemini_api_key
EMAIL_HOST_USER=your_gmail@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password


Run migrations


bashpython manage.py migrate


Start the development server


bashpython manage.py runserver


Visit http://127.0.0.1:8000



Environment Variables

VariableDescriptionSECRET_KEYDjango secret keyDEBUGSet to False in productionALLOWED_HOSTSComma separated list of allowed hostsDATABASE_URLPostgreSQL connection stringGEMINI_API_KEYGoogle Gemini API keyEMAIL_HOST_USERGmail address for sending emailsEMAIL_HOST_PASSWORDGmail app password


Deployment

This project is deployed on Render with Supabase PostgreSQL.

Every push to the main branch automatically redeploys the app.


What I Learned


Building full-stack Django applications from scratch
User authentication and security best practices
Integrating third-party AI APIs (Google Gemini)
Working with PostgreSQL in production
Deploying Django apps with Render and Supabase
Sending emails with Gmail SMTP and Python threading
Environment variable management for production



Author

Chegireddy Ushoddarsha


GitHub: @UshodCh



Built as a portfolio project to demonstrate full-stack Django development skills.