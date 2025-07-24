"""
Orchestrator module for BriefWave.
Coordinates the workflow between different components.
"""

from datetime import datetime
from settings import ConfigManager, EmailConfig, OpenAIConfig
from services.chatgpt import ChatGPTClient
from services.email import EmailSender
from utils.html_formatter import HTMLFormatter

class BriefWaveAutomator:
    """Orchestrates the entire process of generating and emailing content summaries."""

    def __init__(self):
        # Validate configurations
        ConfigManager.validate_email_config(
            EmailConfig.SENDER_EMAIL,
            EmailConfig.SENDER_PASSWORD,
            EmailConfig.RECEIVER_EMAIL
        )
        ConfigManager.validate_api_config(
            OpenAIConfig.API_KEY,
            OpenAIConfig.MODEL
        )
        
        # Initialize components
        self.chatgpt_client = ChatGPTClient(
            OpenAIConfig.API_KEY,
            OpenAIConfig.MODEL
        )
        self.email_sender = EmailSender(
            EmailConfig.SENDER_EMAIL,
            EmailConfig.SENDER_PASSWORD,
            EmailConfig.SMTP_SERVER,
            EmailConfig.SMTP_PORT
        )

    def run(self):
        """Executes the automation workflow: generates summary and sends email."""
        
        print(f"Starting IT Circulars Automation at {datetime.now()}")

        # Generate summary using ChatGPT
        summary_text = self.chatgpt_client.generate_summary(OpenAIConfig.PROMPT)

        # Format email content
        email_subject = f"{EmailConfig.EMAIL_SUBJECT} - {datetime.now().strftime('%Y-%m-%d')}"
        text_content = f"Hello,\n\nHere is your summary:\n\n{summary_text}\n\n ** \n{EmailConfig.EMAIL_DISCLAIMER}\n"
        html_content = HTMLFormatter.format_summary_to_html(summary_text)
        
        # Send email
        success = self.email_sender.send_email(
            email_subject, 
            text_content, 
            html_content, 
            EmailConfig.RECEIVER_EMAIL
        )

        print(f"Automation {'completed successfully' if success else 'failed'} at {datetime.now()}")
        return success
