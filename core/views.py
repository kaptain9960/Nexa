from django.shortcuts import render
from django.http import FileResponse, JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
import os
import json

# Create your views here.
def home(request):
    """Render home page"""
    if request.method == 'POST':
        return handle_contact_form(request)
    return render(request, 'home.html')

@require_http_methods(["POST"])
def handle_contact_form(request):
    """Handle contact form submission"""
    try:
        # Get form data
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Validate required fields
        if not all([name, email, subject, message]):
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all required fields.'
            }, status=400)
        
        # Validate email format
        if '@' not in email or '.' not in email:
            return JsonResponse({
                'success': False,
                'message': 'Please enter a valid email address.'
            }, status=400)
        
        # Email to admin/owner
        admin_subject = f"New Contact Form Submission: {subject}"
        admin_message = f"""
        New message from your website contact form:
        
        Name: {name}
        Email: {email}
        Subject: {subject}
        
        Message:
        {message}
        
        ---
        Please reply to: {email}
        """
        
        # Email to sender (confirmation)
        sender_subject = "We've received your message"
        sender_message = f"""
        Hi {name},
        
        Thank you for contacting us! We've received your message and will get back to you as soon as possible.
        
        Here's a copy of your message:
        
        Subject: {subject}
        Message: {message}
        
        Best regards,
        Nexa Team
        """
        
        # Send emails
        send_mail(
            admin_subject,
            admin_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        
        # Send confirmation to sender
        send_mail(
            sender_subject,
            sender_message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Message sent successfully! We will contact you soon.'
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error sending message. Please try again later.'
        }, status=500)

def portfolio(request):
    """Render portfolio page"""
    return render(request, 'portfolio.html')

def portfolio_details(request):
    """Render portfolio details page"""
    return render(request, 'portfolio-details.html')

def services(request):
    """Render services page"""
    return render(request, 'services.html')

def service_details(request):
    """Render service details page"""
    return render(request, 'service-details.html')

def download_resume(request):
    """Download resume PDF file"""
    file_path = os.path.join(settings.BASE_DIR, 'assets', 'documents', 'resume.pdf')
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Resume.pdf"'
        return response
    return render(request, '404.html', status=404)

def about(request):
    return render(request, 'about.html')