import os

SPIGOTMC_LOGIN = os.environ.get('SPIGOTMC_LOGIN')
SPIGOTMC_PASSWORD = os.environ.get('SPIGOTMC_PASSWORD')

FLARESOLVERR_URL = os.environ.get('FLARESOLVERR_URL')

DESTINATION = os.environ.get('DESTINATION')
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")


if DESTINATION == 'basic':
    OUTPUT_FOLDER = os.environ.get("OUTPUT_FOLDER")

elif DESTINATION == 's3':
    S3_ENDPOINT = os.environ.get("S3_ENDPOINT")
    S3_BUCKET = os.environ.get("S3_BUCKET")
    S3_REGION = os.environ.get("S3_REGION")
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")    

else:
    raise Exception("blablabla pas bonne config")
