## This markdown explains the configurations that have been implemented to protect the django application

## The following configuration steps have been made in Django:
- DEBUG has been disabled for production
- SECURE_BROWSER_SXX_FILTER has been enabled for browser-side XSS protection
- SECURE_CONTENT_TYPE_NOSNIFF has been enabled to prevent MIME sniffing
- X_FRAME_OPTIONS have been set to "DENY" to prevent clickjacking
- CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE have been enables to ensure cookies are only sent via HTTPS