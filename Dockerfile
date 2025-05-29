FROM python:3.13-slim-bullseye AS build-venv

WORKDIR /app

COPY src/requirements.txt .

RUN apt update && \
    apt install build-essential -y && \
    rm -rf /var/lib/apt/lists/*

#RUN python3.13 -m venv venv && \
#    venv/bin/pip3.13 install --upgrade pip setuptools wheel && \
#    venv/bin/pip3.13 install --disable-pip-version-check --no-cache-dir gunicorn[gevent] && \
#    venv/bin/pip3.13 install --disable-pip-version-check --no-cache-dir -r requirements.txt
RUN pip3.13 install --upgrade pip setuptools wheel && \
    pip3.13 install --disable-pip-version-check --no-warn-script-location --no-cache-dir --user gunicorn[gevent] && \
    sed -i 's/^psycopg2\(.*\)$/psycopg2-binary\1/' requirements.txt && \
    pip3.13 install --disable-pip-version-check --no-warn-script-location --no-cache-dir --user -r requirements.txt

#FROM gcr.io/distroless/python3-debian12:debug
#FROM python:3.13-alpine
FROM python:3.13-slim-bullseye

LABEL maintainer="yuangezhizao <root@yuangezhizao.cn>"

#COPY --from=build-venv /app/venv /app/venv
COPY --from=build-venv /root/.local /root/.local

WORKDIR /app

COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#ENV PATH=/app/venv/bin:$PATH
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000

HEALTHCHECK --timeout=10s --interval=30s --retries=3 CMD curl http://localhost:5000 || exit 1

CMD ["gunicorn", "--worker-class", "gevent", "--workers", "8", "--bind", "0.0.0.0:5000", "--pythonpath", "/app/src", "maimai_DX_CN_probe:create_app()", "--max-requests", "10000", "--timeout", "5", "--keep-alive", "5", "--log-level", "info"]
