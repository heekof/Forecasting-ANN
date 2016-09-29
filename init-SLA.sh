#!/bin/bash

mkdir -p SLA-descriptor/SLO
mkdir -p SLA-descriptor/metrics
mkdir -p SLA-descriptor/profiles
mkdir -p SLA-descriptor/vars
touch service-descriptor
touch services
touch sla.cfg
touch SLA-descriptor/SLO/service-name-slo.yaml
touch SLA-descriptor/metrics/main.yaml
touch SLA-descriptor/profiles/basic.yaml
touch SLA-descriptor/profiles/gold.yaml
touch SLA-descriptor/vars/all

echo "---
  include metrics
  include service
  include profiles
    - service: service-name
      actors:
      actions:
      profiles: name=basics
      slo:
        - name: xxxxxxxxxx
          time: start= end= format=Unix
          metric: name=cpu
            - condition: predicat=less percentile=0.2
            - threshold: avg=true value=2
" > SLA-descriptor/SLO/service-name-slo.yaml
