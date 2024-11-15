# Email Sender Script

A simple Python script to send emails using Gmail's SMTP server. This script allows you to send a basic email using your Gmail account with the help of an App Password.

## Requirements

- Python 3.x
- `python-dotenv` (for secure management of credentials)
- A Gmail account with **App Passwords** enabled

## Setup Instructions

1. **Clone the Repository** (or create a new directory):
   ```bash
   git clone https://github.com/your-repository/email_sender.git
   cd email_sender
   ```

2. **Create a Virtual Environment** (recommended):
   - Install the required Python packages in a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   Install the `python-dotenv` package to manage environment variables securely:
   ```bash
   pip install python-dotenv
   ```

4. **Generate an App Password**:
   - If you're using Gmail, create an **App Password** instead of using your regular Gmail password:
     - Go to your [Google Account Security Settings](https://myaccount.google.com/security).
     - Under "Signing in to Google," click "App Passwords."
     - Generate an app password for use with the script.

5. **Create a `.env` File**:
   - Create a `.env` file in the project root directory with the following content:
     ```
     EMAIL_USER=your_email@gmail.com
     EMAIL_PASS=your_generated_app_password
     ```
   - **Important**: Make sure the `.env` file is added to `.gitignore` to keep it secure.
     ```bash
     echo ".env" >> .gitignore
     ```

6. **Update the Script**:
   - Open `send_email.py` and replace the `receiver_email` variable with the email address you want to send the email to:
     ```python
     receiver_email = "recipient@example.com"
     ```

## Running the Script

Once everything is set up, you can run the script to send an email:

```bash
python3 send_email.py
```

If everything is configured correctly, you'll see the message:
```
Email sent successfully!
```

## Security Notes

- **Never** expose your Gmail password in the code. Always use an **App Password**.
- Keep your `.env` file secure by adding it to `.gitignore`.
  
