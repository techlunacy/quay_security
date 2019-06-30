# Quay security scan
Recieve a list of images in internal format and return a list of CVEs and of the metadata of the images.

## Minimum Requirements: 
1. Python 2.7
2. pip
3. Linux/MacOS

## Installation 
1. pip install -r requirements.txt 

## Run 
As a parameter:  
```  
./quay.py test.json  
```  
Reading from stdin:
```  
cat test.json | ./quay.py 
```
