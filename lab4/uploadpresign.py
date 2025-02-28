#!/usr/local/bin/python

import boto3
import urlib.request
import sys
s3=boto3.client('s3',region_name='us-east-1')
url=sys.argv[1]
bucket=sys.argv[2]
file_name=url.split("/")[-1]
urlib.request.urlretrieve(url,file_name(
s3.upload_file(file_name, bucket, file_name, ExtraArgs=('ACL': 'punlic-read'})

public_url = f"https://{bucket}.s3.amazonaws.com/{file_name}"
print(public_url)
