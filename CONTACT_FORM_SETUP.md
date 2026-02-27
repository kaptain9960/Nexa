# 📧 Contact Form & Email Setup Guide

## Overview

Your contact form is now integrated with Django email functionality. When users submit the form, emails are sent to both you and the sender.

## What Was Done

### ✅ Files Modified/Created

1. **Backend Files**:
   - `core/views.py` - Added `handle_contact_form()` function
   - `Nexa Fashion House/settings.py` - Added email configuration
   - `core/templates/home.html` - Updated contact form HTML

2. **Frontend Files**:
   - `assets/js/contact-form.js` - Created form handler with AJAX

3. **Removed Files**:
   - `/core/templates/partial/` - Removed entire folder (unused base.html, nav.html, footer.html)

---

## How It Works

```
User Submits Form
    ↓
Browser validates form (Bootstrap validation)
    ↓
AJAX sends to server (no page refresh)
    ↓
Django view processes request
    ↓
Send email to: divineigwes1184@gmail.com
Send confirmation email to: user's email
    ↓
Return success/error response
    ↓
Display message to user
```

---

## Form Features

✅ **Bootstrap Validation**: Real-time field validation
✅ **AJAX Submission**: No page refresh required
✅ **Loading State**: Shows "Sending..." during submission
✅ **Success Message**: Confirms email was sent
✅ **Error Handling**: Shows friendly error messages
✅ **Auto-Reset**: Form clears after successful submission
✅ **Responsive Design**: Works on all devices

---

## Email Configuration

### Recipients

**Email 1: To Admin (You)**

- Recipient: `divineigwes1184@gmail.com`
- Subject: `New Contact Form Submission: [User's Subject]`
- Content: Full message details + sender's email

**Email 2: To Sender (Auto-reply)**

- Recipient: User's email address
- Subject: `We've received your message`
- Content: Confirmation message + copy of their message

### Email Settings in `Nexa Fashion House/settings.py`

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'divineigwes1184@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')
DEFAULT_FROM_EMAIL = 'divineigwes1184@gmail.com'
CONTACT_EMAIL = 'divineigwes1184@gmail.com'
```

---

## Setup Instructions

### Step 1: Gmail App Password

Since Gmail requires additional security, you need to generate an **App Password**:

1. Go to: https://myaccount.google.com/security
2. Enable **2-Step Verification** (if not already enabled)
3. Go to: https://myaccount.google.com/apppasswords
4. Select: Mail → Windows Computer (or your device)
5. Copy the 16-character password
6. Save it securely

### Step 2: Set Environment Variable

Run this command in your terminal:

**On Linux/macOS:**

```bash
export EMAIL_PASSWORD='your-16-char-app-password'
```

**On Windows (PowerShell):**

```powershell
$env:EMAIL_PASSWORD='your-16-char-app-password'
```

**Permanent (add to ~/.zshrc or ~/.bashrc):**

```bash
echo "export EMAIL_PASSWORD='your-16-char-app-password'" >> ~/.zshrc
source ~/.zshrc
```

### Step 3: Verify Configuration

Test the email setup:

```bash
python manage.py shell
```

Then in Python:

```python
from django.core.mail import send_mail
from django.conf import settings

send_mail(
    'Test Subject',
    'Test Message',
    settings.DEFAULT_FROM_EMAIL,
    ['divineigwes1184@gmail.com'],
    fail_silently=False,
)
```

If successful, you'll see output without errors.

---

## Form HTML Structure

```html
<form action="{% url 'home' %}" method="post" id="contactForm">
  {% csrf_token %}

  <!-- Name Field -->
  <input name="name" type="text" required />

  <!-- Email Field -->
  <input name="email" type="email" required />

  <!-- Subject Field -->
  <input name="subject" type="text" required />

  <!-- Message Field -->
  <textarea name="message" required></textarea>

  <!-- Submit Button -->
  <button type="submit">Send Message</button>
</form>
```

---

## Form Handler Code

**Location**: `core/views.py`

```python
def handle_contact_form(request):
    # Get form data
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    subject = request.POST.get('subject', '').strip()
    message = request.POST.get('message', '').strip()

    # Validate fields
    if not all([name, email, subject, message]):
        return JsonResponse({'success': False, 'message': 'Fill all fields'})

    # Send emails
    send_mail(admin_subject, admin_message, settings.DEFAULT_FROM_EMAIL,
              [settings.CONTACT_EMAIL], fail_silently=False)
    send_mail(sender_subject, sender_message, settings.DEFAULT_FROM_EMAIL,
              [email], fail_silently=False)

    return JsonResponse({'success': True})
