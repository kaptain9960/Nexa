# Nexa Fashion House Project - Architecture & Data Flow

## Project Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Nexa Fashion House PROJECT                             │
│               (Django Web Application)                      │
└─────────────────────────────────────────────────────────────┘

                          ┌──────────────┐
                          │   Browser    │
                          │   Request    │
                          └──────┬───────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │  Main URL Router       │
                    │  (Nexa Fashion House/urls.py)        │
                    └────────┬───────────────┘
                             │
                ┌────────────┼────────────────┐
                │            │                │
                ▼            ▼                ▼
           ┌────────┐  ┌──────────┐  ┌────────────────┐
           │ Admin  │  │Home View │  │Core App URLs   │
           │/admin/ │  │ (root)   │  │/core/...       │
           └────────┘  └────┬─────┘  └─────┬──────────┘
                             │              │
                    ┌────────┘              │
                    │         ┌────────────┬┴────────────┐
                    │         │            │            │
                    ▼         ▼            ▼            ▼
              ┌─────────┐ ┌────────┐ ┌────────┐ ┌──────────┐
              │home()   │ │port()  │ │serv()  │ │details() │
              │view     │ │view    │ │view    │ │views     │
              └────┬────┘ └────┬───┘ └────┬───┘ └──────┬───┘
                   │          │         │           │
                   │          │         │           │
        ┌──────────┴──┐     ┌──┴────┐  ┌┴──────┐  ┌──┴────────┐
        │             │     │       │  │       │  │           │
        ▼             ▼     ▼       ▼  ▼       ▼  ▼           ▼
    ┌────────┐   ┌─────────────────────────────────────────┐
    │Template │   │      Template Rendering                │
    │Render   │   │  (Django Template Engine)              │
    │Request  │   │                                        │
    └────┬───┘   └──────────────┬──────────────────────────┘
         │                      │
         │              ┌───────┴───────┐
         │              │               │
         ▼              ▼               ▼
    ┌─────────────────────────────────────────┐
    │    Templates (HTML + Django Tags)       │
    ├─────────────────────────────────────────┤
    │ ┌─────────────────────────────────────┐ │
    │ │      base.html (Master Template)    │ │
    │ │  - Header & Navigation              │ │
    │ │  - CSS/JS Includes                  │ │
    │ │  - Footer                           │ │
    │ │  - {% block content %} for pages    │ │
    │ └─────────────────────────────────────┘ │
    │ ┌─────────────────────────────────────┐ │
    │ │ Child Templates (extends base.html) │ │
    │ │ - home.html                         │ │
    │ │ - portfolio.html                    │ │
    │ │ - services.html                     │ │
    │ │ - portfolio-details.html            │ │
    │ │ - service-details.html              │ │
    │ └─────────────────────────────────────┘ │
    └──────────────────┬──────────────────────┘
                       │
         ┌─────────────┴─────────────┐
         │                           │
         ▼                           ▼
    ┌──────────────────┐    ┌───────────────────┐
    │ Static Files     │    │ Dynamic Content   │
    │ ({% static %})   │    │ (Context Data)    │
    ├──────────────────┤    └───────────────────┘
    │ ├── css/         │
    │ ├── js/          │
    │ ├── img/         │
    │ └── vendor/      │
    └──────────────────┘
         │
         └─────────────────┐
                           │
                           ▼
                    ┌──────────────┐
                    │ Rendered     │
                    │ HTML Page    │
                    │ (Response)   │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Browser   │
                    │  Displays    │
                    │    Page      │
                    └──────────────┘
```

---

## URL Routing Flow

```
Browser Request
    │
    ├─> GET /                          → home() view → home.html
    │
    ├─> GET /core/portfolio/           → portfolio() view → portfolio.html
    │
    ├─> GET /core/services/            → services() view → services.html
    │
    ├─> GET /core/portfolio-details/   → portfolio_details() view → portfolio-details.html
    │
    ├─> GET /core/service-details/     → service_details() view → service-details.html
    │
    └─> GET /admin/                    → Django Admin Panel
```

---

## Template Inheritance Structure

```
                      base.html
                    (Master Template)
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
    home.html        portfolio.html    services.html
    (Extends)         (Extends)         (Extends)
        │                 │                 │
        └─────────┬───────┴─────────────────┤
                  │                         │
                  ▼                         ▼
        portfolio-details.html    service-details.html
            (Extends)                  (Extends)


Each template:
├─ Inherits header/footer from base.html
├─ Includes {% load static %} for images
├─ Uses {% url 'view_name' %} for links
└─ Has unique {% block content %} section
```

---

## Static Files Hierarchy

```
assets/
├── css/
│   └── main.css          ← Custom styles
├── js/
│   └── main.js           ← Custom JavaScript
├── img/
│   ├── favicon.png
│   ├── logo.webp
│   ├── person/           ← Team photos
│   ├── portfolio/        ← Portfolio images
│   ├── services/         ← Service images
│   ├── about/            ← About section images
│   └── bg/               ← Background images
├── scss/                 ← SCSS source files
└── vendor/               ← Third-party libraries
    ├── bootstrap/        ← Bootstrap Framework
    ├── aos/              ← Scroll animations
    ├── swiper/           ← Carousels
    ├── glightbox/        ← Image lightbox
    ├── isotope-layout/   ← Portfolio filtering
    └── purecounter/      ← Number counters

All referenced via: {% static 'path/to/file' %}
```

---

## Django Configuration Flow

```
┌────────────────────────────────────┐
│    Django Settings                 │
│    (Nexa Fashion House/settings.py)              │
└────────────┬───────────────────────┘
             │
    ┌────────┴─────────────┐
    │                      │
    ▼                      ▼
