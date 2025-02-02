# Django FAQ API

## 🚀 Objective

This project is a Django-based FAQ management system with multilingual support, a WYSIWYG editor, caching, and a REST API. The goal is to:

- Design and implement Django models with WYSIWYG editor support.
- Store and manage FAQs with multi-language translation.
- Follow PEP8 conventions and best practices.
- Write a clear and detailed README.
- Use proper Git commit messages.

## 📌 Features

- **FAQ Model:** Stores questions, answers, and multilingual translations.
- **WYSIWYG Editor:** Uses `django-ckeditor` for rich-text formatting.
- **REST API:** Supports filtering, sorting, pagination, and language selection via `?lang=`.
- **Caching Mechanism:** Uses Redis for optimized performance.
- **Multi-language Support:** Translates FAQs using Google Translate API.
- **Admin Panel:** User-friendly Django admin interface for managing FAQs.
- **Unit Testing:** Uses `pytest` for API and model testing.
- **Docker Support:** `Dockerfile` and `docker-compose.yml` included for easy deployment.

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/NAIDU0019/BHARATFD.git
cd BHARATFD
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Run Development Server

```bash
python manage.py runserver
```

### 6️⃣ Run Tests

```bash
pytest
```

## 🔥 API Endpoints

### 1️⃣ Retrieve All FAQs

```http
GET /api/faqs/
```

**Optional Query Parameters:**

- `?lang=es` (Spanish translation)
- `?filter=keyword` (Filter by keyword)
- `?sort=question` (Sort by question text)
- `?page=1` (Pagination)

### 2️⃣ Create a New FAQ

```http
POST /api/faqs/
```

**Request Body:**

```json
{
  "question": "What is Django?",
  "answer": "Django is a high-level Python web framework."
}
```

### 3️⃣ Retrieve a Single FAQ

```http
GET /api/faqs/{id}/
```

### 4️⃣ Update an FAQ

```http
PUT /api/faqs/{id}/
```

### 5️⃣ Delete an FAQ

```http
DELETE /api/faqs/{id}/
```

## 🔄 Caching with Redis

This project uses Redis for caching translations.
To start Redis:

```bash
redis-server
```

Ensure `settings.py` is configured correctly:

```python
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
    }
}
```

## 📝 Git Commit Best Practices

- Use meaningful commit messages:

```bash
git commit -m "feat: Add multilingual FAQ model"
```

- Follow atomic commits and proper branching strategies.

## 🚀 Deployment (Docker & Heroku)

### 1️⃣ Build and Run with Docker

```bash
docker-compose up --build
```

### 2️⃣ Deploy to Heroku (Optional)

```bash
git push heroku main
```

## 🤝 Contribution Guidelines

- Fork the repository.
- Create a new branch (`feat-new-feature`).
- Commit changes with proper messages.
- Submit a pull request.

---

**Maintainer:** [Your Name](https://github.com/NAIDU0019)
