ansible-role-dci-quay
=====================

Ansible role to setup Quay on a system. 

## How to use

1) Optional: declare any additional subuids you want to setup
2) Include the role.

```
---
- hosts: localhost
  vars:
    - redis_server_url: '<REDIS_SERVER_URL>'
    - redis_server_port: '<REDIS_SERVER_PORT'
    - redis_password: '<REDIS_PASSWORD>
    - postgres_database_uri: '<POSTGRES_URI>'
    - host_public_ip: '<PUBLIC_IP>'
    - quay_system_user: '<QUAY_SYSTEM_USER>'
    - quay_system_group: '<QUAY_SYSTEM_GROUP>'
    - quay_container_name: '<QUAY_CONTAINER_NAME>'
    - quay_http_port: '<QUAY_HTTP_PORT>'
    - quay_https_port: '<QUAY_HTTPS_PORT>'
    - quay_config_path: '<QUAY_CONFIG_PATH>'
    - quay_image: '<QUAY_IMAGE>'
    - storage_local_path: '<STORAGE_LOCAL_PATH>'
    - database_secret_key: '<DATABASE_SECRET_KEY>'
  tasks:
  - include_role:
      name: ansible-role-dci-quay
```

## Variables

Required:
 - redis_server_url: '<REDIS_SERVER_URL>'
 - redis_server_port: '<REDIS_SERVER_PORT'
 - postgres_database_uri: '<POSTGRES_URI>'
 - host_public_ip: '<PUBLIC_IP>'
 - quay_system_user: '<QUAY_SYSTEM_USER>'
 - quay_system_group: '<QUAY_SYSTEM_GROUP>'
 - quay_container_name: '<QUAY_CONTAINER_NAME>'
 - quay_http_port: '<QUAY_HTTP_PORT>'
 - quay_https_port: '<QUAY_HTTPS_PORT>'
 - quay_config_path: '<QUAY_CONFIG_PATH>'
 - quay_image: '<QUAY_IMAGE>'
 - storage_local_path: '<STORAGE_LOCAL_PATH>'
 - quay_container_storage_path: '<QUAY_CONTAINER_STORAGE_PATH>'

Optional:
 - podman_authfile: '<PODMAN_AUTHFILE>'

If using Swift backend:
 - use_swift: 'true'
 - storage_swift_auth_url: '<SWIFT_AUTH_URL>'
 - storage_swift_auth_version: '<SWIFT_AUTH_VERSION>'
 - storage_swift_region: '<SWIFT_REGION>'
 - storage_swift_tenant_id: '<SWIFT_TENANT_ID>'
 - storage_swift_container: '<SWIFT_CONTAINER>'
 - storage_swift_password: '<SWIFT_PASSWORD>'
 - storage_swift_user: '<SWIFT_USER>'

If using TLS:
 - use_tls: 'true'
 - dci_tls_org: defaults to 'Telco CI"
 - host_fqdn: host name for the Quay service.

## Notes on TLS usage

When TLS is enabled (use_tls: true), the role creates an ad-hoc self-signed cetificate and makes it available both to:

- The Quay instance: by placing it, along with the private key, under the {{ quay_config_path }} directory.
- The ansible controller (jumpbox): by placing it in the local CA trust source directory and updating the trusted CA database.

When creating the certificate, the role uses the variable *host_fqdn* as the common name. You must set it to a FQDN and set the appropriate DNS records in place so all the systems involved in the platform will be able to reach the registry.

If you have a certificate of your own you rather use, you may replace the files *ssl.cert* and *ssl.key* in the quay config path and restart the Quay service:

```
$ sudo systemctl restart dci-quay
```


