# Amazon S3 Integration Documentation

## Overview

This document provides comprehensive information about the integration of Amazon S3 into the application. It covers the purpose of the integration, setup instructions, and usage for various functionalities such as file uploads, downloads,
and image processing workflows.

---

## 1. Introduction

Amazon Simple Storage Service (S3) is used for scalable, secure, and highly available object storage. In this application, S3 is integrated for:

- Uploading and storing image files.
- Generating pre-signed URLs for secure file access.
- Organizing images into structured folders.
- Enabling workflows for image processing and database updates.

---

## 2. Prerequisites

To use the S3 integration, ensure the following:

### Required Tools and Access

- **AWS Account**: Ensure you have an active AWS account.
- **IAM User or Role**: Create an IAM user or role with the required permissions for S3. Attach the `AmazonS3FullAccess` policy or a custom policy that grants the necessary access.
- **AWS CLI**:(Optional)

  - Install the AWS Command Line Interface (CLI):

    ```bash
    pip install awscli
    ```

  - Configure the CLI with your AWS credentials:

    ```bash
    aws configure
    ```

- **Python Libraries**:

  - Ensure you have the following Python libraries installed:

    ```bash
    pip install boto3 python-dotenv opencv-python-headless numpy
    ```

### S3 Bucket Setup

1. **Create an S3 Bucket**:

   - Log in to the AWS Management Console.
   - Navigate to the **S3** service.
   - Click **Create bucket** and provide a unique bucket name.
   - Select the desired AWS region.
   - Configure bucket options (e.g., versioning, encryption).

2. **Set Bucket Policies**:

   - Grant access permissions by defining a bucket policy. Example policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::970547383153:root"
      },
      "Action": ["s3:PutObject", "s3:GetObject", "s3:ListBucket", "s3:DeleteObject"],
      "Resource": ["arn:aws:s3:::fabric-storage-bucket", "arn:aws:s3:::fabric-storage-bucket/*"]
    }
  ]
}
```

-

1. **Enable CORS Configuration**:

   - Configure Cross-Origin Resource Sharing (CORS) for the bucket if required. Example:

```json
[
  {
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["GET", "PUT", "POST", "DELETE", "HEAD"],
    "AllowedOrigins": ["*"],
    "ExposeHeaders": ["ETag"]
  }
]
```

## 📘 Creating a Custom IAM User Policy in AWS Console

This guide walks you through the steps to create a custom IAM policy that grants specific S3 bucket access using the AWS Management Console.

Grant the IAM user fabric_search_user permissions to interact with a specified Amazon S3 bucket (e.g., list, read, write, and delete objects).

Prerequisites
You must have sufficient AWS IAM permissions to manage users and policies.

The S3 bucket name should be known (e.g., fabric-storage-bucket).

📝 Steps to Attach the IAM Policy

1. Go to the IAM Console
   Open this URL:
   <https://console.aws.amazon.com/iam/users>

2. Select Your User
   Find and click on the IAM user:
   `fabric_search_user` or `custom_user`

3. Navigate to the “Permissions” Tab
   In the user details page, click on the Permissions tab.

4. Start the Add Permissions Workflow
   Click the “Add permissions” button.
   Then choose:

   - Attach policies directly

5. Create a New Policy
   Click “Create policy” (located at the bottom left of the page).
   This will open the policy creation interface.

6. Switch to the JSON Editor
   Click the “JSON” tab.

Replace the default policy with the following:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowFabricBucketAccess",
      "Effect": "Allow",
      "Action": ["s3:ListBucket", "s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
      "Resource": ["arn:aws:s3:::fabric-storage-bucket", "arn:aws:s3:::fabric-storage-bucket/*"]
    }
  ]
}
```

🔁 Important: Replace `fabric-storage-bucket `with your actual S3 bucket name if different.

1. Name and Create the Policy
   Click “Next”, then provide a name for your policy.
   📄 Example: FabricS3AccessPolicy
   Then click “Create policy” to save it.

