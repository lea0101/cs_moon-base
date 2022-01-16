Python scripts from the Cyberstart America Moon Base --> There are obviously many more, but I didn't save all of them.

When the following is input in the CyberStart python editor:

```

from pip._internal.operations.freeze import freeze
for requirement in freeze(local_only=True):
    print(requirement)

```
    
It returns this:
```
boto3==1.18.55
botocore==1.21.55
jmespath==0.10.0
pip==21.1.1
python-dateutil==2.8.2
rapid-client==0.0.0
s3transfer==0.5.0
setuptools==56.0.0
six==1.16.0
urllib3==1.26.6
```

So I believe thesea are the packages available to us beyond pre-installed python packages, like os and base64. That is why some of these scripts are complicated because the available packages are limited. 
Some of the functions of the os package are also limited.
