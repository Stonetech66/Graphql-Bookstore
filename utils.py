import boto3
import uuid
from django.conf import settings
from django.core.validators import validate_image_file_extension



s3=boto3.client("s3", region_name=settings.AWS_REGION_NAME, aws_access_key_id=settings.AWS_ACCESS_KEY, aws_secret_access_key=settings.ACCESS_SECRET_KEY)
def format_file_name(name):
    return str(uuid.uuid4().hex[:6]+ name)


def upload_to_s3(file):
    try:
        file_name=format_file_name(file.name)
        file.name=file_name
        s3.upload_file(file,settings.AWS_BUCKET_NAME, file_name)
        return f"https://s3.amazonaws.com/{settings.AWS_BUCKET_NAME}/{file_name}"
    except:
        return False
    

def validate_image(image):
    try:
        validate_image_file_extension(image)
        if image.size > settings.IMAGE_FILE_MAX_SIZE:
            return False
        return image
    except:
        return False


def validate_book(book):
    if  not book.endswith('.pdf' or '.docx') or book.size > settings.BOOK_FILE_MAX_SIZE:
        return False
    return book

