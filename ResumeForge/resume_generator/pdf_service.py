from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT, TA_LEFT

class PDFExportService:
    @staticmethod
    def generate_pdf(context):
        buffer = BytesIO()
        
        # Configure A4 document structure with 0.75-inch (54 points) margins
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            leftMargin=54,
            rightMargin=54,
            topMargin=54,
            bottomMargin=54
        )
        
        story = []
        styles = getSampleStyleSheet()
        
        # Define clean, professional color palette
        COLOR_PRIMARY = colors.HexColor('#0f172a')   # Slate 900
        COLOR_SECONDARY = colors.HexColor('#475569') # Slate 600
        COLOR_TEXT = colors.HexColor('#333333')      # Dark Charcoal
        COLOR_DIVIDER = colors.HexColor('#cbd5e1')   # Slate 200
        
        # Define custom styles
        style_body = ParagraphStyle(
            'CVBody',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            leading=14,
            textColor=COLOR_TEXT,
            spaceAfter=3
        )
        
        style_bullet = ParagraphStyle(
            'CVBullet',
            parent=style_body,
            leftIndent=15,
            firstLineIndent=-10,
            spaceAfter=3
        )
        
        style_nested_bullet = ParagraphStyle(
            'CVNestedBullet',
            parent=style_body,
            leftIndent=30,
            firstLineIndent=-10,
            spaceAfter=2
        )
        
        style_heading = ParagraphStyle(
            'CVHeading',
            parent=styles['Heading1'],
            fontName='Helvetica-Bold',
            fontSize=12,
            leading=16,
            textColor=COLOR_PRIMARY,
            spaceBefore=12,
            spaceAfter=6,
            keepWithNext=True
        )
        
        style_project_head = ParagraphStyle(
            'CVProjectHead',
            parent=styles['Normal'],
            fontName='Helvetica-Bold',
            fontSize=10.5,
            leading=14,
            textColor=COLOR_PRIMARY,
            spaceBefore=10,
            spaceAfter=4,
            keepWithNext=True
        )

        employee = context['employee']
        
        # Header block using a 2-column Table: Name on Left, Designation on Right
        name_p = Paragraph(f"<b>{employee.full_name}</b>", ParagraphStyle(
            'HeaderName',
            fontName='Helvetica-Bold',
            fontSize=18,
            leading=22,
            textColor=COLOR_PRIMARY
        ))
        
        designation_name = employee.designation.designation_name if employee.designation else "Software Developer"
        desig_p = Paragraph(f"Designation: <b>{designation_name}</b>", ParagraphStyle(
            'HeaderDesig',
            fontName='Helvetica',
            fontSize=10.5,
            leading=14,
            textColor=COLOR_SECONDARY,
            alignment=TA_RIGHT
        ))
        
        # 100% width of printable A4 is roughly 487 points (595 - 2*54)
        header_table = Table([[name_p, desig_p]], colWidths=[290, 197])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LINEBELOW', (0, 0), (-1, -1), 1, COLOR_DIVIDER),
        ]))
        
        story.append(header_table)
        story.append(Spacer(1, 10))
        
        # 1. Professional Summary Section
        story.append(Paragraph("Professional Summary:", style_heading))
        if context['summary_bullets']:
            for bullet in context['summary_bullets']:
                story.append(Paragraph(f"&bull;&nbsp;&nbsp;{bullet}", style_bullet))
        else:
            story.append(Paragraph("No professional summary bullet points configured.", style_body))
            
        story.append(Spacer(1, 6))

        # 2. Technical Skill Set Section
        story.append(Paragraph("Technical Skill Set:", style_heading))
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;<b>Coding:</b> {context['coding_skills']}", style_bullet))
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;<b>Tools:</b> {context['tools']}", style_bullet))
        
        story.append(Spacer(1, 6))

        # 3. Professional Projects Section
        story.append(Paragraph("Professional Projects", style_heading))
        
        if context['projects']:
            for proj in context['projects']:
                # Project header line: "Project X: Project Name"
                story.append(Paragraph(f"Project {proj['index']}: {proj['name']}", style_project_head))
                
                # Tech used
                story.append(Paragraph(f"&bull;&nbsp;&nbsp;<b>Technology used:</b> {proj['tech_used']}", style_bullet))
                
                # Description
                story.append(Paragraph(f"&bull;&nbsp;&nbsp;<b>Description:</b> {proj['description']}", style_bullet))
                
                # Role and Responsibilities
                story.append(Paragraph("&bull;&nbsp;&nbsp;<b>Role and Responsibilities:</b>", style_bullet))
                
                # Nested responsibilities
                if proj['responsibilities']:
                    for resp in proj['responsibilities']:
                        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{resp}", style_nested_bullet))
                else:
                    story.append(Paragraph(f"&bull;&nbsp;&nbsp;Worked as {proj['role']}.", style_nested_bullet))
                    
                story.append(Spacer(1, 4))
        else:
            story.append(Paragraph("No project assignments available.", style_body))
            
        # Build PDF document
        doc.build(story)
        buffer.seek(0)
        return buffer
