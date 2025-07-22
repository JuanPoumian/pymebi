import requests

class GenericConnector:
    def __init__(self, url, username=None, password=None, api_key=None):
        self.url = url
        self.username = username
        self.password = password
        self.api_key = api_key

    def test_connection(self):
        try:
            headers = self._build_headers()
            resp = requests.get(self.url, headers=headers, timeout=5)
            return resp.status_code < 400
        except Exception as e:
            print(f"Generic API Error: {e}")
            return False

    def fetch_data(self, resource, method="GET", params=None, body=None):
        try:
            url = self.url.rstrip("/") + "/" + resource.lstrip("/")
            headers = self._build_headers()
            resp = requests.request(
                method=method.upper(),
                url=url,
                headers=headers,
                params=params,
                json=body,
                timeout=10
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except Exception:
                return resp.text
        except Exception as e:
            print(f"Generic Fetch Error: {e}")
            return None

    def _build_headers(self):
        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers
