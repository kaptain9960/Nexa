# Nexa Fashion House Project Structure

## Project Overview

This is a Django-based business solutions website built with Bootstrap 5 and various vendor libraries for animations, carousels, and lightbox functionality.

## Directory Structure

```
Nexa Fashion House/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore file
├── Nexa Fashion House/                    # Main Django project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # Main URL routing
│   ├── asgi.py              # ASGI configuration
│   ├── wsgi.py              # WSGI configuration
│   └── __init__.py
├── core/                    # Main Django app
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # App URL routing
│   ├── forms/               # Form files
│   ├── migrations/          # Database migrations
│   └── templates/           # HTML templates
│       ├── base.html        # Base template (inherited by all pages)
│       ├── home.html        # Home page
│       ├── portfolio.html   # Portfolio listing
│       ├── services.html    # Services listing
│       ├── portfolio-details.html  # Portfolio details
│       └── service-details.html    # Service details
└── assets/                  # Static files
    ├── css/
    │   └── main.css         # Main stylesheet
    ├── js/
    │   └── main.js          # Main JavaScript
    ├── img/                 # Images
    │   ├── person/          # Team member photos
    │   ├── portfolio/       # Portfolio images
    │   ├── services/        # Service images
    │   └── about/           # About section images
    ├── scss/                # SCSS source files
    └── vendor/              # Third-party libraries
        ├── bootstrap/       # Bootstrap CSS/JS
        ├── bootstrap-icons/ # Bootstrap icons
        ├── aos/             # Animate on scroll
        ├── swiper/          # Carousel library
        ├── glightbox/       # Lightbox gallery
        ├── isotope-layout/  # Portfolio filtering
        └── purecounter/     # Number counter

```

## Setup Instructions

### 1. Clone or Download the Project

```bash
cd /home/sir-kaptain/Nexa Fashion House
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000/` in your browser.

## URL Routes

| Route                      | View              | Template               |
| -------------------------- | ----------------- | ---------------------- |
| `/`                        | home              | home.html              |
| `/core/portfolio/`         | portfolio         | portfolio.html         |
| `/core/services/`          | services          | services.html          |
| `/core/portfolio-details/` | portfolio_details | portfolio-details.html |
| `/core/service-details/`   | service_details   | service-details.html   |
| `/admin/`                  | admin             | N/A                    |

## Key Features

- **Responsive Design**: Built with Bootstrap 5 for mobile-first responsive design
- **Animations**: AOS (Animate on Scroll) for scroll-triggered animations
- **Carousels**: Swiper for responsive touch sliders
- **Galleries**: GLightBox for image lightbox functionality
- **Icons**: Bootstrap Icons for scalable vector icons
- **Performance**: Lazy loading, optimized images in WebP format

## Static Files

Django is configured to serve static files from the `assets/` directory:

- **CSS**: `assets/css/` and vendor CSS files
- **JavaScript**: `assets/js/` and vendor JS files
- **Images**: `assets/img/` with organized subdirectories

## Template Inheritance

All page templates extend `base.html` which includes:

- Header navigation
- Footer
- All CSS/JavaScript includes
- Meta tags and favicons

This ensures consistent styling and functionality across all pages.

## Django App Structure

### Views (core/views.py)

- `home()` - Renders home page
- `portfolio()` - Renders portfolio listing
- `services()` - Renders services listing
- `portfolio_details()` - Renders portfolio detail page
- `service_details()` - Renders service detail page

### URLs (core/urls.py)

Routes for portfolio, services, and detail pages.

### Settings (Nexa Fashion House/settings.py)

- Configured static files directory
- Template directory set to `core/templates`
- Debug mode enabled for development

## Customization

### Adding New Pages

1. Create a new view in `core/views.py`
2. Create a new template file extending `base.html` in `core/templates/`
3. Add a URL route in `core/urls.py`

### Styling

- Edit `assets/css/main.css` for custom styles
- SCSS source files available in `assets/scss/` if you want to recompile

### Images

- Replace placeholder images in `assets/img/` with your own
- Maintain the same directory structure for proper linking

## Troubleshooting

### Static files not loading

Run: `python manage.py collectstatic`

### Database errors

Run: `python manage.py migrate`

### Port already in use

Run: `python manage.py runserver 8001`

## License

Template by BootstrapMade.com - Adapted for Django
