import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="project3-dbserver.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="azureuser@project3-dbserver" #TODO: Update value
    POSTGRES_PW="aman@123"   #TODO: Update value
    POSTGRES_DB="techconf-db11"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://project3-servicebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=xuF5Pv5Zd2djo3trmQ3LqkqnEGRp1WiV7f452Ms76nA=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'amanchagti135@gmail.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False