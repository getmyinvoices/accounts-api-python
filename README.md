# accounts-api-python

This repository serves as a python API client for the GetMyInvoices API v2. 
Visit the [documentation](https://api.getmyinvoices.com/accounts/v2/doc/#)
for further information.


### Install
To simply integrate this library into your project, you can install it via 
[pip](https://pypi.org/project/pip/): 
```
pip install getmyinvoices
```

### How to use
To initiate an API client, create an `GMI` instance with an access token:
```
GMI("XXXX-XXXX-XXXX-XXXX-XXXX")
```

Example usage:
```
gmi = GMI("XXXX-XXXX-XXXX-XXXX-XXXX")
gmi.api_status()
```

##### Maintainer
[Ben Barten](mailto:bba@fino.digital)
