import os
from pathlib import Path

project_name = "flipkart_bot"

list_of_files = [
    f"app/{project_name}/__init__.py",
    f"app/{project_name}/data_converter.py",
    f"app/{project_name}/data_ingestion.py",
    f"app/{project_name}/retrieval_generation.py",
    "app/static/style.css",
    "app/templates/chat.html",
    "app/setup.py",
    "app/app.py",
    "app/requirements.txt",
    "app/.env"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok= True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass