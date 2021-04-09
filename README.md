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
