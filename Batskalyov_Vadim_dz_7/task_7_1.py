# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
# |--settings
# |--mainapp
# |--adminapp
# |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как
# лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
# папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
# данные о вложенных папках и файлах (добавлять детали)?

import os
import json

proj_dict = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}

with open('proj.json', 'w') as f:
    json.dump(proj_dict, f)

with open('proj.json') as f:
    starter = json.load(f)

for root, folders in starter.items():
    if not os.path.exists(root):
        for folder in folders:
            folder_path = os.path.join(root, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
