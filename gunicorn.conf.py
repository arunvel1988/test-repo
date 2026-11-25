import os

bind = "0.0.0.0:5000"
worker_class = "gthread"
workers = 2
threads = 2
timeout = 30
graceful_timeout = 30
keepalive = 5
max_requests = 1000
max_requests_jitter = 100
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190
accesslog = "-"
errorlog = "-"
loglevel = "info"
capture_output = True
forwarded_allow_ips = os.getenv("FORWARDED_ALLOW_IPS", "127.0.0.1")
worker_tmp_dir = "/tmp"
