FROM open-pension-ng
RUN DJANGO_STATIC_ROOT=/srv/static python manage.py collectstatic --noinput -c
# Pulled Apr 24, 2023
FROM nginx@sha256:63b44e8ddb83d5dd8020327c1f40436e37a6fffd3ef2498a6204df23be6e7e94
COPY --from=0 /srv/static /usr/share/nginx/html/static
RUN rm /usr/share/nginx/html/*.html
