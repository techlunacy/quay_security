#!/usr/bin/env python
import json
import pprint
import sys
import requests


def get_security_results(images):
    for image in images:
        repo = "{}/{}".format(image["Organisation"], image["Repository"])
        tag = image['Tag']
        repository_response = requests.get(
            'https://quay.io/api/v1/repository/{}?includeTags=true'.format(repo))
        repository_response.raise_for_status()
        repository = repository_response.json()
        manifest = repository['tags'][tag]['manifest_digest']
        security_results_response = requests.get(
            'https://quay.io/api/v1/repository/{repository}/manifest/{manifest}/security?vulnerabilities=true'.format(repository=repo, manifest=manifest))
        security_results_response.raise_for_status()
        security_results = security_results_response.json()
        image.update(security_results)
        results.append(image)
        return results
pp = pprint.PrettyPrinter(indent=4)
results = []
images = []
if(len(sys.argv) == 2):
    filepath = sys.argv[1]
    with open(filepath, 'r') as outfile:
        images = json.load(outfile)
else:
    images = json.load(sys.stdin)
results = get_security_results(images)
print(json.dumps(results, indent=4, sort_keys=True))
