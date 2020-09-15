'''import sys
sys.path.insert(0, './games')
from games import *'''

'''import pkgutil
search_path = ['./games'] # Используйте None, чтобы увидеть все модули, импортируемые из sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print(all_modules)
for module in all_modules:
    try:
        s = f'import Bet'
        eval(s)
    except:
        raise
        print(f'Не удалось добавить игру {module}')'''
def load(dir) -> list:
  from os import listdir as ls
  py_files = [m[:-3] for m in ls(dir) if m[-3:]=='.py']
  return [getattr(__import__(dir+'.'+m), m) for m in py_files]

for m in load('games'):
    print(m)
    m.info()