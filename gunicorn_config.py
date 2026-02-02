"""
Gunicorn Configuration for Production
"""
import multiprocessing
import os

# Server socket
bind = os.getenv('BIND', '0.0.0.0:8000')
backlog = 2048

# Worker processes
workers = int(os.getenv('WEB_CONCURRENCY', multiprocessing.cpu_count() * 2 + 1))
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

# Process naming
proc_name = 'flask-starter'

# Logging
accesslog = os.getenv('ACCESS_LOG', '/var/log/gunicorn/access.log')
errorlog = os.getenv('ERROR_LOG', '/var/log/gunicorn/error.log')
loglevel = os.getenv('LOG_LEVEL', 'info')
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
daemon = False
pidfile = os.getenv('PIDFILE', '/tmp/gunicorn.pid')
umask = 0o007
user = None
group = None

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# SSL (if using HTTPS)
keyfile = None
certfile = None
ssl_version = 2
cert_reqs = 0
ca_certs = None
suppress_ragged_eofs = True
do_handshake_on_connect = False

# Server hooks
def on_starting(server):
    """Called just before the master process is initialized."""
    pass

def when_ready(server):
    """Called just after the server is started."""
    print(f"Gunicorn server ready. Listening on {bind}")

def pre_fork(server, worker):
    """Called just before a worker is forked."""
    pass

def post_fork(server, worker):
    """Called just after a worker has been forked."""
    print(f"Worker spawned (pid: {worker.pid})")

def pre_exec(server):
    """Called just before a new master process is forked."""
    pass

def pre_request(worker, req):
    """Called just before a worker processes the request."""
    worker.log.debug(f"{req.method} {req.path}")

def post_request(worker, req, environ, resp):
    """Called after a worker processes the request."""
    pass

def worker_abort(worker):
    """Called when a worker received the SIGABRT signal."""
    print(f"Worker aborted (pid: {worker.pid})")
