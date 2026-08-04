from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.db.utils import OperationalError, ProgrammingError
from django.shortcuts import render


def get_model(app_label, model_name):
    try:
        return apps.get_model(app_label, model_name)
    except LookupError:
        return None


def safe_count(model):
    if model is None:
        return 0
    try:
        return model.objects.count()
    except (OperationalError, ProgrammingError):
        return 0


def count_field(model, field_name, value):
    if model is None:
        return 0
    try:
        return model.objects.filter(**{field_name: value}).count()
    except (OperationalError, ProgrammingError):
        return 0


def has_field(model, field_name):
    if model is None:
        return False
    return any(field.name == field_name for field in model._meta.get_fields())


def recent_records(model, order_field, limit=5):
    if model is None:
        return []
    try:
        results = model.objects.order_by(f'-{order_field}')[:limit]
        return list(results)
    except (OperationalError, ProgrammingError):
        try:
            results = model.objects.order_by('-pk')[:limit]
            return list(results)
        except (OperationalError, ProgrammingError):
            return []


@login_required(login_url='accounts:login')
def home(request):
    Employee = get_model('employees', 'Employee')
    Project = get_model('projects', 'Project')
    Coding = get_model('coding', 'Coding')
    Tool = get_model('tools', 'Tool')
    Designation = get_model('designations', 'Designation')

    try:
        total_employees = safe_count(Employee)
        total_projects = safe_count(Project)
        total_coding = safe_count(Coding)
        total_tools = safe_count(Tool)
        total_designations = safe_count(Designation)

        current_employees = count_field(Employee, 'status', 'active') if has_field(Employee, 'status') else total_employees
        ex_employees = count_field(Employee, 'status', 'inactive') if has_field(Employee, 'status') else 0
        active_projects = count_field(Project, 'status', 'active') if has_field(Project, 'status') else total_projects
        closed_projects = count_field(Project, 'status', 'closed') if has_field(Project, 'status') else 0

        recent_employees = recent_records(Employee, 'created_at') if has_field(Employee, 'created_at') else recent_records(Employee, 'pk')
        recent_projects = recent_records(Project, 'created_at') if has_field(Project, 'created_at') else recent_records(Project, 'pk')
    except (OperationalError, ProgrammingError):
        total_employees = total_projects = total_coding = total_tools = total_designations = 0
        current_employees = ex_employees = active_projects = closed_projects = 0
        recent_employees = []
        recent_projects = []

    return render(request, 'dashboard/dashboard.html', {
        'total_employees': total_employees,
        'total_projects': total_projects,
        'total_coding': total_coding,
        'total_tools': total_tools,
        'total_designations': total_designations,
        'current_employees': current_employees,
        'ex_employees': ex_employees,
        'active_projects': active_projects,
        'closed_projects': closed_projects,
        'recent_employees': recent_employees,
        'recent_projects': recent_projects,
    })
