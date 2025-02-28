#!/bin/bash
LOCAL_FILE=$1
BUCKET_NAME=$2
EXPIRATION=$3
aws s3 cp =acl public-read "$LOCAL_FILE" "s3://$BUCKET_NAME/"
FILE_NAME=$(basename "$LOCAL_FILE")
PRESIGNED_URL=$(aws s3 presign "s3://$BUCKET_NAME/$(basename $LOCAL_FILE)" --expires-in "$EXPIRATION")
