from model.api.notion_api import notion
import json

print(json.dumps(notion.users.list(),indent=2, ensure_ascii=False))