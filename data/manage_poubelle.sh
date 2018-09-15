#!/usr/bin/env bash
#add schema
curl -X POST -H 'Content-type:text/xml' --data-binary @poubelle_data.xml http://localhost:8983/solr/trash/update?commit=true
#curl -X POST -d @myfilename http://user:pass@myhost/hudson/job/_jobName_/postBuildResult

