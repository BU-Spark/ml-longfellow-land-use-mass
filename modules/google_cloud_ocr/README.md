# Google Cloud OCR Setup with Python

## Step 1: Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. **Create a New Project**:
   - In the top-left corner, click the project dropdown menu and then "New Project."
   - Enter a project name (e.g., "OCR Project") and click "Create."

## Step 2: Enable the Cloud Vision API

1. In the **Google Cloud Console**, go to the **Navigation Menu** (three horizontal lines at the top left).
2. Click on **APIs & Services** > **Library**.
3. In the search bar, type **Vision API**.
4. Select **Cloud Vision API** and click **Enable**.

## Step 3: Create Service Account Credentials

1. Navigate to **APIs & Services** > **Credentials**.
2. Click on **Create Credentials** > **Service Account**.
3. **Service Account Details**:
   - Give the service account a name (e.g., "vision-api-service-account").
   - Click "Create and Continue."
4. **Grant Permissions**:
   - Choose **Role**: Select "Project" > "Editor" to give your service account sufficient permissions.
   - Click "Continue."
5. **Create JSON Key**:
   - After creating the service account, click on the three dots next to the account.
   - Select "Manage Keys" > "Add Key" > "Create New Key."
   - Choose **JSON** format and download the JSON file. This file contains your credentials.

## Step 4: Set Up the `.env` File

1. Create a new file named `.env` in the root directory of your Python project.
2. Add the following line to the `.env` file, replacing the path with the actual path to your downloaded JSON credentials file:

   ```bash
   GOOGLE_APPLICATION_CREDENTIALS=/path-to-your-credentials.json
   ```
   We recommend setting the path as ./credentials/google-cloud.json

## Step 5: Running the script

1. Ensure you have the needed package:

```bash
pip install google-cloud-vision python-dotenv
```

2. Run the script and see the text files for outputs
