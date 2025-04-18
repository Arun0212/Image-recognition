import streamlit as st
import boto3
from decimal import Decimal

# Initialize Rekognition and DynamoDB clients
rekognition_client = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

table = dynamodb.Table('ImageLabelsTable')

# Function to analyze image with Rekognition
def analyze_image(image_bytes):
    response = rekognition_client.detect_labels(
        Image={'Bytes': image_bytes},
        MaxLabels=10,
        MinConfidence=80
    )
    return response['Labels']

# Function to save labels to DynamoDB
def save_labels_to_dynamodb(image_id, labels):
    for label in labels:
        table.put_item(
            Item={
                'ImageId': image_id,  # Unique ID for the image
                'LabelName': label['Name'],  # Name of the label detected by Rekognition
                'Confidence': Decimal(str(label['Confidence']))  # Convert to Decimal
            }
        )

# Streamlit app layout
st.title("Image Label Detector with DynamoDB")

image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if image_file is not None:
    # Display the uploaded image
    st.image(image_file, caption='Uploaded Image', use_column_width=True)
    
    # Convert the image to bytes for Rekognition
    image_bytes = image_file.read()
    
    # Analyze the image using Rekognition
    labels = analyze_image(image_bytes)
    
    # Display the detected labels
    st.write("Detected Labels:")
    for label in labels:
        st.write(f"{label['Name']} - Confidence: {label['Confidence']}%")
    
    # Save the labels to DynamoDB
    image_id = f"image_{image_file.name}"  # You can use other unique identifiers here
    save_labels_to_dynamodb(image_id, labels)
    st.write("Labels have been saved to DynamoDB!")