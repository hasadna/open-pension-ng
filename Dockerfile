# Pulled Apr 24, 2023
FROM python:3.8@sha256:6aea47c16a4fe8a30f184060a2347caa24ea156b224041543fdc6b901dbec699
WORKDIR /srv
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt && rm requirements.txt
COPY djang ./djang
WORKDIR /srv/djang
ENTRYPOINT ["/srv/djang/entrypoint.sh"]
