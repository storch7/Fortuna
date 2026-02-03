from notion_client import Client
from config import TOKEN_NOTION
import os

notion = Client(auth=os.environ["TOKEN_NOTION"])