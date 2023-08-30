# Streamlit_Firebase

## Table of Contents
- [Project Description](#project-description)
- [Getting Started](#getting-started)
- [Usage](#usage)

## Project Description
Aimple application for connect python streamlit and Firebase Authentication , Firebas Realtime Database and Firebase Storage.
## Getting Started
install requirements - 
```bash 
pip install -r .\requirements.txt
```
## Usage
### Firebase SDK Setup and Configuration

To set up Firebase SDK for your project, follow these steps:

1. **Access Firebase Console**: Go to the [Firebase Console](https://console.firebase.google.com/) and sign in with your Google account.

2. **Create or Select Your Firebase Project**: If you don't have an existing Firebase project, create a new one. If you already have a project, select it from the Firebase Console dashboard.

3. **Navigate to Project Settings**: In the Firebase Console, click on the gear icon (settings) next to "Project Overview" on the left sidebar.

4. **General Settings**: Under the "General" tab, you'll find various settings for your project. Scroll down to find the "Your apps" section.

5. **Your Apps**: In the "Your apps" section, you'll see your project's app(s) listed. Click on the app for which you want to access the SDK setup and configuration.

6. **SDK Setup and Configuration**: You'll now be on the SDK setup and configuration page for the selected app. Here, you'll find important information, including:

   - Firebase SDK configuration code (similar to what you have in your project's README).
   - Web app configuration details, including the Firebase Configuration Object.
   - Links to SDK setup instructions for various platforms (iOS, Android, Web, etc.).

   Copy the Firebase SDK configuration code and use it in your project as needed.

7. **Additional Information**: You can also access other app-specific information and settings related to your Firebase project on this page.

That's it! You've now accessed the SDK setup and configuration information for your Firebase project.

Remember to keep your Firebase configuration secure and do not expose sensitive information, such as API keys, in public repositories. Use environment variables or a secrets manager for secure configuration in your applications.

### Configuration Keys

In your project, you may need to configure Firebase for various services. Below is an example of a Firebase configuration object with placeholders for sensitive information.

```javascript
firebaseConfig = {
  "apiKey": "YOUR_API_KEY",           // Replace with your Firebase API Key
  "authDomain": "YOUR_AUTH_DOMAIN",   // Replace with your Firebase Auth Domain
  "projectId": "YOUR_PROJECT_ID",     // Replace with your Firebase Project ID

  // Remove the "databaseURL" entry if you are not using the Firebase Realtime Database.
  // "databaseURL": "YOUR_DATABASE_URL", // Replace with your Firebase Realtime Database URL

  "storageBucket": "YOUR_STORAGE_BUCKET",     // Replace with your Firebase Storage Bucket
  "messagingSenderId": "YOUR_MESSAGING_SENDER_ID", // Replace with your Firebase Messaging Sender ID
  "appId": "YOUR_APP_ID",               // Replace with your Firebase App ID
  "measurementId": "YOUR_MEASUREMENT_ID"  // Replace with your Firebase Measurement ID
}
```
### To Run code
```bash
streamlit run main.py
```




