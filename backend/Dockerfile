# Gunakan base image yang sudah mendukung Python
FROM python:3.11-slim

# Install library sistem yang dibutuhkan OpenCV agar libGL.so.1 ada
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy sisa file aplikasi
COPY . .

# Jalankan gunicorn dengan shell agar $PORT terbaca sebagai angka
# Mengganti $PORT dengan 8080 secara langsung
CMD ["gunicorn", "--workers", "1", "--timeout", "120", "--bind", "0.0.0.0:8080", "app:app"]
