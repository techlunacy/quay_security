#!/usr/bin/env python
import json
import pprint
import sys
import requests
filepath = sys.argv[1]
pp = pprint.PrettyPrinter(indent=4)
results = []
with open(filepath, 'r') as outfile:  
    images = json.load(outfile)
    for image in images:
      repo = "{}/{}".format(image["Organisation"],image["Repository"])
      tag = image['Tag']
      repository = requests.get('https://quay.io/api/v1/repository/{}?includeTags=true'.format(repo)).json()
      manifest = repository['tags'][tag]['manifest_digest']
      # pp.pprint(repository)
      security_results = requests.get('https://quay.io/api/v1/repository/{repository}/manifest/{manifest}/security?vulnerabilities=true'.format(repository=repo,manifest=manifest)).json()
      image.update(security_results)
      results.append(image)
print(json.dumps(results, indent=4, sort_keys=True))