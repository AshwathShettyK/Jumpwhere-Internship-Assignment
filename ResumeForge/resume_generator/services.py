import datetime
from django.shortcuts import get_object_or_404
from employees.models import Employee

class ResumeBuilderService:
    @staticmethod
    def get_resume_context(employee_id):
        # Fetch active employee, select related designation and prefetch related skills and tools
        employee = Employee.objects.select_related('designation').prefetch_related(
            'coding_skills', 'tools'
        ).get(pk=employee_id, is_deleted=False)
        
        # Parse professional summary into bullet list lines
        summary_bullets = []
        if employee.professional_summary:
            summary_bullets = [
                line.strip() 
                for line in employee.professional_summary.splitlines() 
                if line.strip()
            ]
        
        # Aggregate coding skills as a comma-separated list
        active_coding = employee.coding_skills.filter(status='active', is_deleted=False)
        coding_skills_str = ", ".join([c.coding_name for c in active_coding]) if active_coding.exists() else "N/A"
        
        # Aggregate tools as a comma-separated list
        active_tools = employee.tools.filter(status='active', is_deleted=False)
        tools_str = ", ".join([t.tool_name for t in active_tools]) if active_tools.exists() else "N/A"
        
        # Fetch active project assignments
        assignments = employee.project_assignments.filter(
            is_deleted=False,
            project__is_deleted=False
        ).select_related('project').prefetch_related('project__coding_skills', 'project__tools')
        
        # Sort projects by start_date descending (newest first).
        # Projects with missing start_date are placed last.
        sorted_assignments = sorted(
            assignments,
            key=lambda a: a.project.start_date or datetime.date.min,
            reverse=True
        )
        
        projects_list = []
        for index, a in enumerate(sorted_assignments, start=1):
            proj = a.project
            
            # Combine project's coding skills and tools for "Technology Used"
            proj_tech = []
            for cs in proj.coding_skills.all():
                proj_tech.append(cs.coding_name)
            for tl in proj.tools.all():
                proj_tech.append(tl.tool_name)
                
            tech_used_str = ", ".join(proj_tech) if proj_tech else "N/A"
            
            # Parse project responsibilities into list lines
            responsibilities = []
            if proj.role_responsibilities:
                responsibilities = [
                    line.strip() 
                    for line in proj.role_responsibilities.splitlines() 
                    if line.strip()
                ]
                
            projects_list.append({
                'index': index,
                'name': proj.project_name,
                'tech_used': tech_used_str,
                'description': proj.description or 'No project description provided.',
                'role': a.role or 'Developer / Member',
                'responsibilities': responsibilities,
                'start_date': proj.start_date,
                'end_date': proj.end_date,
            })
            
        return {
            'employee': employee,
            'summary_bullets': summary_bullets,
            'coding_skills': coding_skills_str,
            'tools': tools_str,
            'projects': projects_list,
        }
