FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        python3-dev \
        g++ \
        curl \
        git \
        libglib2.0-0 \
        libsm6 \
        libxrender1 \
        libxext6 \
        && rm -rf /var/lib/apt/lists/*

# Prevent Python from writing .pyc files & buffer issues
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working dir
WORKDIR /app

# Copy requirements & spaCy model wheel
COPY requirements.txt .
COPY en_core_web_lg-3.6.0-py3-none-any.whl /tmp/

# Upgrade pip first
RUN pip install --upgrade pip setuptools wheel

# Install numpy first
RUN pip install "numpy<2.0"

# Install all other requirements and spaCy model in one step
RUN pip install --no-cache-dir -r requirements.txt && \
        pip install /tmp/en_core_web_lg-3.6.0-py3-none-any.whl

# Copy project files
COPY . .

# Expose port for Django
EXPOSE 8000

# Run Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
