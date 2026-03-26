from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from .models import Module, ModulePart, QuizQuestion, QuizResult, Update
import json
import os
import re


def _validate_student_name(name):
    """Validate and sanitize student name input."""
    if not name or not isinstance(name, str):
        return "Participant"
    # Allow only alphanumeric, spaces, hyphens, and apostrophes
    name = name.strip()[:100]  # Max 100 characters
    if not re.match(r"^[a-zA-Z0-9\s\-']+$", name):
        return "Participant"
    return name


def _verify_module_access(request, module_id):
    """Verify user has access to module based on passed_modules."""
    passed_modules = request.session.get("passed_modules", [])
    modules = list(Module.objects.all().order_by("order").values_list("id", flat=True))

    if not modules:
        return True

    module_index = modules.index(module_id) if module_id in modules else -1
    if module_index == -1:
        return False

    # First module is always accessible
    if module_index == 0:
        return True

    # Check if previous module(s) are passed
    return modules[module_index - 1] in passed_modules


def home(request):
    module_count = Module.objects.count()
    total_parts = ModulePart.objects.count()
    final_question_count = QuizQuestion.objects.filter(module=None).count()

    return render(
        request,
        "home.html",
        {
            "module_count": module_count,
            "total_parts": total_parts,
            "final_question_count": final_question_count,
        },
    )


def modules_list(request):
    modules = Module.objects.all().order_by("order")
    passed_modules = request.session.get("passed_modules", [])
    return render(
        request,
        "modules.html",
        {
            "modules": modules,
            "passed_modules": passed_modules,
        },
    )


def module_detail(request, module_id):
    if not _verify_module_access(request, module_id):
        return render(
            request,
            "error.html",
            {"error": "Access denied. Complete previous modules first."},
            status=403,
        )

    module = get_object_or_404(Module, id=module_id)
    all_modules = Module.objects.order_by("order")
    parts = module.parts.order_by("order")
    passed_modules = request.session.get("passed_modules", [])

    if parts.exists():
        first_part = parts.first()
        return module_part(request, module_id, first_part.order)

    prev_module = (
        Module.objects.filter(order__lt=module.order).order_by("-order").first()
    )

    return render(
        request,
        "module_detail.html",
        {
            "module": module,
            "all_modules": all_modules,
            "passed_modules": passed_modules,
            "prev_module": prev_module,
            "next_module": None,
            "total_modules": all_modules.count(),
            "parts": parts,
        },
    )


def module_part(request, module_id, part_order):
    if not _verify_module_access(request, module_id):
        return render(
            request,
            "error.html",
            {"error": "Access denied. Complete previous modules first."},
            status=403,
        )

    module = get_object_or_404(Module, id=module_id)
    all_modules = Module.objects.order_by("order")
    parts = list(module.parts.order_by("order"))
    passed_modules = request.session.get("passed_modules", [])

    current_part = get_object_or_404(ModulePart, module=module, order=part_order)
    current_index = next((i for i, p in enumerate(parts) if p.order == part_order), 0)
    prev_part = parts[current_index - 1] if current_index > 0 else None
    next_part = parts[current_index + 1] if current_index < len(parts) - 1 else None

    prev_module = (
        Module.objects.filter(order__lt=module.order).order_by("-order").first()
    )

    return render(
        request,
        "module_part.html",
        {
            "module": module,
            "part": current_part,
            "parts": parts,
            "prev_part": prev_part,
            "next_part": next_part,
            "prev_module": prev_module,
            "all_modules": all_modules,
            "passed_modules": passed_modules,
            "total_modules": all_modules.count(),
            "is_last_part": next_part is None,
        },
    )


def module_quiz(request, module_id):
    if not _verify_module_access(request, module_id):
        return render(
            request,
            "error.html",
            {"error": "Access denied. Complete previous modules first."},
            status=403,
        )

    module = get_object_or_404(Module, id=module_id)
    questions = QuizQuestion.objects.filter(module=module)
    passed_modules = request.session.get("passed_modules", [])

    if request.method == "POST":
        student_name = _validate_student_name(request.POST.get("student_name", ""))
        score = 0
        total = questions.count()

        for q in questions:
            user_ans = request.POST.get(f"q_{q.id}", "").strip()
            if user_ans.upper() == q.correct_option.strip().upper():
                score += 1

        percentage = (score / total * 100) if total > 0 else 0
        passed = percentage >= 60

        result = QuizResult.objects.create(
            student_name=student_name, score=score, total=total, module=module
        )

        # Avoid duplicate IDs in passed_modules list
        if passed and module_id not in passed_modules:
            passed_modules.append(module_id)
            request.session["passed_modules"] = passed_modules
            request.session.modified = True

        next_module = (
            Module.objects.filter(order__gt=module.order).order_by("order").first()
        )

        return render(
            request,
            "module_quiz.html",
            {
                "module": module,
                "questions": questions,
                "submitted": True,
                "score": score,
                "total": total,
                "percentage": round(percentage, 1),
                "passed": passed,
                "next_module": next_module,
                "result": result,
            },
        )

    return render(
        request,
        "module_quiz.html",
        {
            "module": module,
            "questions": questions,
        },
    )


def final_quiz(request):
    questions = QuizQuestion.objects.filter(module=None).order_by("id")

    if request.method == "POST":
        student_name = _validate_student_name(request.POST.get("student_name", ""))
        score = 0
        total = questions.count()

        for q in questions:
            user_ans = request.POST.get(f"q_{q.id}", "").strip()
            if user_ans.upper() == q.correct_option.strip().upper():
                score += 1

        percentage = (score / total * 100) if total > 0 else 0
        passed = percentage >= 60

        result = QuizResult.objects.create(
            student_name=student_name,
            score=score,
            total=total,
        )

        return render(
            request,
            "final_quiz.html",
            {
                "questions": questions,
                "submitted": True,
                "score": score,
                "total": total,
                "percentage": round(percentage, 1),
                "passed": passed,
                "result": result,
            },
        )

    return render(
        request,
        "final_quiz.html",
        {
            "questions": questions,
        },
    )


def updates(request):
    updates_list = Update.objects.all().order_by("-id")
    return render(request, "updates.html", {"updates": updates_list})


def chatbot(request):
    return render(request, "chatbot.html")


def certificate(request, result_id):
    result = get_object_or_404(QuizResult, id=result_id, module__isnull=True)
    percentage = (result.score / result.total * 100) if result.total else 0
    passed = percentage >= 60
    return render(
        request,
        "certificate.html",
        {
            "result": result,
            "percentage": round(percentage, 1),
            "passed": passed,
        },
    )


@require_http_methods(["POST"])
@csrf_protect
def chat_api(request):
    """Chat API endpoint with CSRF protection enabled."""
    try:
        data = json.loads(request.body.decode("utf-8"))
        user_message = data.get("message", "").strip()
    except (json.JSONDecodeError, UnicodeDecodeError, AttributeError):
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    if not user_message:
        return JsonResponse({"error": "Message required"}, status=400)

    if len(user_message) > 1000:
        return JsonResponse({"error": "Message too long"}, status=400)

    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return JsonResponse({"error": "API not configured"}, status=500)

    try:
        from groq import Groq

        client = Groq(api_key=api_key)
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are an anti-doping awareness assistant. Keep answers clear and student-friendly.",
                },
                {"role": "user", "content": user_message},
            ],
            temperature=0.4,
            max_tokens=400,
        )
        return JsonResponse({"reply": completion.choices[0].message.content})
    except Exception as e:
        # Don't expose internal error details to client
        return JsonResponse({"error": "Failed to process request"}, status=500)
