
# 🚀 Django Employee Task

A Django-based web application for tracking and visualizing employee performance data.

## 📦 Features

- CRUD operations for employee performance records
- API endpoint providing performance data in JSON format
- Chart visualization using a Django template
- Custom Django management command to seed data

## 📂 Project Structure

```
django-employee-task/
│
├── core/
│   ├── migrations/
│   ├── management/commands/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
├── employee_backend/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│
├── templates/
│   └── data_chart/
│       └── emp_performance_chart.html
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── venv/
```

## 🔗 Key Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/performance/` | GET, POST, PUT, DELETE | Manage performance records |
| `/api/performance-summary/` | GET | Get summary data for charting |
| `/performance-summary-chart/` | GET | Render performance chart HTML |

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd django-employee-task
   ```

2. **Create virtual environment and activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Generate sample data (optional)**
   ```bash
   python manage.py generate_data
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - API: `http://127.0.0.1:8000/api/performance-summary/`
   - Chart: `http://127.0.0.1:8000/performance-summary-chart/`

## 🧪 Running Tests

```bash
python manage.py test
```

## 🙌 Contributions

Feel free to fork this project and submit pull requests. Feedback and contributions are welcome!

## 📝 License

This project is licensed under the MIT License.
