# BriefWave

A Python module for automating the process of retrieving, summarizing, and emailing content using the OpenAI ChatGPT API.

## Features

- Uses OpenAI's ChatGPT API to generate summaries of IT circulars
- Formats summaries into professional HTML emails
- Sends emails via SMTP (supports Gmail)
- Modular design following Single Responsibility Principle
- Easy to configure via environment variables or .env file

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd it-circulars-automation
   ```

2. Install required dependencies:
   ```
   pip install openai python-dotenv requests
   ```

3. Configure your environment variables by creating a `.env` file:
   ```
   SENDER_EMAIL=your_email@gmail.com
   SENDER_PASSWORD=your_app_password  # Use App Password for Gmail!
   RECEIVER_EMAIL=recipient_email@example.com
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   ITD_CIRCULARS_URL=https://incometax.gov.in/iec/foportal/latest-news/circulars-notifications
   
   # OpenAI API Configuration
   OPENAI_API_KEY=your_openai_api_key
   OPENAI_MODEL=gpt-3.5-turbo
   OPENAI_PROMPT=Summarize the latest IT circulars from the Income Tax Department of India. Focus on key changes, deadlines, and implications for taxpayers. Format the information in a clear, concise manner suitable for an email newsletter.
   ```

## Usage

Run the automation script:

```
python main.py
```

## Module Structure

```
it_circulars/
├── __init__.py             # Package initialization
├── config/                 # Configuration settings
│   ├── __init__.py
│   └── settings.py         # Environment variables and config classes
├── services/               # Core services
│   ├── __init__.py
│   ├── chatgpt.py          # ChatGPT API client
│   └── email.py            # Email sending service
├── utils/                  # Utility functions
│   ├── __init__.py
│   └── formatter.py        # HTML formatting utilities
└── orchestrator.py         # Main workflow orchestrator
```

## Scheduling

### Windows Task Scheduler

To schedule this script to run automatically on Windows:

1. Open Task Scheduler (search for it in the Start menu)
2. Click "Create Basic Task"
3. Enter a name and description for the task
4. Select the trigger (Daily, Weekly, etc.)
5. Select "Start a program" as the action
6. Browse to your Python executable (e.g., `C:\Python39\python.exe`)
7. Add the full path to your script in the "Add arguments" field (e.g., `C:\path\to\it-circulars-automation\main.py`)
8. Set the "Start in" field to your script's directory (e.g., `C:\path\to\it-circulars-automation`)
9. Complete the wizard and check "Open the Properties dialog" before finishing
10. In the Properties dialog, you can set additional options like running whether the user is logged in or not

### Linux/macOS Cron Job

To schedule this script on Linux or macOS:

1. Open your crontab file:
   ```
   crontab -e
   ```

2. Add a line to run the script at your desired schedule:
   ```
   # Run daily at 8 AM
   0 8 * * * cd /path/to/it-circulars-automation && /usr/bin/python3 main.py >> /path/to/it-circulars-automation/cron.log 2>&1
   ```

## Security Notes

- For Gmail, you need to use an App Password if you have 2-factor authentication enabled
- Store your OpenAI API key securely and never commit it to version control
- Consider using environment variables instead of a .env file in production environments
