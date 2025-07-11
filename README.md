# Email Spam Classifier

An intelligent email spam detection system that automatically classifies incoming emails as spam or legitimate using machine learning.

## Features

- 🤖 **Machine Learning Model**: Trained on 5,575 email samples using Logistic Regression
- 📧 **Gmail Integration**: Connects to Gmail via IMAP to analyze inbox emails
- 🔄 **Real-time Classification**: Automatically classifies the last 10 emails in your inbox
- 📝 **Text Analysis**: Analyzes both subject and body content for accurate classification
- 💾 **Model Persistence**: Saves trained model for reuse without retraining

## How It Works

1. **Training Phase**: The system trains on a dataset of labeled emails (spam/ham)
2. **Feature Extraction**: Uses CountVectorizer to convert text to numerical features
3. **Classification**: Logistic Regression model predicts spam probability
4. **Email Analysis**: Connects to Gmail and analyzes recent emails
5. **Results**: Displays classification results with clear labels

## Files

- `train_model.py` - Trains and saves the spam classification model
- `check_emails.py` - Connects to Gmail and classifies recent emails
- `spam.csv` - Training dataset with 5,575 email samples
- `spam_classifier_model.pkl` - Saved trained model (generated after training)
- `vectorizer.pkl` - Saved text vectorizer (generated after training)

## Technologies Used

- Python 3.x
- scikit-learn (Logistic Regression, CountVectorizer)
- pandas (Data manipulation)
- imaplib (Gmail connection)
- joblib (Model serialization)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/email-spam-classifier.git
   cd email-spam-classifier
   ```

2. Install required packages:
   ```bash
   pip install pandas scikit-learn joblib
   ```

## Usage

1. Train the model:
   ```bash
   python train_model.py
   ```

2. Configure Gmail settings in `check_emails.py`:
   - Replace `"SeninMailin@gmail.com"` with your Gmail address
   - Replace `"Gmail-Güvenlik-Numarası"` with your Gmail App Password

3. Classify emails:
   ```bash
   python check_emails.py
   ```

## Gmail Setup

To use this with Gmail, you need to:

1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a password for "Mail"
3. Use this App Password in the `check_emails.py` file

## Requirements

- Gmail account with IMAP enabled
- Gmail App Password (for authentication)
- Python packages: pandas, scikit-learn, joblib

## License

MIT License

## Contributing

Feel free to submit issues and enhancement requests! 