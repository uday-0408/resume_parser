import pdfplumber
from django.http import JsonResponse
from .models import Resume


def get_resume(request):
    resume_id = request.GET.get("resume_id")
    try:
        resume = Resume.objects.get(id=resume_id)
        file_path = resume.file.path
        text = ""
        if file_path.lower().endswith(".pdf"):
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
        else:
            # fallback for non-pdf files
            text = open(file_path, encoding="utf-8").read()
    except Exception as e:
        text = f"Error: {str(e)}"
    return JsonResponse({"text": text})
