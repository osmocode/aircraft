#!/bin/sh

set -e

entrypoint_log() {
  if [ -z "${NGINX_ENTRYPOINT_QUIET_LOGS:-}" ]; then
    echo "$@"
  fi
}

gen_configuration() {

  local config="$1"
  entrypoint_log "Loading configration for: $config"

  local cert_dir="/etc/nginx/certs/$config"

  # Check if the cert directory exists
  if [ ! -d $cert_dir ]; then
    entrypoint_log "Cert directory is missing at: /etc/nginx/certs/$config"
    return 1
  fi

  # Check if any files exist in the cert directory
  if [ ! "$(ls -A $cert_dir)" ]; then
    entrypoint_log "Cert directory is empty at: /etc/nginx/certs/$config"
    return 1
  fi

  # Check if the config file exists
  local config_file="/etc/nginx/custom-templates/nginx.$config.conf"
  if [ ! -f $config_file ]; then
    entrypoint_log "Config is missing at: /etc/nginx/custom-templates/nginx.$config.conf"
    return 1
  fi

  # Create template directory if not exists
  if [ ! -d /etc/nginx/templates ]; then
    mkdir -p /etc/nginx/templates
  fi

  # Copy the config file to the template directory
  local template_suffix="${NGINX_ENVSUBST_TEMPLATE_SUFFIX:-.template}"
  cat $config_file > /etc/nginx/templates/nginx.conf$template_suffix
  return 0

}

if [ ! -z $NGINX_CUSTOM_CONFIG ]; then
  if gen_configuration $NGINX_CUSTOM_CONFIG; then
    exit 0
  fi
fi

if [ ! -z $NGINX_DEFAULT_CONFIG ]; then
  if gen_configuration $NGINX_DEFAULT_CONFIG; then
    exit 0
  fi
fi

if gen_configuration "default"; then
  exit 0
fi

entrypoint_log "No valid configuration found, exiting..."
exit 1
