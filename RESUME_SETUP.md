# Resume Download Setup Guide

## Overview

Your resume has been integrated into your portfolio website with both static and dynamic download options.

## File Location

- **Resume File**: `/home/sir-kaptain/Nexa Fashion House/assets/documents/resume.pdf`
- **Original Location**: Moved from `/home/sir-kaptain/Nexa Fashion House/assets/img/portfolio/CV Resume.pdf`

## How It Works

### 1. **Header Navigation Link**

- Located in the main navigation bar at the top of every page
- Shows as: "📥 Resume"
- Uses Bootstrap Icons for visual appeal
- Clicking triggers the download via Django view

### 2. **Footer Resources Section**

- Located in the footer "Resources" column
- Shows as: "📥 Download Resume"
- Same download functionality as header link

## Implementation Details

### Backend

**File**: `/home/sir-kaptain/Nexa Fashion House/core/views.py`

```python
def download_resume(request):
    """Download resume PDF file"""
    file_path = os.path.join(settings.BASE_DIR, 'assets', 'documents', 'resume.pdf')
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Resume.pdf"'
        return response
```

### URL Routing

**File**: `/home/sir-kaptain/Nexa Fashion House/core/urls.py`

```python
path('download-resume/', views.download_resume, name='download-resume'),
```

### Frontend

**File**: `/home/sir-kaptain/Nexa Fashion House/core/templates/base.html`

**Header Link**:

```html
<a
  href="{% url 'download-resume' %}"
  class="nav-link-resume"
  download="Resume.pdf"
>
  <i class="bi bi-download"></i> Resume
</a>
```

**Footer Link**:

```html
<a href="{% url 'download-resume' %}" download="Resume.pdf">
  <i class="bi bi-download"></i> Download Resume
</a>
```

## Features

✅ **Direct Download**: Users can download the resume directly to their device  
✅ **Automatic Naming**: File downloads as "Resume.pdf"  
✅ **Mobile Friendly**: Works on all devices (desktop, tablet, mobile)  
✅ **Icon Integration**: Uses Bootstrap Icons for consistent design  
✅ **Error Handling**: Returns 404 if file not found  
✅ **URL Reversal**: Uses Django's `{% url %}` tag for maintainability

## Usage

1. **For End Users**: Simply click "Resume" in the header or footer to download
2. **To Update Resume**: Replace the file at `/home/sir-kaptain/Nexa Fashion House/assets/documents/resume.pdf`
3. **To Change Filename**: Update the `download_resume()` function in `views.py`

## Security Considerations

- File is served through a Django view for better control
- Path is constructed securely using `settings.BASE_DIR`
- File existence is checked before serving
- Content type is explicitly set to PDF

## Troubleshooting

**Issue**: Resume link doesn't work

- **Solution**: Ensure `resume.pdf` exists in `/home/sir-kaptain/Nexa Fashion House/assets/documents/`

**Issue**: Download triggers but file is corrupted

- **Solution**: Verify the PDF file is not corrupted by opening it locally

**Issue**: Wrong filename on download

- **Solution**: The filename comes from the `response['Content-Disposition']` header in `views.py`

## Future Enhancements

- Add resume preview before download
- Support multiple resume versions (e.g., "Resume_Developer.pdf", "Resume_Designer.pdf")
- Add download analytics tracking
- Version history of resumes
