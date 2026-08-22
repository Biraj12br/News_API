This project demonstrates how to build a Python application that:
Fetches the latest news from News API.
Processes the JSON response.
Extracts headline, source, description, publication time, and article URL.
Creates an HTML email using Python's email.message module.
Sends the news digest using SMTP and smtplib.
Runs automatically in the cloud using PythonAnywhere Scheduled Tasks.

Architecture

                    +----------------------+
                    |      News API        |
                    |  Latest Headlines    |
                    +----------+-----------+
                               |
                               | HTTP GET
                               v
                    +----------------------+
                    |    Python Script      |
                    |       requests       |
                    +----------+-----------+
                               |
                               | JSON
                               v
                    +----------------------+
                    | Extract News Articles |
                    | title / source / URL  |
                    | description / date    |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | email.message        |
                    | Build HTML Email      |
                    +----------+-----------+
                               |
                               | SMTP
                               v
                    +----------------------+
                    |      Gmail SMTP      |
                    | smtp.gmail.com:587   |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |    User's Email      |
                    |   News Digest        |
                    +----------------------+

                         PythonAnywhere
                    Scheduled Task executes
                         the script

Technologies Used :
Python
Requests
News API
smtplib
email.message.EmailMessage
SMTP
PythonAnywhere
Gmail SMTP
