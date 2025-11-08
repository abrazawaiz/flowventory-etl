FROM apache/airflow:2.9.3

USER airflow
WORKDIR /app

ENV PYTHONPATH=/app

COPY --chown=airflow:root requirements.txt .

RUN --mount=type=cache,target=/home/airflow/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

COPY --chown=airflow:root ./app ./app
COPY --chown=airflow:root ./data ./data
COPY --chown=airflow:root ./logs ./logs
COPY --chown=airflow:root ./secrets ./secrets
COPY --chown=airflow:root ./dags /opt/airflow/dags

CMD ["bash"]
