import boto3
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# AWS config from .env
AWS_REGION = os.getenv('AWS_REGION')
S3_BUCKET = os.getenv('S3_BUCKET')

print("AWS_REGION loaded as:", AWS_REGION)


rekognition = boto3.client('rekognition', region_name=AWS_REGION)
s3 = boto3.client('s3', region_name=AWS_REGION)

def upload_image_to_s3(file_obj, filename):
    s3.upload_fileobj(file_obj, S3_BUCKET, filename)
    return f"s3://{S3_BUCKET}/{filename}"

def detect_labels_s3(filename):
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': S3_BUCKET, 'Name': filename}},
        MaxLabels=10,
        MinConfidence=80
    )
    return response['Labels']

def delete_image_from_s3(filename):
    s3.delete_object(Bucket=S3_BUCKET, Key=filename)