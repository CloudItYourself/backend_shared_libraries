import logging
import aioboto3


async def check_if_s3_file_exists(bucket_name: str, key: str, access_key: str, secret_key: str, url: str,
                                  logger_name: str) -> bool:
    session = aioboto3.Session()
    s3_client = session.client('s3',
                               aws_access_key_id=access_key,
                               aws_secret_access_key=secret_key,
                               endpoint_url=url)

    try:
        await s3_client.head_object(Bucket=bucket_name, Key=key)
        return True
    except s3_client.exceptions.ClientError as e:
        if e.response['Error']['Code'] != '404':
            logging.getLogger(logger_name).error(f"Error checking for {key} in {bucket_name}, error: {e}")
        return False

def s3_download_file(bucket_name: str, key: str, access_key: str, secret_key: str, url: str, dest_file: pathlib.Path):
    s3_client = boto3.client('s3',
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key,
                             endpoint_url=url)
    dest_file.parent.mkdir(parents=True, exist_ok=True)
    s3_client.download_file(bucket_name, key, str(dest_file.absolute()))