┌─────────────────┐  ┌──────────────────┐
│ INSTALLED_APPS  │  │ TEMPLATES        │
├─────────────────┤  ├──────────────────┤
│ - django apps   │  │ DIRS: [           │
│ - core app      │  │   core/templates] │
└─────────────────┘  │ APP_DIRS: True    │
                     └──────────────────┘

    ┌────────────────────────────────┐
    ▼                                ▼
┌─────────────────────┐  ┌──────────────────────┐
│ Static Files Config │  │ Database Config      │
├─────────────────────┤  ├──────────────────────┤
│ STATIC_URL = /      │  │ ENGINE: sqlite3      │
│ STATIC_ROOT =       │  │ NAME: db.sqlite3     │
│   staticfiles/      │  │                      │
│ STATICFILES_DIRS =  │  │ (Ready for:          │
│   [assets/]         │  │  PostgreSQL, MySQL)  │
└─────────────────────┘  └──────────────────────┘
```

---

## Request-Response Cycle Example

### Example: User visits home page

```
1. Browser sends: GET /
                  ↓
2. URL Router (Nexa Fashion House/urls.py) matches to path('', views.home)
                  ↓
3. View function home(request) called
   - home(request) { return render(request, 'home.html') }
                  ↓
4. Django loads template: core/templates/home.html
                  ↓
5. Template extends base.html
   - Inherits header with navigation
   - Inherits footer
   - Includes all CSS/JS via {% static %} tags
   - Loads images via {% static %} tags
                  ↓
6. Django Template Engine processes:
   - {% load static %} loads static file tags
   - {% extends 'base.html' %} inherits parent
   - {% block content %} inserts unique content
   - {% url 'view_name' %} generates URLs
   - {% static 'path' %} converts to /static/path
                  ↓
7. Template renders to HTML
                  ↓
8. Browser receives complete HTML page with:
   - Proper CSS links
   - Proper JS links
   - Proper image paths
   - Working navigation links
                  ↓
9. Browser displays formatted page
```

---

## File Linking Summary

### How Links Work:

```
1. Navigation Links (in base.html)
   <a href="{% url 'portfolio' %}">Portfolio</a>
   → Calls django.urls.reverse('portfolio')
   → Returns: /core/portfolio/
   → Links to: core/urls.py → portfolio view

2. Static Files (in templates)
   <link href="{% static 'css/main.css' %}">
   → Calls django.templatetags.static.static()
   → Returns: /static/css/main.css
   → Serves from: assets/css/main.css

3. Images (in templates)
   <img src="{% static 'img/person.webp' %}">
   → Returns: /static/img/person.webp
   → Served from: assets/img/person.webp
```

---

## Complete Data Flow

```
┌─────────────────────────────────────────────────────────────┐
│                 USER BROWSER                                │
│         (Makes HTTP Request to Server)                      │
└──────────────────┬──────────────────────────────────────────┘
                   │ HTTP GET /portfolio/
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│              DJANGO WEB SERVER                              │
│           (Processes Request)                               │
├──────────────────────────────────────────────────────────────┤
│ 1. URL ROUTING                                              │
│    /portfolio/ → matches core/urls.py                       │
│    → portfolio() view function                              │
├──────────────────────────────────────────────────────────────┤
│ 2. VIEW PROCESSING                                          │
│    portfolio(request) {                                     │
│      return render(request, 'portfolio.html')               │
│    }                                                        │
├──────────────────────────────────────────────────────────────┤
│ 3. TEMPLATE LOADING                                         │
│    Load: core/templates/portfolio.html                      │
│    - Extends base.html                                      │
│    - Inherits navigation, footer, CSS/JS                    │
│    - Loads portfolio images from assets/img/                │
├──────────────────────────────────────────────────────────────┤
│ 4. TEMPLATE RENDERING                                       │
│    Process Django template tags:                            │
│    - {% load static %} enable static files                  │
│    - {% extends %} include base.html                        │
│    - {% block content %} insert page content                │
│    - {% url %} generate navigation URLs                     │
│    - {% static %} generate asset paths                      │
├──────────────────────────────────────────────────────────────┤
│ 5. RESPONSE GENERATION                                      │
│    Complete HTML page with:                                │
│    - Proper CSS paths (/static/css/)                        │
│    - Proper JS paths (/static/js/)                          │
│    - Proper image paths (/static/img/)                      │
│    - Working navigation links                               │
│    - Full content structure                                 │
└──────────────────┬──────────────────────────────────────────┘
                   │ HTTP Response (HTML)
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│                 USER BROWSER                                │
│          (Receives and Renders Page)                        │
│                                                             │
│   ┌─────────────────────────────────────────────┐          │
│   │     Portfolio Page Displayed                │          │
│   │  - With proper styling (CSS loaded)         │          │
│   │  - With proper functionality (JS loaded)    │          │
│   │  - With proper images (from /static/img/)   │          │
│   │  - With working navigation links            │          │
│   └─────────────────────────────────────────────┘          │
│                                                             │
│   User clicks "Home" link                                  │
│   → browser sends GET / request                            │
│   → cycle repeats...                                       │
└─────────────────────────────────────────────────────────────┘
```

---

## Summary

✅ **All files properly organized**
✅ **All routes properly configured**
✅ **All templates properly linked**
✅ **All static files properly referenced**
✅ **Navigation fully functional**
✅ **Project ready to run**

The Nexa Fashion House project is now a fully functional Django web application with:

- Proper URL routing
- Template inheritance
- Static file management
- Clean project structure
- Professional organization
