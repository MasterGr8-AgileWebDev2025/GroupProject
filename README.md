# Tennis Analytics Platform

The Tennis Analytics Platform is a web-based application designed to help tennis players 
track, analyze, and share their match performance data. The system enables users to upload 
match details, visualize performance metrics through interactive charts, and selectively 
share insights with other users.

## Purpose & Design

### Purpose
- 🎾 Empower **recreational and competitive players** to track progress and make data-informed improvements.
- 🧠 Enable **coaches** to monitor player development and provide targeted feedback.
- 🏆 Support **teams and clubs** in comparing performance across members.
- 📊 Promote **data literacy in sports** through intuitive dashboards and analytics.

### Design Philosophy
- 🖥️ **User-Centered Interface**: Clean navigation, responsive layout, and seamless user experience across devices.
- 📈 **Visualization-First**: Interactive charts, heatmaps, and dashboards for clear performance feedback.
- 🧩 **Modular Architecture**: Built with scalability in mind—ready for future integrations like ML, video analysis, and mobile support.
- 🔒 **Privacy & Permission Control**: Fine-grained sharing and access to ensure users retain control over their data.

This platform combines modern web technologies, intelligent analysis, and sleek design to create a smart, collaborative tool for the tennis community.

## Tech Stack

- **Backend Framework**: Flask (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Authentication**: Flask-Login
- **Form Handling**: Flask-WTF
- **ORM**: SQLAlchemy (Flask-SQLAlchemy)
- **Data Visualization**: Chart.js
- **Icons**: Font Awesome

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables
4. Run the application: `python main.py`

# Project Structure

/tennis-analytics-platform
|-- app.py                  # Application initialization and configuration
|-- main.py                 # Application entry point
|-- models.py               # Database model definitions
|-- forms.py                # Form definitions
|-- routes.py               # Routes and controllers
|-- helpers.py              # Helper functions
|-- utils.py                # Utility functions
|-- .gitignore              # Git ignore file
|-- .DS_Store               # Mac OS directory attributes file
|-- chromedriver.exe        # Chrome WebDriver for Selenium tests
|-- README.md               # Project documentation
|-- requirements.txt        # list of Python packages
|-- doc/                    # Documentation
|-- static/                 # Static resources
|   |-- css/                # CSS stylesheets
|   |-- js/                 # JavaScript files
|   |-- images/                # Image resources
|-- templates/              # HTML templates
|   |-- layout.html         # Base layout template
|   |-- index.html          # Home page
|   |-- dashboard.html      # User dashboard
|   |-- analysis.html       # Match analysis
|   |-- match_details.html  # Match details
|   |-- history.html        # Match history
|   |-- profile.html        # User profile
|   |-- upload.html         # Upload match
|   |-- share.html          # Share analysis
|   |-- about.html          # About page
|   |-- register.html       # User registration
|   |-- login.html          # User login



# GroupProject
The git repo for group 8 in Agile Web Dev of semester 1 2025.
## 👥 Project Members

| Student ID | Name           | GitHub Username |
|------------|----------------|-----------------|
| 24525844   | Daniel Xu      | danielxu1987    |
| 24386828   | Brielle Wang   | briellewang     |
| 24647365   | Md Jubel Ahmed |                 |
| 24404533   | Jimmy Li       | oxff-96         |
