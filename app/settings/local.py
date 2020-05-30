import os


BOT_TOKEN = os.getenv('TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
MODEL_FILENAME = os.getenv('MODEL_PATH')
STAGE = os.getenv('STAGE', 'prod')
