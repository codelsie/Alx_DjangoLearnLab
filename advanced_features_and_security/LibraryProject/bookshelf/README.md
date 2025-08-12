Permissions and Groups:
Groups:
  - Viewers: can_view
  - Editors: can_view, can_create, can_edit
  - Admins: can_view, can_create, can_edit, can_delete

These are enforced in views using the @permission_required decorator.
Users are assigned to groups in Django admin.


## Security checklist for LibraryProject

1. DEBUG
   - Ensure DEBUG = False in production (LibraryProject/LibraryProject/settings.py).

2. Cookies & HTTPS
   - CSRF_COOKIE_SECURE = True
   - SESSION_COOKIE_SECURE = True
   - Ensure site served over HTTPS for these to be effective.

3. Browser headers
   - SECURE_BROWSER_XSS_FILTER = True
   - SECURE_CONTENT_TYPE_NOSNIFF = True
   - X_FRAME_OPTIONS = 'DENY'

4. CSP
   - Either use django-csp (recommended) or the provided middleware to send Content-Security-Policy headers.

5. CSRF tokens
   - All forms must include {% csrf_token %} inside <form>.

6. Input handling
   - Validate user input with Django forms.
   - Use ORM methods (filter, exclude) to avoid raw SQL.

Testing:
- Try submitting a form without a CSRF token — should be blocked.
- Test input with script tags — should be escaped in templates (unless explicitly marked safe).
- Verify cookies are flagged Secure when using HTTPS.
- Inspect response headers for CSP and X-Frame options.
