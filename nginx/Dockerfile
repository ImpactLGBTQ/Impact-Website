FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY impact-website.conf /etc/nginx/conf.d/
COPY uwsgi_params /etc/nginx/conf.d/uwsgi_params

