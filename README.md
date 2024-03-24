# Установка

### Чтобы использовать проект, следуйте приложенным инструкциям:
- Создайте папку и склонируйте туда репозиторий:

```sh
mkdir project-tp
cd project-tp
git clone git@gitlab.akhcheck.ru:ilya.ivanov/project-tp.git
```

- После этого зайдите в папку и выберите ветку main

```sh
cd src
git checkout main
```

- Чтобы установить все необходимые модули, используйте:

```sh
python -m venv venv
```
для Linux/MacOs:
```sh
source venv/bin/activate
```
для Windows:
```sh
venv\Scripts\activate.bat
```
Затем
```sh
pip install -r requirements.txt 
chmod +x main.py
```

- Запуск игры
```sh
python3 main.py
```

