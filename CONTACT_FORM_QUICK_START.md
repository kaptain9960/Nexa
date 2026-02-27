# 🚀 Quick Start - Contact Form & Email

## 3-Step Setup

### Step 1: Get Gmail App Password (2 minutes)

1. Visit: https://myaccount.google.com/apppasswords
2. Select: Mail → Windows Computer
3. Copy the 16-character password
4. Keep it safe!

### Step 2: Set Environment Variable (1 minute)

```bash
export EMAIL_PASSWORD='your-16-char-app-password'
```

To make it permanent:

```bash
echo "export EMAIL_PASSWORD='your-16-char-app-password'" >> ~/.zshrc
source ~/.zshrc
```

### Step 3: Test (2 minutes)

```bash
python manage.py runserver
```

Visit: http://localhost:8000

- Scroll to Contact section
- Fill form
- Click Send
- Check your email!

---

## What Works Now

✅ Contact form with Bootstrap styling
✅ Real-time form validation
✅ Email to you at divineigwes1184@gmail.com
✅ Auto-reply to sender
✅ AJAX submission (no page refresh)
✅ Success/error messages
✅ Mobile responsive

---

## Form Fields

- **Name** (required)
- **Email** (required)
- **Subject** (required)
- **Message** (required)

---

## Email Recipients

**Email 1**: To you (admin)

- Recipient: divineigwes1184@gmail.com
- Subject: "New Contact Form Submission: [subject]"

**Email 2**: To sender

- Recipient: User's email
- Subject: "We've received your message"

---

## Troubleshooting

| Problem            | Solution                                |
| ------------------ | --------------------------------------- |
| Email not received | Check spam folder                       |
| SMTP error         | Regenerate Gmail App Password           |
| Form won't submit  | Check browser console (F12)             |
| Can't set env var  | Use: `export EMAIL_PASSWORD='password'` |

---

## File Locations

- **Form**: `/core/templates/home.html`
- **Handler**: `/core/views.py`
- **Settings**: `/Nexa Fashion House/settings.py`
- **Script**: `/assets/js/contact-form.js`

---

## Changed Files

✅ `core/views.py` - Email handler
✅ `Nexa Fashion House/settings.py` - Email config
✅ `core/templates/home.html` - Form updated
✅ `core/templates/base.html` - Script added
✅ `assets/js/contact-form.js` - New file
❌ Removed: `/core/templates/partial/`

---

## Full Guides

- `CONTACT_FORM_SETUP.md` - Complete guide
- `CONTACT_FORM_SUMMARY.md` - Summary
- `CONTACT_FORM_COMPLETE.md` - Full report

---

**Ready to go!** 🎉
