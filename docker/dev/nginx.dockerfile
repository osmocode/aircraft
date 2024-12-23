FROM nginx

# Change location of nginx template output files
ENV NGINX_ENVSUBST_OUTPUT_DIR=/etc/nginx

# Remove default configuration
RUN rm /etc/nginx/conf.d/default.conf

# Add custom certificates
COPY ../config/nginx/certs            /etc/nginx/certs
# Add custom configuration templates
COPY ../config/nginx/custom-templates /etc/nginx/custom-templates

# Add custom template generator script
COPY ../config/nginx/docker-entrypoint.d/1-custom-template-generator.sh /docker-entrypoint.d/1-custom-template-generator.sh
RUN chmod +x /docker-entrypoint.d/1-custom-template-generator.sh

# Forward nginx logs to docker
# https://alexanderallen.medium.com/forwarding-nginx-logs-to-docker-3bb6283a207
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log
