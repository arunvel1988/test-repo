FROM python:3.12-slim-bookworm@sha256:44cf1793efa7c7a476bb0f2cff81443f4a072c90c1cb127e2924933daa3e8c64

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --require-hashes --no-cache-dir -r requirements.txt \
    && useradd --create-home --uid 10001 --shell /usr/sbin/nologin app

COPY --chown=app:app app.py gunicorn.conf.py ./

USER app

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000/health', timeout=2).read()" || exit 1

CMD ["gunicorn", "--config", "gunicorn.conf.py", "app:app"]
