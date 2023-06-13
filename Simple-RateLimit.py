#RyDev
import requests
import time
# RateLimiter, limit request per IP
rate_limiter = requests.RateLimiter(
    max_requests=10,
    per=1 * 60,
)
# request to the server.
response = rate_limiter.get('https://example.com')
print(response.status_code)
  