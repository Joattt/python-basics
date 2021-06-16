# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
# «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
# templates, например:
# |--my_project
# ...
# |--templates
# | |--mainapp
# | | |--base.html
# | | |--index.html
# | |--authapp
# | |--base.html
# | |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
# расположены в родительских папках (они играют роль пространств имён); предусмотреть
# возможные исключительные ситуации; это реальная задача, которая решена, например, во
# фреймворке django.

import os
import shutil

templates_path = os.path.join('my_project', 'templates')

if not os.path.exists(templates_path):
    os.mkdir(templates_path)

for root, dirs, files in os.walk('my_project'):
    if root != r'my_project\templates\authapp' and root != r'my_project\templates\mainapp':
        for file in files:
            if file.lower().endswith('.html'):
                file_path = os.path.join(root, file)
                file_name = os.path.basename(file_path)
                dir_name = os.path.basename(os.path.dirname(file_path))
                new_dir_path = os.path.join(templates_path, dir_name)
                if not os.path.exists(new_dir_path):
                    os.mkdir(new_dir_path)
                shutil.copy(file_path, new_dir_path)