2. Attach the Policy to the User

   - Go back to the IAM user: `fabric_search_user` or `custom_user`

   - Click Add permissions again

   - Choose: Attach existing policies directly

   - Search for the policy you just created (FabricS3AccessPolicy)

   - Check the box next to the policy

   - Click Add permissions

✅ Verification
After attaching the policy, verify the user has the correct permissions by:

Navigating to the user’s Permissions tab

Confirming that FabricS3AccessPolicy appears in the attached policies list

1. **Enable Versioning**:

   - Turn on versioning to keep multiple versions of an object in the bucket.

---

## 3. Environment Variables

The application uses environment variables for secure configuration. Add the following variables to a `.env` or`constants.py` file:

```env
AWS_ACCESS_KEY_ID=<your-access-key-id>
AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
AWS_REGION=<your-region>

```

---

## 4. AWS S3 Bucket Structure

The S3 bucket is structured into the following folders:

- **search_uploads/**: Stores original uploaded images.
- **generated/**: Stores processed/generated images.
- **single_images/**: Stores single image files uploaded by users.
- **group_images/**: Stores grouped image files for processing.
- **table/fabric_table**: Stores metadata.

### Example

```bash
fabric-storage-bucket
├── search_uploads/
├── generated/
└── uploaded/single_images/
├── uploaded/group_images/
└── table/fabric_table/

```

---

## 5. Key Features

### 5.1 File Upload to S3

Allows uploading files to specific S3 folders.

- Function: `upload_file_to_s3(file, bucket_name, s3_key)`
- Parameters:
  - `file`: File object to be uploaded.
  - `bucket_name`: Name of the S3 bucket.
  - `s3_key`: Path (key) within the bucket.
- Returns: `True` on success, `False` otherwise.

### 5.2 Generate Pre-Signed URLs

Generates secure, temporary URLs for accessing S3 objects.

- Function: `generate_presigned_url(bucket_name, object_key, expiration=3600)`
- Parameters:
  - `bucket_name`: Name of the S3 bucket.
  - `object_key`: Path (key) within the bucket.
  - `expiration`: Time in seconds before the URL expires (default: 3600).
- Returns: URL string or `None` on failure.

### 5.3 List Objects in S3

Lists objects in specific folders of the S3 bucket.

- Example folders: `single_images`, `group_images`, `generated`.
- Usage within API endpoints like `/image/list`.

### 5.4 Process and Store Images

Processes uploaded images, generates new images, and stores them in the `generated/` folder.

---

## 7. Helper Functions

### 7.1 Upload to S3

```python
def upload_file_to_s3(file, bucket_name, s3_key):
    try:
        s3_client.upload_fileobj(file, bucket_name, s3_key)
        return True
    except Exception as e:
        logger.error(f"S3 Upload Failed: {e}")
        return False
```

### 7.2 Generate Pre-Signed URL

```python
def generate_presigned_url(bucket_name, object_key, expiration=3600):
    try:
        return s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": object_key},
            ExpiresIn=expiration,
        )
    except Exception as e:
        logger.error(f"Pre-Signed URL Generation Failed: {e}")
        return None
```

---

## 8. Error Handling

- **File Upload Errors**: Returns 500 with descriptive messages.
- **Pre-Signed URL Failures**: Returns 500 if URL generation fails.
- **S3 Object Listing Issues**: Logs the stack trace and returns 500.

## 10. Best Practices

- Use IAM roles with least privilege for accessing S3.
- Validate all user inputs.
- Enable S3 versioning for important data.
- Use lifecycle policies to manage storage costs.

---

## 11. Troubleshooting

### Common Issues

1. **Access Denied Errors**:

   - Ensure the AWS access key and secret key have proper permissions.
   - Check S3 bucket policies.

2. **File Not Found in S3**:
   - Verify the folder structure and `s3_key`.
