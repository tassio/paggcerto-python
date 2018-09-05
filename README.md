# Paggcerto Python API
The Paggcerto Python API provides convenient access to the Paggcerto API from applications written in the Python language. 

## Quick Install
This lib can be found on pip. To install it, use:


```
$ pip install paggcerto-python
```

## Usage

### Export environment variables

```
export PAGGCERTO_API_USER=...
export PAGGCERTO_API_PASSWORD=...
export PAGGCERTO_API_USE_SANDBOX=True
```

### Creating a Client

```
from paggcert import PaggcertoAPIClient, Client
api = PaggcertoAPIClient()
client = Client(**{
  "cpfCnpj": "31618850075",
  "name": "Maria Joao dos Santos",
  "sex": "F",
  "dateOfBirth": "01/25/1978",
  "phone": "7927667035",
  "cellphone": "79993764596",
  "email": "saragabriellyribeiro_@zf.com",
  "typePerson": "F",
  "zipCode": "49030-720",
  "address": "Avenida Tancredo Neves",
  "number": "10",
  "complement": "Próximo ao conjunto inácio barbosa",
  "neighborhood": "Inacio Barbosa",
  "city": "Aracaju",
  "uf": "SE",
  "note": "O cliente possui apenas um dependente.",
  "paymentMethod": "C"
})
api.client.core.client.register.post(request_body=client.get())
```

## Documentation
- <a href="https://desenvolvedor.paggcerto.com.br/v1">Paggcerto API Docs</a>

