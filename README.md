Установка

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/DarhannnJ/endpoint.git
   cd endpoint
   ```
2. Создай виртуальное окружение и установи зависимости:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # или venv\Scripts\activate  # Windows
   pip install fastapi uvicorn
   ```
3. Запусти сервер:
   ```bash
   uvicorn main:app --reload
   ```
4. Открой в браузере:
   ```bash
   http://localhost:8000/masters
   ```
