import base64
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def send_gmail(credentials_path, sender, to, subject, message):
    # Load OAuth2 credentials
    flow = InstalledAppFlow.from_client_secrets_file(credentials_path, ["https://www.googleapis.com/auth/gmail.send"])
    credentials = flow.run_local_server(port=0)

    # Build the Gmail API service
    service = build('gmail', 'v1', credentials=credentials)

    # Create a properly formatted email message
    email_message = {
        "raw": base64.urlsafe_b64encode(f"From: {sender}\nTo: {to}\nSubject: {subject}\n\n{message}".encode()).decode()
    }

    # Send the email using the Gmail API
    try:
        message = service.users().messages().send(userId="me", body=email_message).execute()
        print(f"Email sent successfully! Message ID: {message['id']}")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")



def main(receiver_mail,system_info):
    # Replace 'path/to/your/credentials.json' with the path to the credentials JSON file you downloaded
    credentials_path = "C:\\Users\gowrishankar\Downloads\credentials.json"

    sender_email = "psgfreshers@gmail.com"
    recipient_email = receiver_mail
    email_subject = "image Email"
    email_body = system_info

    send_gmail(credentials_path, sender_email, recipient_email, email_subject, email_body)

#main('smvignesh80@gmail.com','widows')