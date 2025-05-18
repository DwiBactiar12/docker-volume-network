# Docker Volume & Network - Fullstack Example

Project ini adalah contoh arsitektur microservices sederhana menggunakan Docker Compose, terdiri dari tiga bagian utama:

- **Frontend** (dengan Nginx)
- **Backend** (Flask API)
- **Database** (PostgreSQL)

## Struktur Proyek
docker-volume-network/
│
├── frontend/
│ ├── nginx/
│ │ └── default.conf # Konfigurasi Nginx
│ └── docker-compose.yml # Compose untuk frontend (jika dipisah)
│
├── backend/
│ ├── app.py # Aplikasi Flask utama
│ ├── requirements.txt # Daftar dependencies Python
│ ├── Dockerfile # Dockerfile untuk backend
│ └── docker-compose.yml # Compose untuk backend (jika dipisah)
│
└── database/
  └── docker-compose.yml
