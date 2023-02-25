## Тестовое задание для Saber Interactive 

### Установка и запуск:

 - Клонируйте репозиторий на свою локальную машину и перейдите в директорию проекта:
```sh
git clone https://github.com/aimerkz/merge-logs-test.git
cd merge-logs-test
```

- Cоздайте и активируйте виртуальное окружение:
```sh
python3 -m venv venv
source venv/Scripts/activate
```

- Запустите скрипт для генерации файлов с логами:
```sh
python log_genetator.py ./static
```

- Запустите скрипт для слияния сгенерированных файлов:
```sh
python main.py static/log_a.jsonl static/log_b.jsonl -o ./result
```
