
# 📘 Project Design Document – Django Employee Task

## 📂 Project Structure Overview

```
django-employee-task/
│
├── core/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_attendance_performance.py
│   ├── management/commands/
│   │   └── generate_data.py
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
│   ├── __init__.py
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

## 🧱 Components

### 1. **Models**
- `Performance`: Stores performance data for employees.
- Related to `Employee` (likely foreign key).

### 2. **Views**
- `PerformanceViewSet`: A model viewset for full CRUD support and filtering on `rating` and `review_date`.
- `EmployeePerformanceSummary`: API view that returns JSON with employee names and their performance ratings.
- `EmployeePerformanceSummaryChart`: Serves the performance chart HTML template.

### 3. **Templates**
- `emp_performance_chart.html`: Frontend chart visualization (likely rendered with charting library like Chart.js).

### 4. **Serializers**
- Handles serialization/deserialization of `Performance` data for the API.

### 5. **Management Commands**
- `generate_data.py`: Script to populate the database with sample or initial data.

## 🔗 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/performance/` | GET, POST, etc. | ViewSet for Performance data |
| `/api/performance-summary/` | GET | Returns JSON summary of all employee performance |
| `/performance-summary-chart/` | GET | Renders HTML page for chart view |

## 🔐 Permissions
- `EmployeePerformanceSummary` and `EmployeePerformanceSummaryChart` use `AllowAny` (public access). Consider securing these if needed.

## 📊 Chart Visualization
- Data from `EmployeePerformanceSummary` is consumed by the frontend chart rendered in `emp_performance_chart.html`.
- The API sends:
  ```json
  {
    "labels": ["John Doe", "Jane Smith", ...],
    "performance_scores": [4.5, 3.8, ...]
  }
  ```

## 🧪 Testing
- `tests.py` should include unit tests for:
  - API data retrieval.
  - View rendering.
  - Model behavior.

## 🔧 Future Improvements
- Add pagination and filtering to performance API.
- Add authentication and permission checks.
- Improve template UI and integrate live chart updates.
- Write more robust unit and integration tests.
- Include Docker and CI/CD for production readiness.
