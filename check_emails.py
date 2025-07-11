import imaplib
import email
from email.header import decode_header
import joblib


model = joblib.load('spam_classifier_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')


IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "SeninMailin@gmail.com"
EMAIL_PASSWORD = "Gmail-Güvenlik-Numarası"


mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
mail.select("inbox")


status, messages = mail.search(None, "ALL")
email_ids = messages[0].split()[-10:]

print("Son 10 e-posta sınıflandırılıyor...\n")

for email_id in email_ids:
    _, msg_data = mail.fetch(email_id, "(RFC822)")
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)


    subject, encoding = decode_header(msg["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding if encoding else "utf-8")


    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                try:
                    body = part.get_payload(decode=True).decode()
                except:
                    pass
    else:
        body = msg.get_payload(decode=True).decode()


    features = vectorizer.transform([subject + " " + body])
    prediction = model.predict(features)[0]

    label = "📮 HAM" if prediction == 0 else "🚫 SPAM"
    print(f"Konu: {subject}")
    print(f"Etiket: {label}")
    print("-" * 50)

mail.logout()
