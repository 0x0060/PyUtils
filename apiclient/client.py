import requests
from requests.exceptions import RequestException
from typing import Any, Dict, Optional
from pyutils.logger.logger import Logger
from pyutils.retrylogic.retry import Retry


class HttpClient:
    def __init__(self, 
                 base_url: str, 
                 timeout: float = 5.0, 
                 max_retries: int = 3, 
                 retry_delay: float = 1.0, 
                 retry_backoff: float = 2.0):
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.retry_backoff = retry_backoff

    @Retry(max_attempts=3, delay=1, backoff=2)
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        url = f"{self.base_url}{endpoint}"
        Logger.client(f"Making GET request to {url} with params: {params}")
        
        try:
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            Logger.client(f"Response from {url}: {response.text}")
            return response.json()  # Assuming JSON response
        except RequestException as e:
            Logger.error(f"GET request failed: {e}")
            raise

    @Retry(max_attempts=3, delay=1, backoff=2)
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Any:
        url = f"{self.base_url}{endpoint}"
        Logger.client(f"Making POST request to {url} with data: {data}")
        
        try:
            response = requests.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            Logger.client(f"Response from {url}: {response.text}")
            return response.json()  # Assuming JSON response
        except RequestException as e:
            Logger.error(f"POST request failed: {e}")
            raise
