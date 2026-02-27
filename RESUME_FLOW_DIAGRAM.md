# Resume Download Flow Diagram

## User Interaction Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    USER VIEWS WEBSITE                       │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│            Sees Navigation Menu (Header)                    │
│   [Home] [About] [Services] [Portfolio] [Contact] [Resume]  │
│            or Footer Resources Section                      │
│               [📥 Download Resume]                          │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│            USER CLICKS RESUME LINK                          │
│        {% url 'download-resume' %}                          │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│        DJANGO ROUTES TO /core/download-resume/              │
│               (URL Dispatcher)                              │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│   DOWNLOAD_RESUME() VIEW EXECUTES                           │
│                                                             │
│   1. Check: Does resume.pdf exist?                          │
│      ├─ YES → Continue to step 2                           │
│      └─ NO → Return 404 Error                              │
│                                                             │
│   2. Open file: /assets/documents/resume.pdf               │
│      ├─ Mode: Binary ('rb')                                │
│      └─ Type: PDF                                          │
│                                                             │
│   3. Set Response Headers:                                  │
│      ├─ Content-Type: application/pdf                      │
│      └─ Content-Disposition: attachment; filename="Resume.pdf" │
│                                                             │
│   4. Return FileResponse with file content                 │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│         BROWSER RECEIVES PDF FILE                           │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│      BROWSER AUTOMATICALLY DOWNLOADS FILE                   │
│           (Saved as: Resume.pdf)                            │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│            FILE ON USER'S COMPUTER                          │
│        ~/Downloads/Resume.pdf                               │
└─────────────────────────────────────────────────────────────┘
```

## File System Architecture

```
/home/sir-kaptain/Nexa Fashion House/
│
├── 📄 Nexa Fashion House/
│   ├── settings.py          ← Django configuration
│   ├── urls.py              ← Main URL router
│   └── wsgi.py
│
├── 📄 core/
│   ├── views.py             ← Contains download_resume()
│   ├── urls.py              ← Contains download-resume route
│   └── templates/
│       ├── base.html        ← Contains resume download links
│       ├── home.html
│       └── ...
│
├── 📄 assets/
│   │
│   ├── 📁 documents/        ← RESUME STORAGE
│   │   └── resume.pdf       ← ⭐ Your Resume File Here
│   │
│   ├── 📁 css/
│   │   └── main.css
│   │
│   ├── 📁 img/
│   │   └── ...
│   │
│   ├── 📁 js/
│   │   └── main.js
│   │
│   └── 📁 vendor/
│       └── (Bootstrap, jQuery, etc.)
│
└── manage.py               ← Django management
```

## Code Location Map

```
TEMPLATES (Frontend):
├── Header Navigation
│   └── Location: core/templates/base.html (Line ~70)
│       Link: <a href="{% url 'download-resume' %}">Resume</a>
│
└── Footer Resources
    └── Location: core/templates/base.html (Line ~125)
        Link: <a href="{% url 'download-resume' %}">Download Resume</a>

VIEWS (Backend Logic):
├── Function: download_resume()
│   └── Location: core/views.py (Line ~28-34)
│       Task: Serve PDF file with proper headers
│
└── Imports:
    ├── FileResponse: Send file to browser
    ├── settings: Access BASE_DIR
    └── os: Check file existence

URLs (Routing):
├── Route: download-resume/
│   └── Location: core/urls.py (Line ~9)
│       Maps to: views.download_resume
│       Name: download-resume (for template reverse)
│
└── Main URL Config: Nexa Fashion House/urls.py
    Includes: core/urls.py
```

## HTTP Request/Response Flow

```
CLIENT REQUEST:
┌────────────────────────────────────────────────────┐
│ GET /core/download-resume/ HTTP/1.1               │
│ Host: localhost:8000                               │
│ User-Agent: Mozilla/5.0...                         │
│ Accept: text/html,application/xhtml+xml...        │
└────────────────────────────────────────────────────┘

SERVER PROCESSING:
┌────────────────────────────────────────────────────┐
│ 1. Match URL pattern: 'download-resume/'          │
│ 2. Call: views.download_resume(request)           │
│ 3. Build path: settings.BASE_DIR/assets/documents │
│ 4. Check file exists: resume.pdf ✓               │
│ 5. Open in binary mode: rb                        │
│ 6. Create FileResponse with PDF content           │
│ 7. Set headers: Content-Type, Content-Disposition│
└────────────────────────────────────────────────────┘

SERVER RESPONSE:
┌────────────────────────────────────────────────────┐
│ HTTP/1.1 200 OK                                    │
│ Content-Type: application/pdf                      │
│ Content-Disposition: attachment;                  │
│   filename="Resume.pdf"                            │
│ Content-Length: 257773                             │
│                                                    │
│ [Binary PDF Content - 257 KB]                      │
└────────────────────────────────────────────────────┘

BROWSER ACTION:
┌────────────────────────────────────────────────────┐
│ Detects Content-Disposition: attachment           │
│ Triggers Download Dialog                          │
│ Saves as: Resume.pdf                              │
│ Location: ~/Downloads/ (or user's choice)         │
└────────────────────────────────────────────────────┘
```

## Security & Data Flow

```
                        ┌─────────────────┐
                        │   User Request  │
                        └────────┬────────┘
                                 │
                        ┌────────▼────────┐
                        │  Django Router  │
                        └────────┬────────┘
                                 │
                        ┌────────▼────────────────────┐
                        │ check: File Exists? (Security)
                        └────────┬────────────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
            ┌───────▼──────┐        ┌────────▼─────┐
            │  NOT FOUND   │        │   FOUND ✓    │
            │ Return 404   │        └────────┬─────┘
            └──────────────┘                 │
                                  ┌─────────▼──────────┐
                                  │ Open File (Binary) │
                                  └─────────┬──────────┘
                                           │
                                  ┌────────▼────────────┐
                                  │ Set Headers:        │
                                  │ - Type: PDF         │
                                  │ - Mode: Attachment  │
                                  │ - Name: Resume.pdf  │
                                  └────────┬────────────┘
                                           │
                                  ┌────────▼───────────┐
                                  │ Send to Browser    │
                                  └────────┬───────────┘
                                           │
                                  ┌────────▼──────────┐
                                  │ Browser Downloads │
                                  │ Resume.pdf        │
                                  └───────────────────┘
```

---

**Key Points**:

- 🔒 Security: File path validated, existence checked
- ⚡ Performance: Direct binary file serving
- 🎯 User Experience: One-click download from any page
- 📱 Mobile: Works on all devices and browsers
- 🔄 Maintainable: Only need to replace file to update