```

---

## JavaScript Handler

**Location**: `assets/js/contact-form.js`

Features:

- Bootstrap form validation
- AJAX submission (no reload)
- Loading indicator
- Error messages
- Success confirmation
- Auto-scroll to messages
- Form reset on success

---

## Customizing Emails

### To Change Email Recipient

Edit `Nexa Fashion House/settings.py`:

```python
CONTACT_EMAIL = 'newemail@example.com'
```

### To Change Email Content

Edit `core/views.py` in the `handle_contact_form()` function:

```python
# Change these strings:
admin_message = "Your custom message here..."
sender_message = "Your custom confirmation here..."
```

### To Change Email From Address

Edit `Nexa Fashion House/settings.py`:

```python
EMAIL_HOST_USER = 'youremail@gmail.com'
DEFAULT_FROM_EMAIL = 'youremail@gmail.com'
```

---

## Testing the Form

1. **Start Django Server**:

   ```bash
   python manage.py runserver
   ```

2. **Navigate to Home Page**: http://localhost:8000

3. **Scroll to Contact Section**: Fill the form

4. **Submit**:
   - Should see "Sending..." message
   - Then success/error message
   - Check your email inbox

5. **Check Emails**:
   - Check spam folder if not in inbox
   - Both you and sender should receive emails

---

## Troubleshooting

### Issue: "SMTP Authentication Error"

**Solution**:

- Verify EMAIL_PASSWORD environment variable is set
- Check Gmail App Password is correct (16 characters)
- Ensure 2-Step Verification is enabled on Gmail account

### Issue: "Connection refused"

**Solution**:

- Check internet connection
- Verify EMAIL_HOST = 'smtp.gmail.com' in settings
- Verify EMAIL_PORT = 587

### Issue: Emails not received

**Solution**:

- Check spam/junk folder
- Verify recipient email address is correct
- Check Django error logs for exceptions

### Issue: Form won't submit

**Solution**:

- Open browser console (F12) to check for JavaScript errors
- Verify csrf_token is in form
- Check that contactForm.js is loaded

### Issue: "Environment variable not set"

**Solution**:

```bash
# Set temporarily for this session
export EMAIL_PASSWORD='your-app-password'
python manage.py runserver

# OR set permanently in ~/.zshrc
echo "export EMAIL_PASSWORD='your-app-password'" >> ~/.zshrc
source ~/.zshrc
```

---

## Security Considerations

✅ **CSRF Protection**: Form includes `{% csrf_token %}`
✅ **Validation**: Server-side validation of all fields
✅ **Email Validation**: Checks for valid email format
✅ **Environment Variables**: App password stored in environment, not in code
✅ **TLS Encryption**: Uses EMAIL_USE_TLS = True for secure connection

---

## File Cleanup

Removed unused files:

```
✅ /core/templates/partial/templates/base.html
✅ /core/templates/partial/templates/nav.html
✅ /core/templates/partial/templates/footer.html
✅ Entire /core/templates/partial/ directory
```

All navigation and footer are now in `/core/templates/base.html` only.

---

## Alternative Email Services

If you want to use a different email service instead of Gmail:

### SendGrid

```python
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
```

### AWS SES

```python
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_SES_REGION_NAME = 'us-east-1'
```

### Mailgun

```python
EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
ANYMAIL = {'MAILGUN_API_KEY': os.environ.get('MAILGUN_API_KEY')}
```

---

## Production Considerations

Before deploying to production:

1. **Set Environment Variable** on your server
2. **Update ALLOWED_HOSTS** in settings.py
3. **Set DEBUG = False** in settings.py
4. **Configure CSRF_TRUSTED_ORIGINS** if needed
5. **Use HTTPS** (form works best over HTTPS)
6. **Test on production server** before going live

---

## Next Steps (Optional)

Consider these enhancements:

- ✨ Add spam protection (reCAPTCHA)
- ✨ Save submissions to database
- ✨ Add file attachment support
- ✨ Create admin interface for submissions
- ✨ Add email scheduling/queue system
- ✨ Add reply-to functionality

---

**Status**: ✅ Ready to Use
**Form Location**: Home page, Contact section
**Email Recipient**: divineigwes1184@gmail.com
**Last Updated**: February 27, 2026
