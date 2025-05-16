# Tennis Analytics Platform

## GroupProject
The git repo for group 8 in Agile Web Dev of semester 1 2025.
### 👥 Project Members

| Student ID | Name           | GitHub Username |
|------------|----------------|-----------------|
| 24525844   | Daniel Xu      | danielxu1987    |
| 24386828   | Brielle Wang   | briellewang     |
| 24647365   | Md Jubel Ahmed | Jubel-Ahmed     |
| 24404533   | Jimmy Li       | oxff-96         |


## Features

### Match Tracking
- Record detailed match statistics including:
  - Score tracking
  - Shot types and outcomes
  - Serve performance
  - Rally analysis
  - Court positioning

### Advanced Analytics
- Comprehensive match statistics
- Performance trends
- Win/loss analysis
- Serve and return statistics
- Shot distribution patterns

### AI-Powered Analysis
- Match performance insights
- Strategic recommendations
- Technical improvement suggestions
- Opponent analysis
- Personalized training recommendations

## Technical Stack

### Backend
- Python
- Flask
- SQLAlchemy
- Google Gemini API for AI analysis

### Frontend
- HTML5
- CSS3
- JavaScript
- Chart.js for data visualization

## Project Structure
```
tennis-analytics/
├── .cursor/          # Cursor IDE configuration
├── .github/          # GitHub configuration files
├── .idea/            # IntelliJ IDEA configuration
├── docs/             # Project documentation
├── instance/         # Instance-specific files
├── migrations/       # Database migrations
├── routes/           # Route definitions
├── selenium_tests/   # Selenium test files
│   ├── test_homepage.py    # Homepage UI tests
│   └── test_login_page.py  # Login page UI tests
├── static/          # Static files (CSS, JS, images)
├── templates/       # HTML templates
├── .DS_Store        # macOS system file
├── .env             # Environment variables
├── .gitignore       # Git ignore rules
├── app.py           # Main application file
├── chromedriver.exe # Chrome WebDriver for Selenium
├── config.py        # Application configuration
├── conftest.py      # Pytest configuration
├── forms.py         # Form definitions
├── helpers.py       # Helper functions
├── main.py          # Application entry point
├── match_analysis.html      # Match analysis template
├── match_details.html       # Match details template
├── match_report_orginal.html # Original match report template
├── models.py        # Database models
├── requirements.txt # Project dependencies
├── routes.py        # Route definitions
├── test_utils.py    # Utility function tests
└── utils.py         # Utility functions
```

### Key Components

#### Application Files
- `app.py`: Main Flask application file
- `main.py`: Application entry point
- `routes.py`: Route handlers and endpoints
- `models.py`: Database models and schemas
- `forms.py`: Form definitions for user input
- `config.py`: Application configuration settings

#### Testing
- `selenium_tests/`: UI testing with Selenium
  - `test_homepage.py`: Tests for homepage functionality
  - `test_login_page.py`: Tests for login page functionality
- `test_utils.py`: Unit tests for utility functions
- `conftest.py`: Pytest configuration and fixtures

#### Templates
- `templates/`: HTML templates directory
- `match_analysis.html`: AI-powered match analysis view
- `match_details.html`: Detailed match statistics view
- `match_report_orginal.html`: Original match report template

#### Utilities
- `utils.py`: Core utility functions
- `helpers.py`: Helper functions for data processing
- `chromedriver.exe`: Chrome WebDriver for Selenium tests

#### Configuration
- `.env`: Environment variables
- `requirements.txt`: Project dependencies
- `.gitignore`: Git ignore rules

#### Documentation
- `docs/`: Project documentation
- `README.md`: Project overview and setup instructions

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Google Gemini API for AI analysis capabilities
- Chart.js for data visualization
- Flask community for the web framework

## Customer Support Guidelines

### Objective 🎯
You are an exceptional customer support representative for the Tennis Analytics Platform. Your objective is to help users understand and effectively use our tennis match analysis system. This includes:
- Answering questions about platform features
- Providing guidance on match data recording
- Explaining AI analysis results
- Troubleshooting technical issues
- Offering best practices for tennis analytics

### Communication Style 💬
- **Tone**: Friendly and professional
- **Format**: Use clear structure with:
  - Headers for main topics
  - Bullet points for lists
  - Bold text for emphasis
  - Emojis for engagement
- **Language**: Clear and concise, avoiding technical jargon unless necessary

### Response Guidelines 📝
1. **Always verify information** from our knowledge base before responding
2. **Provide specific examples** when explaining features
3. **Include relevant links** to documentation or tutorials
4. **Ask clarifying questions** if the user's query is unclear
5. **Stay within scope** of tennis analytics platform support
6. **Redirect off-topic queries** to appropriate resources

### Common Support Topics 🎾
1. **Match Recording**
   - How to start a new match
   - Recording different shot types
   - Saving and editing match data

2. **Data Analysis**
   - Understanding statistics
   - Interpreting AI recommendations
   - Exporting match reports

3. **Technical Support**
   - Account management
   - Device compatibility
   - Data synchronization

4. **Best Practices**
   - Optimal data recording
   - Maximizing AI insights
   - Regular performance tracking

### Escalation Process ⚡
If a query requires technical expertise:
1. Document the issue thoroughly
2. Collect relevant user information
3. Escalate to the development team
4. Follow up with the user

### Response Templates 📋
```
🎾 Welcome Message:
Hi [User]! I'm here to help you with the Tennis Analytics Platform. How can I assist you today?

📊 Feature Explanation:
The [feature name] helps you [benefit] by [how it works]. Here's a quick guide:
• Step 1: [instruction]
• Step 2: [instruction]
• Step 3: [instruction]

🔧 Technical Support:
I understand you're having trouble with [issue]. Let's try these steps:
1. [First troubleshooting step]
2. [Second troubleshooting step]
3. [Third troubleshooting step]

❓ Need More Information:
To better assist you, could you please provide:
• [Specific information needed]
• [Any error messages]
• [Steps you've already tried]
```

### Quality Standards ✅
- Respond within 24 hours
- Maintain 95% accuracy in responses
- Follow up on unresolved issues
- Document all support interactions
- Regular knowledge base updates

### Continuous Improvement 🔄
- Collect user feedback
- Update support documentation
- Share common issues with development team
- Regular training on new features
- Monitor support metrics

The Tennis Analytics Platform is a web-based application designed to help tennis players 
track, analyze, and share their match performance data. The system enables users to upload 
match details, visualize performance metrics through interactive charts, and selectively 
share insights with other users.

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/GroupProject/tennis-analytics.git
cd tennis-analytics
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
flask db upgrade
```

5. Run the application:
```bash
flask run
```

## Testing

Run `pytest` to collect and run all test files.
Use `pytest test_utils.py` to run only the test file `test_utils.py`.

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
