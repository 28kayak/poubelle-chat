#!/usr/bin/env bash
#curl -X POST -H 'Content-type:application/xml' --data-binary @poubelle_schema.xml 'http://localhost:8983/solr/trash/schema'
curl -X POST -H 'Content-type:application/json' --data-binary @poubelle_schema.json 'http://localhost:8983/solr/trash/schema'