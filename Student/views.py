from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Student


def index(request):
    return render(request, 'index.html')


# -------------------------
# STUDENT REGISTRATION
# -------------------------
 

def register(request):
    if request.method == "POST":

        student_name = request.POST.get("student_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        # IMPORTANT: HTML form uses name="dob"
        date_of_birth = request.POST.get("dob")

        gender = request.POST.get("gender")
        course = request.POST.get("course")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Check password
        if password != confirm_password:
            return render(request, "register.html", {
                "error": "Passwords do not match."
            })

        # Check date of birth
        if not date_of_birth:
            return render(request, "register.html", {
                "error": "Date of birth is required."
            })

        # Combine address, city and state
        full_address = f"{address}\n{city}\n{state}"

        student = Student(
            student_name=student_name,
            email=email,
            phone=phone,
            date_of_birth=date_of_birth,
            gender=gender,
            course=course,
            address=full_address,
            password=password
        )

        student.save()

        return redirect("login")

    return render(request, "register.html")



# -------------------------
# STUDENT LOGIN
# -------------------------
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            student = Student.objects.get(
                email=email,
                password=password
            )

            request.session["student_id"] = student.id

            return redirect("student_profile")

        except Student.DoesNotExist:
            return render(
                request,
                "login.html",
                {"error": "Invalid email or password"}
            )

    return render(request, "login.html")


# -------------------------
# STUDENT PROFILE
# -------------------------
def student_profile(request):
    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("login")

    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        request.session.flush()
        return redirect("login")

    return render(
        request,
        "student_profile.html",
        {"student": student}
    )


# -------------------------
# LOGOUT
# -------------------------
def logout_student(request):

    request.session.flush()

    return redirect('index')
 


def about(request):
    return render(request, "about.html")


def courses(request):
    return render(request, "courses.html")


def team(request):
    return render(request, "team.html")


def testimonial(request):
    return render(request, "testimonial.html")


def contact(request):
    return render(request, "contact.html")


def page_404(request):
    return render(request, "404.html")

def students(request):

    student_list = Student.objects.all().order_by("-id")

    return render(
        request,
        "students.html",
        {"students": student_list}
    )

def all_students(request):
    students = Student.objects.all()
    total_students = students.count()

    return render(
        request,
        'all_students.html',
        {
            'students': students,
            'total_students': total_students,
        }
    )



def staff_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "admin" and password == "admin123":

            request.session["is_staff"] = True

            return redirect("all_students")

        return render(request, "staff_login.html", {
            "error": "Invalid username or password"
        })

    return render(request, "staff_login.html")

def newsletter_signup(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if email:
            send_mail(
                "Techno Soft Newsletter Subscription",
                f"A new user subscribed to the Techno Soft newsletter.\n\nSubscriber Email: {email}",
                "nagarajkadabur3@gmail.com",
                ["nagarajkadabur3@gmail.com"],
            )

            messages.success(
                request,
                "Thank you for subscribing to Techno Soft Newsletter!"
            )

        return redirect("index")

    return redirect("index")