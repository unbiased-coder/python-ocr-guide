import boto3_helper

print ('Initializing boto3 session...')
session = boto3_helper.init_aws_session()

print ('Getting Textract client...')
textract = session.client('textract')


s3_obj = { 
    'Bucket': 'unbiased-coder-bucket', 
    'Name': 'sample-ocr.png'
}

print ('Setting up object location: ', s3_obj)

doc_info = {
    'S3Object': s3_obj
}

print ('Processing document: ', doc_info)
ret = textract.detect_document_text(Document=doc_info)

print ('Received result: ')
for item in ret['Blocks']:
    if item["BlockType"] == "LINE":
        print (item["Text"])
