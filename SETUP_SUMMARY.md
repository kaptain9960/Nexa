# Nexa Fashion House Project - Setup & Link Summary

## ✅ Changes Made

### 1. **Django Configuration (Nexa Fashion House/settings.py)**

- ✅ Fixed TEMPLATES directory to point to `core/templates`
- ✅ Configured STATIC_URL and STATIC_ROOT for proper static file serving
- ✅ Set STATICFILES_DIRS to include `assets/` folder
- ✅ Configured MEDIA_URL and MEDIA_ROOT for uploaded files

### 2. **URL Routing**

- ✅ Main project URLs (Nexa Fashion House/urls.py):
  - Added root path `/` pointing to `home` view
  - Included `core` app URLs at `/core/`
  - Configured static/media file serving in development mode

- ✅ App URLs (core/urls.py):
  - `/core/portfolio/` → portfolio view
  - `/core/services/` → services view
  - `/core/portfolio-details/` → portfolio details view
  - `/core/service-details/` → service details view

### 3. **Views (core/views.py)**

- ✅ Added 5 view functions:
  - `home()` - renders home.html
  - `portfolio()` - renders portfolio.html
  - `services()` - renders services.html
  - `portfolio_details()` - renders portfolio-details.html
  - `service_details()` - renders service-details.html

### 4. **Templates**

- ✅ **base.html** - Created master template with:
  - Header navigation with proper URL linking
  - Footer with company info and links
  - All CSS/JS includes with `{% static %}` tags
  - Block structure for content inheritance

- ✅ **home.html** - Updated to:
  - Extend base.html instead of being standalone
  - Use `{% static %}` tags for all image paths
  - Proper Django template syntax

- ✅ **portfolio.html** - Created new template with:
  - Portfolio grid layout
  - Links to portfolio details
  - Proper static file paths

- ✅ **services.html** - Created new template with:
  - Services grid with icons
  - Links to service details
  - Proper static file paths

- ✅ **portfolio-details.html** - Updated with:
  - Django template inheritance
  - Image slider with static paths
  - Project information section

- ✅ **service-details.html** - Updated with:
  - Django template inheritance
  - Service information and benefits
  - Call-to-action section

### 5. **Static Files**

- ✅ All image references updated from `assets/img/` to `{% static 'img/' %}`
- ✅ Vendor CSS/JS properly referenced in base.html
- ✅ Static file configuration in settings.py

### 6. **Documentation**

- ✅ requirements.txt - Python dependencies
- ✅ .gitignore - Git configuration
- ✅ README.md - Comprehensive project documentation

---

## 🚀 How to Run

```bash
# 1. Navigate to project directory
cd /home/sir-kaptain/Nexa Fashion House

# 2. Create virtual environment (if not already done)
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations (if needed)
python manage.py migrate

# 5. Start development server
python manage.py runserver

# 6. Visit in browser
# http://localhost:8000/
```

---

## 📍 URL Map

| URL Path                   | View Function       | Template               | Purpose                   |
| -------------------------- | ------------------- | ---------------------- | ------------------------- |
| `/`                        | `home`              | home.html              | Main landing page         |
| `/core/portfolio/`         | `portfolio`         | portfolio.html         | Portfolio listings        |
| `/core/services/`          | `services`          | services.html          | Services listings         |
| `/core/portfolio-details/` | `portfolio_details` | portfolio-details.html | Portfolio project details |
| `/core/service-details/`   | `service_details`   | service-details.html   | Service information       |
| `/admin/`                  | Django Admin        | N/A                    | Admin panel               |

---

## 🔗 Template Links

All templates are properly linked through:

1. **base.html** - Central template with navigation
2. **Navigation links** using `{% url 'view_name' %}` tags
3. **Static file paths** using `{% static 'path/to/file' %}` tags

### Navigation Menu (in base.html)

- Home link points to `home` view
- Service/Portfolio sections link to respective views
- All internal links use Django URL reverse lookup

---

## 📂 File Structure Overview

```
Nexa Fashion House/
├── manage.py                          ✅ Django manager
├── requirements.txt                   ✅ Python dependencies
├── .gitignore                         ✅ Git configuration
├── README.md                          ✅ Full documentation
│
├── Nexa Fashion House/                              ✅ Project settings
│   ├── settings.py                    ✅ Updated configuration
│   ├── urls.py                        ✅ Updated with all routes
│   ├── asgi.py
│   ├── wsgi.py
│   └── __init__.py
│
├── core/                              ✅ Main app
│   ├── views.py                       ✅ 5 view functions
│   ├── urls.py                        ✅ Updated routes
│   ├── models.py                      Ready for models
│   ├── migrations/
│   └── templates/                     ✅ All templates updated
│       ├── base.html                  ✅ Master template
│       ├── home.html                  ✅ Updated with static tags
│       ├── portfolio.html             ✅ New template
│       ├── services.html              ✅ New template
│       ├── portfolio-details.html     ✅ Updated
│       └── service-details.html       ✅ Updated
│
└── assets/                            ✅ All static files
    ├── css/
    ├── js/
    ├── img/
    ├── scss/
    └── vendor/
```

---

## ✨ Key Features Implemented

1. **Template Inheritance** - All pages extend base.html
2. **Static File Management** - Proper Django static file configuration
3. **URL Routing** - Clean, organized URL structure
4. **Navigation** - Working navigation menu with proper links
5. **Responsive Design** - Bootstrap 5 responsive layout
6. **Image Optimization** - WebP format images with lazy loading
7. **Vendor Libraries**:
   - Bootstrap 5 for layout
   - AOS for scroll animations
   - Swiper for carousels
   - GLightBox for image galleries
   - Bootstrap Icons for icons
   - PureCounter for animated counters

---

## ✅ Verification

All components have been checked:

- ✅ Django system check: `python manage.py check` → No issues
- ✅ URL patterns defined and working
- ✅ Templates properly configured for Django
- ✅ Static files properly linked
- ✅ Navigation menu working
- ✅ All views defined and callable

---

## 📝 Next Steps

1. **Database Setup** (if needed):

   ```bash
   python manage.py migrate
   ```

2. **Create Admin User** (if needed):

   ```bash
   python manage.py createsuperuser
   ```

3. **Start Server**:

   ```bash
   python manage.py runserver
   ```

4. **Customize Content**:
   - Edit templates to add your content
   - Update images in assets/img/
   - Modify colors in assets/css/main.css

---

## 🆘 Troubleshooting

| Issue                    | Solution                                      |
| ------------------------ | --------------------------------------------- |
| Static files not loading | Run `python manage.py collectstatic`          |
| Template not found       | Check template directory in settings.py       |
| Image paths broken       | Ensure `{% static %}` tags are used correctly |
| URL not found            | Check URL patterns in urls.py files           |
| Database errors          | Run `python manage.py migrate`                |

---

## 📄 Configuration Summary

- **Framework**: Django 4.2.11
- **Database**: SQLite (production-ready for PostgreSQL)
- **Static Files**: Served from `assets/` directory
- **Templates**: Located in `core/templates/`
- **Python Version**: 3.8+
- **Debug Mode**: Enabled (change in settings.py for production)

---

All files are now properly organized and linked. The project is ready to run! 🎉
