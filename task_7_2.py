# 2. *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей
# структурой:
# |--my_project
#   |--settings
#   |   |--__init__.py
#   |   |--dev.py
#   |   |--prod.py
#   |--mainapp
#   |   |--__init__.py
#   |   |--models.py
#   |   |--views.py
#   |   |--templates
#   |       |--mainapp
#   |           |--base.html
#   |           |--index.html
#   |--authapp
#   |   |--__init__.py
#   |   |--models.py
#   |   |--views.py
#   |   |--templates
#   |       |--authapp
#   |           |--base.html
#   |           |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
# текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные
# ситуации, библиотеки использовать нельзя.

import os
import yaml

proj_dict = {
    'my_project':
        [{'settings':
            ['__init__.py', 'dev.py', 'prod.py']},
         {'mainapp':
            ['__init__.py', 'models.py', 'views.py', {'templates':
                                                        [{'mainapp':
                                                            ['base.html', 'index.html']}]}]},
         {'authapp':
            ['__init__.py', 'models.py', 'views.py', {'templates':
                                                        [{'authapp':
                                                            ['base.html', 'index.html']}]}]}
         ]
}

with open('config.yaml', 'w') as f:
    f.write(yaml.dump(proj_dict))

with open('config.yaml') as f:
    starter = yaml.safe_load(f)


def make_starter(input_starter):
    for folder, folders_files in input_starter.items():
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        for folder_file in folders_files:
            if type(folder_file) == dict:
                make_starter(folder_file)
            else:
                if not os.path.exists(folder_file):
                    if '.' in folder_file:
                        with open(folder_file, 'w', encoding='utf-8') as f:
                            f.write('')
    else:
        os.chdir('../')


make_starter(starter)
