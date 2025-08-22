# AURA (Atams Universal Runtime Architecture)

Template backend untuk startup Atams menggunakan FastAPI, PostgreSQL, dan Clean Architecture.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- PostgreSQL 15+
- Redis (optional)
- Docker & Docker Compose (optional)

### Setup dengan Docker

1. Clone repository
```bash
git clone https://github.com/GratiaManullang03/aura.git
cd aura
```

2. Copy environment variables
```bash
cp .env.example .env
# Edit .env sesuai kebutuhan
```

3. Jalankan dengan Docker Compose
```bash
docker-compose up --build
```

API akan berjalan di http://localhost:8000

### Setup Manual (Development)

1. Buat virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Setup database
Pastikan PostgreSQL sudah berjalan dan buat database:
```sql
CREATE DATABASE atabot;
CREATE SCHEMA IF NOT EXISTS atabot;

-- DDL User table sudah ada
CREATE TABLE atabot."user" (
    u_id bigserial NOT NULL,
    u_name varchar NULL,
    u_created_at timestamp DEFAULT now() NOT NULL,
    u_updated_at timestamp NULL,
    CONSTRAINT user_pk PRIMARY KEY (u_id)
);
```

4. Jalankan aplikasi
```bash
uvicorn app.main:app --reload --port 8000
```

## 📚 API Documentation

Setelah aplikasi berjalan, akses:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🔧 Configuration

### Authentication
Auth system menggunakan JWT sebagai skeleton. Untuk customize per client:
1. Edit `app/core/security.py` untuk logic token generation
2. Edit `app/api/deps.py` untuk validation logic
3. Bisa integrate dengan SSO, OAuth2, atau API Key

### Database
- Menggunakan SQLAlchemy ORM
- Support raw SQL untuk query kompleks via `execute_raw_sql()`
- Connection pooling sudah dikonfigurasi

### Redis (Optional)
Redis bisa digunakan untuk:
- Caching
- Session storage
- Rate limiting
- Background tasks dengan Celery

## 📁 Project Structure

```
app/
├── api/          # API endpoints
├── core/         # Core configuration
├── db/           # Database setup
├── models/       # SQLAlchemy models
├── schemas/      # Pydantic schemas
├── repositories/ # Data access layer
└── services/     # Business logic layer
```

## 🧪 Testing

Folder `tests/` sudah disiapkan untuk unit tests dan integration tests.

## 🚢 Deployment

### Production dengan Docker
```bash
docker-compose --env-file .env.prod -f docker-compose.yml up -d --build
```

### Scaling
- Gunakan Nginx sebagai reverse proxy
- Deploy multiple instances dengan load balancer
- Setup Redis untuk shared cache/session

## 📝 Notes

- Template ini tidak overkill, hanya menyediakan struktur dasar yang solid
- Semua dependencies yang di-import benar-benar digunakan
- Auth system adalah skeleton yang bisa disesuaikan per client
- Support hybrid approach: ORM untuk CRUD sederhana, raw SQL untuk query kompleks

## 👥 Contributing

Untuk development lebih lanjut, ikuti Clean Architecture principles:
1. Business logic di `services/`
2. Data access di `repositories/`
3. API contracts di `schemas/`
4. Keep it simple, avoid over-engineering
