
import os
import logging

import python_http_client

from .client import Client


logger = logging.getLogger("paggcerto")


try:
    API_USER = os.environ["PAGGCERTO_API_USER"]
    API_PASSWORD = os.environ["PAGGCERTO_API_PASSWORD"]
    API_USE_SANDBOX = os.environ.get("PAGGCERTO_API_USE_SANDBOX", True)
except KeyError:
    raise Exception(
        "Required environment variables PAGGCERTO_API_USER and PAGGCERTO_API_PASSWORD"
    )


PRODUCTION_HOST = 'https://api-recorrencia.paggcerto.com.br/v1/'
SANDBOX_HOST = 'https://sandbox-recorrencia.paggcerto.com.br/v1/'


class PaggcertoAPIClient:

    def __init__(self, api_user=API_USER, api_password=API_PASSWORD, use_sandbox=API_USE_SANDBOX):
        self._api_user = api_user
        self._api_password = api_password

        self._use_sandbox = API_USE_SANDBOX

        self._token = None

        self._client = python_http_client.Client(
            host=SANDBOX_HOST if self._use_sandbox else PRODUCTION_HOST
        )

    @property
    def client(self):
        if not self._token:
            self._token = self._request_token()

            self._client.request_headers = {
                "Authorization": f"Bearer {self._token}"
            }

        return self._client

    def _request_token(self):
        try:
            response = self._client.core.auth.post(request_body={
                'username': self._api_user,
                'pass': self._api_password
            })
            return response.to_dict['token']
        except Exception:
            logger.exception(f"error on auth {e.to_dict}")
            raise
