
# 📘 Learning Django REST Framework

This repository contains my personal practice projects and code snippets while learning Django REST Framework (DRF). It serves as a learning log to understand how to build RESTful APIs using Django.

---

## 🧠 Purpose

This project is not meant for production or public use. It's a personal sandbox where I explore and understand the following DRF concepts:

- Django project and app setup
- Creating models and migrations
- Writing serializers
- Building API views (Function-Based Views, Class-Based Views, ViewSets)
- Using routers and URLs
- CRUD operations
- Authentication (Token, Session)
- Permissions & throttling
- Pagination
- API testing with Postman / DRF's built-in browser

---

## 🛠 Tech Stack

- Python 3.x  
- Django  
- Django REST Framework  

---

## 📁 Folder Structure

```
learning-drf/
├── api/                  # Django app for API-related code
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── learning_drf/         # Project settings
│   ├── settings.py
│   ├── urls.py
├── manage.py
```

---

## 🚀 Getting Started (for personal reference)

1. Create virtual environment  
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

2. Install dependencies  
   ```bash
   pip install django djangorestframework
   ```

3. Run server  
   ```bash
   python manage.py runserver
   ```

---

# 📘 Django REST Framework (DRF) – Complete Learning Notes

This is a personal reference guide covering all essential concepts needed to master Django REST Framework (DRF) for building RESTful APIs using Django.

---

## 🔧 1. What is Django REST Framework?

Django REST Framework (DRF) is a powerful and flexible toolkit for building Web APIs on top of Django.

---

## 📦 2. Installation

```bash
pip install djangorestframework
```

Add to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

---

## 🧱 3. Core Components of DRF

| Component      | Purpose                                  |
|----------------|-------------------------------------------|
| `Serializer`   | Converts complex data (e.g. models) to JSON, and vice versa |
| `APIView`      | Base class for class-based views          |
| `ViewSet`      | Simplified view structure for CRUD APIs   |
| `Router`       | Auto-generates URLconf for ViewSets       |
| `Permissions`  | Control access to API endpoints           |
| `Authentication` | Handles user verification (token, session, etc.) |
| `Pagination`   | Limits number of results per page         |
| `Throttling`   | Rate-limiting for API usage               |

---

## 🔤 4. Serializers

- Convert Django model instances or other data to JSON
- Validate incoming data
- Save validated data to DB

**ModelSerializer example:**

```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```

---

## 👁️ 5. Views

### Function-Based Views (FBV)

```python
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
```

### Class-Based Views (CBV)

```python
class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
```

### ViewSets + Routers

```python
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

```python
router = DefaultRouter()
router.register(r'books', BookViewSet)
urlpatterns = router.urls
```

---

## 🔐 6. Authentication

### Built-in types:

- SessionAuthentication (default in browsable API)
- TokenAuthentication

```bash
pip install djangorestframework authtoken
```

```python
from rest_framework.authtoken.views import obtain_auth_token
path('api-token-auth/', obtain_auth_token),
```

---

## 🔒 7. Permissions

Examples:
- `AllowAny`
- `IsAuthenticated`
- `IsAdminUser`
- `IsAuthenticatedOrReadOnly`

Set in settings:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

---

## 📃 8. Pagination

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

---

## 📉 9. Filtering, Searching, Ordering

Install:
```bash
pip install django-filter
```

In settings:

```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
```

In views:

```python
filterset_fields = ['author', 'genre']
search_fields = ['title', 'description']
ordering_fields = ['price']
```

---

## 🔁 10. Throttling (Rate Limiting)

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '100/day',
    }
}
```

---

## 🧪 11. API Testing Tools

- **DRF Browsable API** (built-in)
- **Postman**
- **cURL**
- **Swagger** / **Redoc** (with drf-yasg or drf-spectacular)

---

## ✅ 12. Best Practices

- Use `ViewSets + Routers` for CRUD APIs
- Use `ModelSerializer` unless custom logic is needed
- Use pagination for large datasets
- Use proper authentication & permission controls
- Use throttling for public APIs
- Modularize large projects (split serializers, views, permissions, urls)

---

## 🛠 13. Useful Commands

```bash
python manage.py startapp api
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 📚 14. Resources

- [Official DRF Docs](https://www.django-rest-framework.org/)
- [DRF Cheat Sheet](https://cheatography.com/)

---

## 📅 Notes

This file is for personal study and quick revision. Keep updating as you learn new features or patterns.
