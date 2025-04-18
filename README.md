# Image Label Detector with DynamoDB

## Project Overview

This project uses **AWS Rekognition** to analyze images and detect labels such as objects, people, and scenes. The detected labels are stored in **AWS DynamoDB** for easy retrieval and tracking. The application is built using **Streamlit**, which provides an interactive web interface for users to upload images and view the detected labels in real-time.

### Key Features:
- **Image Upload**: Users can upload images (JPG, JPEG, PNG formats).
- **Rekognition Integration**: AWS Rekognition analyzes the uploaded image and detects labels.
- **DynamoDB Storage**: Detected labels are saved to **AWS DynamoDB** with each image's unique ID.
- **Streamlit Interface**: Simple, interactive UI for image uploads and label display.

---

## Prerequisites

### **Before running this project, you need the following:**

- **AWS Account** with access to the following services:
  - **Amazon Rekognition**: Used for detecting labels in images.
  - **Amazon DynamoDB**: Used for storing the image labels.
  
- **AWS CLI**: Installed and configured with the necessary credentials (`aws configure`).

- **Python 3.x**: Make sure you have **Python 3** installed on your system.

- **Streamlit**: Installed to run the web application.

---

## Installation

### Step 1: Clone the Repository

Clone the repository to your local machine or cloud environment:

```bash
git clone https://github.com/yourusername/image-label-detector.git
cd image-label-detector
Step 2: Install Dependencies
You need to install the required Python libraries. The necessary dependencies are listed in requirements.txt.

bash
Copy
Edit
pip install -r requirements.txt
If you don't have the requirements.txt file, install the following manually:

bash
Copy
Edit
pip install streamlit boto3
Step 3: Configure AWS CLI
Ensure that your AWS CLI is configured properly with the necessary permissions:

bash
Copy
Edit
aws configure
Enter your AWS Access Key ID, Secret Access Key, Region (e.g., ap-south-1), and Output Format.

Make sure your IAM user has permissions for the following:

rekognition:DetectLabels

dynamodb:PutItem (to save labels to DynamoDB)

Step 4: Set up DynamoDB Table
Create a DynamoDB table in AWS with the following configuration:

Table Name: ImageLabelsTable

Partition Key: ImageId (String)

You can create the table directly through the AWS console or use the AWS CLI.

Usage
Step 1: Run the Streamlit Application
To start the web application, use the following command:

bash
Copy
Edit
streamlit run app.py
Streamlit will launch the app in your default browser.

Step 2: Upload Image
In the Streamlit interface, click on the Upload an image button.

Choose an image file (JPG, JPEG, or PNG).

The image will be displayed on the web interface.

Step 3: View Detected Labels
The AWS Rekognition service will analyze the uploaded image and return the detected labels with their confidence scores.

The labels and confidence scores will be displayed in the app.

Step 4: Store Labels in DynamoDB
After processing the image, the detected labels are automatically stored in AWS DynamoDB.

The ImageId is generated from the image file name (you can customize this ID format).

A message saying "Labels have been saved to DynamoDB!" will be displayed once the labels are successfully stored.

Project Structure
bash
Copy
Edit
.
├── app.py                # Streamlit app for the user interface
├── requirements.txt      # List of required Python packages
├── .gitignore            # Files and directories to ignore in Git
└── README.md             # This file
Code Explanation:
Rekognition Client: The rekognition_client object is used to call the detect_labels API from AWS Rekognition. This API analyzes the uploaded image and returns labels detected with confidence scores.

DynamoDB Integration: The save_labels_to_dynamodb function stores the detected labels in an AWS DynamoDB table named ImageLabelsTable. The labels are saved as items, with each item containing an ImageId, LabelName, and Confidence.

Streamlit App: The app allows users to upload images. It then shows the uploaded image, calls AWS Rekognition to detect labels, and displays the labels in the app interface. Finally, it saves the labels to DynamoDB.

AWS Configuration
1. AWS Rekognition:
Make sure the IAM user or role you are using has the rekognition:DetectLabels permission.

2. AWS DynamoDB:
The DynamoDB table should have the following configuration:

Table Name: ImageLabelsTable

Partition Key: ImageId (String)

You can create this table manually in the AWS console or via the CLI.

Example DynamoDB setup:

bash
Copy
Edit
aws dynamodb create-table \
    --table-name ImageLabelsTable \
    --attribute-definitions AttributeName=ImageId,AttributeType=S \
    --key-schema AttributeName=ImageId,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
3. Permissions:
Ensure the IAM user has the following permissions:

rekognition:DetectLabels

dynamodb:PutItem

Contributing
We welcome contributions to this project! To contribute:

Fork the repository.

Clone your forked repository.

Create a new branch (git checkout -b feature/your-feature).

Make your changes.

Commit the changes (git commit -am 'Add new feature').

Push to your fork (git push origin feature/your-feature).

Open a Pull Request on GitHub.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Acknowledgements
Amazon Rekognition Documentation

Streamlit Documentation

AWS DynamoDB Documentation
