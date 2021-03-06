freedomofpress.kibana
=====================

[![CircleCI](https://circleci.com/gh/freedomofpress/ansible-role-kibana.svg?style=svg&circle-token=95f31e6b9e0e8b11b68ec29b8fc54537c46841f3)](https://circleci.com/gh/freedomofpress/ansible-role-kibana)

Ansible role to install and configure kibana. 

Role Variables
--------------

```
---
# Packaging options
kibana_major_version: "5.x"
kibana_version: "5.5.0"
kibana_pkg_lock: false
kibana_pkg_name: kibana
kibana_pkg_deps: []
kibana_elastic_pgp: "46095ACC8548582C1A2699A9D27D666CD88E42B4"
kibana_pgp_keyserver: pgp.mit.edu
kibana_elastic_repo: "deb https://artifacts.elastic.co/packages/{{ kibana_major_version }}/apt stable main"

kibana_config_server:
  server.port: 5601
  server.host: "localhost"
  # server.basePath: ""
  server.maxPayloadBytes: 1048576
  # server.name: "your-hostname"

kibana_config_es:
  elasticsearch.url: "http://localhost:9200"
  elasticsearch.preserveHost: true
  elasticsearch.requestTimeout: 30000
  # elasticsearch.pingTimeout: 1500
  # elasticsearch.username: "user"
  # elasticsearch.password: "pass"
  # elasticsearch.ssl.certificate: /path/to/your/client.crt
  # elasticsearch.ssl.key: /path/to/your/client.key
  # elasticsearch.ssl.certificateAuthorities: [ "/path/to/your/CA.pem" ]
  # elasticsearch.ssl.verificationMode: full
  # elasticsearch.requestHeadersWhitelist: [ authorization ]
  # elasticsearch.customHeaders: {}
  # elasticsearch.shardTimeout: 0
  # elasticsearch.startupTimeout: 5000

kibana_config_misc:
  kibana.index: ".kibana"
  kibana.defaultAppId: "discover"
  ops.interval: 5000
  i18n.defaultLocale: "en"
  # server.ssl.enabled: false
  # server.ssl.certificate: /path/to/your/server.crt
  # server.ssl.key: /path/to/your/server.key
  # pid.file: /var/run/kibana.pid

kibana_config_logging:
  # logging.dest: stdout
  logging.silent: false
  logging.quiet: false
  logging.verbose: false

kibana_config: "{{ kibana_config_es|combine(kibana_config_server)|combine(kibana_config_misc)|combine(kibana_config_logging) }}"
```

Dependencies
------------

This is one piece of an ELK deployment. I advise that you seek other for elasticsearch and logstash.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: freedomofpress.kibana

License
-------

MIT

Author Information
------------------

Michael Sheinberg <@msheiny>
Freedom of the Press Foundation
