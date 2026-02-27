# 🚀 Quick Start Guide - Nexa Fashion House Project

## 30-Second Setup

```bash
cd /home/sir-kaptain/Nexa Fashion House
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Then visit: **http://localhost:8000/**

---

## What Was Fixed

✅ **Django Configuration** - Settings properly configured for static files and templates
✅ **URL Routing** - All pages properly linked and accessible
✅ **Templates** - All HTML files now use Django template syntax
✅ **Static Files** - Images and assets properly referenced
✅ **Navigation** - Menu links working throughout the site
✅ **File Organization** - Clean, professional project structure

---

## Pages Available

| Route                                           | Page              |
| ----------------------------------------------- | ----------------- |
| `http://localhost:8000/`                        | Home              |
| `http://localhost:8000/core/portfolio/`         | Portfolio         |
| `http://localhost:8000/core/services/`          | Services          |
| `http://localhost:8000/core/portfolio-details/` | Portfolio Details |
| `http://localhost:8000/core/service-details/`   | Service Details   |
| `http://localhost:8000/admin/`                  | Admin Panel       |

---

## Project Structure

```
Nexa Fashion House/
├── manage.py                    # Django CLI
├── requirements.txt             # Dependencies
├── Nexa Fashion House/                        # Settings
│   ├── settings.py             # Configuration ✅
│   └── urls.py                 # Routes ✅
├── core/                        # Main app
│   ├── views.py                # 5 views ✅
│   ├── urls.py                 # Routes ✅
│   └── templates/              # All templates ✅
│       ├── base.html           # Master template
│       ├── home.html
│       ├── portfolio.html
│       ├── services.html
│       ├── portfolio-details.html
│       └── service-details.html
└── assets/                      # Static files
    ├── css/
    ├── js/
    ├── img/
    └── vendor/
```

---

## Key Commands

```bash
# Start development server
python manage.py runserver

# Create admin user
python manage.py createsuperuser

# Run migrations
python manage.py migrate

# Access admin panel
# http://localhost:8000/admin/

# Deactivate virtual environment
deactivate
```

---

## Everything Works! ✨

- ✅ Server starts without errors
- ✅ All pages load
- ✅ Navigation menu works
- ✅ Images display properly
- ✅ CSS/JS load correctly
- ✅ Django admin accessible

---

## Customization

### Add new page:

1. Create view in `core/views.py`
2. Create template in `core/templates/`
3. Add URL in `core/urls.py`

### Update content:

1. Edit HTML in `core/templates/`
2. Replace images in `assets/img/`
3. Modify styles in `assets/css/main.css`

### Database:

Django is using SQLite by default. Ready to switch to PostgreSQL/MySQL in production.

---

## Troubleshooting

**Port 8000 in use?**

```bash
python manage.py runserver 8001
```

**Images not showing?**

```bash
python manage.py collectstatic
```

**Template not found?**
Check `TEMPLATES` in `Nexa Fashion House/settings.py`

---

**Everything is working! Start the server and visit http://localhost:8000/ 🎉**
