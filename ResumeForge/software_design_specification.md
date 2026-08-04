# ResumeForge - Software Design Specification (SDS)

**Document Version:** 1.0.0  
**Status:** Approved Blueprint  
**Authors:** Principal Solution Architect, Enterprise Software Architect, Technical Lead, and HRMS Domain Expert  

---

## 1. Business Analysis

### 1.1 Business Problem
A corporate enterprise with over 100 employees requires a standardized resume format for sales pitches, client proposals, RFP (Request for Proposal) bids, and auditing. Currently, employees design and maintain their resumes independently, causing massive inconsistencies in layout, style, branding, and detail depth. Additionally, employees spend excessive billable hours manually compiling and updating resumes, and the Human Resources (HR) team lacks a single source of truth to track skills, tools, and project histories across the workforce.

### 1.2 Business Goal
Develop **ResumeForge**, a centralized corporate resume management platform. It will enable the HR department to maintain a structured registry of employees, projects, designations, technical coding languages, and tools. The system will automatically compile and export resumes into print-ready PDF and Microsoft Word format, ensuring uniform branding, styling, and visual structure that matches the organization's official format (defined in `SAMPLE - Resume.pdf`).

### 1.3 Current Process vs. Proposed Solution
```
[Current Process]
Employee manually drafts resume -> Inconsistent styles -> Hard for HR to review -> Manual export -> Slow RFP submission
                                                                                                             
[Proposed Solution (ResumeForge)]
HR manages master entities (Coding, Tools, Projects) -> HR links Employees -> Automated 1-Click PDF/Word Exports
```

### 1.4 Expected Benefits
* **Brand Consistency:** 100% uniformity in fonts, alignment, margins, and content structure for all client-facing materials.
* **Time Savings:** HR can generate resumes in seconds rather than spending hours formatting documents.
* **Searchability & Inventory:** Centrally query which employees possess specific coding skills or tools.
* **Operational Readiness:** Drastically reduce response times for client proposals and RFPs.

### 1.5 Actors
* **Primary Actor:** HR Admin / HR Staff (manage registry data, assign projects to employees, compile and download resumes).
* **Secondary Actor:** System Administrator (manages accounts and performs database configurations).
* **System Boundary:** The Django-based web interface, the MySQL database server, the Word/PDF compilation engine, and the static files storage.

### 1.6 Business Rules
1. **Audit Logs:** Every change to core records must track `created_at`, `updated_at`, `created_by`, and `updated_by`.
2. **Soft Deletes:** No active records can be hard-deleted from the database. A boolean flag (`is_deleted`) must be toggled.
3. **Descending Order:** Projects in the exported resume must always appear in descending order of project start dates (most recent first).
4. **Technology Aggregation:** Technology used in a project is a combination of coding languages and tool parameters mapped from the database.
5. **No Watermarks:** Background watermarks are omitted from the exports to maintain visual clarity.

---

## 2. Requirement Analysis

### 2.1 Functional Requirements (FR)
* **FR-1 (Authentication):** Secure user login and registration for the HR team.
* **FR-2 (Dashboard):** Show statistics: total active employees, projects, coding skills, and tools.
* **FR-3 (Designation CRUD):** Maintain list of official corporate job titles.
* **FR-4 (Coding Skills CRUD):** Maintain master directory of coding languages (e.g., JavaScript, Python).
* **FR-5 (Tools CRUD):** Maintain master directory of developer tools (e.g., VSCode, Postman, Git).
* **FR-6 (Projects CRUD):** Manage project catalog, including start/end dates, description, roles, and technologies used (combination of coding and tools).
* **FR-7 (Employee Registry CRUD):** Add and update employees with designation, summary, and lists of coding/tools skills.
* **FR-8 (Project Mapping):** Map employees to projects they have worked on, capturing their specific role.
* **FR-9 (PDF Resume Export):** Export a styled PDF matching the layout of the sample resume.
* **FR-10 (Word Resume Export):** Export a styled `.docx` file matching the layout of the sample resume.

### 2.2 Non-Functional Requirements (NFR)
* **NFR-1 (Security):** Enforce secure session cookies, CSRF protection, SQL injection prevention, and password hashing (PBKDF2).
* **NFR-2 (Maintainability):** Follow Django MVC architecture with a decoupled service layer.
* **NFR-3 (Reliability):** Database constraints and unique indexes on active non-deleted rows to prevent duplicate records.
* **NFR-4 (Visual Alignment):** Pixel-perfect matching with `SAMPLE - Resume.pdf` layout.

### 2.3 Requirement Traceability Matrix (RTM)

| Req ID | Requirement Description | Priority | Depends On | Covered By Module |
| :--- | :--- | :---: | :---: | :--- |
| **FR-1** | HR Authentication (Login/Register) | High | None | Accounts |
| **FR-2** | Dashboard Metrics | High | FR-3, FR-6, FR-7 | Dashboard |
| **FR-3** | Designation CRUD | Medium | None | Designations |
| **FR-4** | Coding Skills CRUD | Medium | None | Coding |
| **FR-5** | Tools CRUD | Medium | None | Tools |
| **FR-6** | Projects CRUD | High | FR-4, FR-5 | Projects |
| **FR-7** | Employee Registry | High | FR-3, FR-4, FR-5 | Employees |
| **FR-8** | Project Assignment | High | FR-6, FR-7 | Employee Project Mapping |
| **FR-9** | PDF Generation | High | FR-7, FR-8 | PDF Export |
| **FR-10**| Microsoft Word Generation | High | FR-7, FR-8 | Word Export |
| **NFR-1**| CSRF, SQLi, XSS, Session Guard | High | FR-1 | Accounts, Custom Middleware |
| **NFR-2**| Audit Fields tracking | Medium | None | Common / Abstract Base Model |
| **NFR-3**| Soft Delete on Delete requests | High | None | Common / Soft Delete Manager |
| **NFR-4**| Descending Order of Project Timeline | High | FR-8 | Resume Generator / Service |

---

## 3. System Architecture

ResumeForge uses a robust, layered model-view-controller (MVC) architecture built on Python Django, backed by a MySQL database.

```
       +--------------------------------------------------------+
       |                  Web Browser Client                    |
       |  (HTML5 / CSS3 / Vanilla JS / Fetch API / Bootstrap)   |
       +----------------------------+---------------------------+
                                    | HTTP Requests (JSON/HTML)
                                    v
       +--------------------------------------------------------+
       |                  Django Web Server                     |
       |  +--------------------------------------------------+  |
       |  |                    Middleware                    |  |
       |  | (CSRF, Authentication, LoginRequiredMiddleware)  |  |
       |  +-------------------------+------------------------+  |
       |                            |                           |
       |  +-------------------------+------------------------+  |
       |  |                      Views                       |  |
       |  |   (FBVs & CBVs rendering templates and APIs)     |  |
       |  +-------------------------+------------------------+  |
       |                            |                           |
       |  +-------------------------+------------------------+  |
       |  |                  Service Layer                   |  |
       |  | (EmployeeService, ResumeBuilderService, PDFService)|  |
       |  +--------------------+-------------------+---------+  |
       |                       |                   |            |
       |                       |                   |            |
       |  +--------------------v---+           +---v---------+  |
       |  |      Django Models     |           | Generators  |  |
       |  | (ORM / Soft Delete QA) |           |  (WeasyPrint|  |
       |  +------------+-----------+           | python-docx)|  |
       |               |                       +-------------+  |
       +---------------+----------------------------------------+
                       | SQL Queries
                       v
       +--------------------------------------------------------+
       |                     MySQL Server                       |
       | (InnoDB Engine, Custom unique constraints on active)   |
       +--------------------------------------------------------+
```

---

## 4. Application Modules

### 4.1 Accounts Module
* **Purpose:** Handles user enrollment, session authentication, and access control.
* **Responsibilities:** Validate login credentials, issue session cookies, manage password resets, and register new HR accounts.
* **Dependencies:** Django core auth, session database tables.
* **Inputs:** Username, email, password.
* **Outputs:** Auth session cookie, redirection to Dashboard.
* **Business Logic:** Block access to all other application routes if the user is unauthenticated. Enforce Django password complexity.

### 4.2 Dashboard Module
* **Purpose:** Serves as the launchpad screen for HR users.
* **Responsibilities:** Count and display active employees, active projects, coding languages, and developer tools.
* **Dependencies:** `employees.models`, `projects.models`, `coding.models`, `tools.models`.
* **Inputs:** Fetch requests.
* **Outputs:** Rendered dashboard page with statistics cards.
* **Business Logic:** Read database counts of only active (non-deleted) records.

### 4.3 Coding Module
* **Purpose:** Manages the registry of programming languages.
* **Responsibilities:** Create, edit, list, and soft-delete coding languages.
* **Dependencies:** None.
* **Inputs:** Coding language name, description, status.
* **Outputs:** Success alerts, master dropdown source for project and employee registry.
* **Validation:** Language name must be unique among active entries.

### 4.4 Tools Module
* **Purpose:** Manages developer tools and platforms database.
* **Responsibilities:** Create, edit, list, and soft-delete developer tools.
* **Dependencies:** None.
* **Inputs:** Tool name, description, status.
* **Outputs:** Success alerts, dropdown entries for mapping.
* **Validation:** Tool name must be unique among active entries.

### 4.5 Designation Module
* **Purpose:** Manages corporate job titles.
* **Responsibilities:** Define designations to classify employee hierarchy.
* **Dependencies:** None.
* **Inputs:** Designation name, description.
* **Outputs:** Dropdown values for employee mapping.
* **Validation:** Unique check on designation name.

### 4.6 Projects Module
* **Purpose:** Manages the registry of company projects.
* **Responsibilities:** Define project metadata, timelines, descriptions, role templates, and technological stacks.
* **Dependencies:** Coding module, Tools module.
* **Inputs:** Name, description, start date, end date, status, coding languages (multi-select), tools (multi-select).
* **Outputs:** Project listings, technology tags.
* **Business Logic:** Merge Coding and Tools collections to form the project’s "Technology Used" field.
* **Validation:** End date must be greater than or equal to start date.

### 4.7 Employees Module
* **Purpose:** Manages employee profiles and professional details.
* **Responsibilities:** Store names, email addresses, phone numbers, designations, coding skills, developer tools, and professional summaries.
* **Dependencies:** Designation, Coding, Tools.
* **Inputs:** First name, last name, email, phone, designation id, coding skill ids, tool ids, status, professional summary (paragraph text representing resume bullet points).
* **Outputs:** Profile summary page.
* **Validation:** Active unique email constraint.

### 4.8 Employee Project Mapping Module
* **Purpose:** Links employees to their respective project histories.
* **Responsibilities:** Associate an employee with a project, designating their specific role during that project.
* **Dependencies:** Employees module, Projects module.
* **Inputs:** Employee ID, Project ID, Role title.
* **Outputs:** Relationship links shown in project detail page.
* **Business Logic:** Maintain chronological tracking.

### 4.9 Resume Generator Module
* **Purpose:** Orchestrates the assembly of resumes.
* **Responsibilities:** Fetch employee profile data, designations, skill lists, and mapped projects, sorting them to render preview states.
* **Dependencies:** Employees, Projects, Mappings.
* **Inputs:** Employee ID.
* **Outputs:** Standardized resume structure.

### 4.10 Word Export Module
* **Purpose:** Compiles resume structures into Word documents.
* **Responsibilities:** Construct `.docx` templates programmatically matching fonts, headers, and bullet formats.
* **Dependencies:** Resume Generator, `python-docx` library.
* **Inputs:** Formatted resume structure.
* **Outputs:** Styled Word binary stream download.

### 4.11 PDF Export Module
* **Purpose:** Compiles resume structures into PDF documents.
* **Responsibilities:** Render print-ready CSS templates to output static PDF formats.
* **Dependencies:** Resume Generator, HTML-to-PDF library (WeasyPrint).
* **Inputs:** Formatted resume structure.
* **Outputs:** Styled PDF binary stream download.

### 4.12 Admin Module
* **Purpose:** Django Admin Portal integration.
* **Responsibilities:** Direct database manipulation for super-users.
* **Dependencies:** Django admin contrib app.
* **Inputs:** Admin panels.
* **Outputs:** Direct database changes.

---

## 5. Database Design

```
+-------------------------------------------------------------------------------------------------------+
|                                              BaseModel                                                |
|  - created_at: DateTime                                                                               |
|  - updated_at: DateTime                                                                               |
|  - is_deleted: Boolean                                                                                |
|  - created_by: ForeignKey (User)                                                                      |
|  - updated_by: ForeignKey (User)                                                                      |
+-------------------------------------------------------------------------------------------------------+
```

### 5.1 Designations Table (`designations_designation`)
* **Purpose:** Stores corporate job titles.
* **Columns:**
  * `id`: BIGINT (Primary Key, Auto Increment)
  * `designation_name`: VARCHAR(100) (Unique, Not Null)
  * `description`: TEXT (Nullable)
  * `status`: VARCHAR(8) (Default: 'active', Choices: 'active', 'inactive')
  * `is_deleted`: BOOLEAN (Default: False)
  * `created_at`: DATETIME (Auto Add)
  * `updated_at`: DATETIME (Auto Update)
  * `created_by_id`: INT (Foreign Key -> auth_user.id, Nullable)
  * `updated_by_id`: INT (Foreign Key -> auth_user.id, Nullable)
* **Indexes:** `idx_designation_active` (`designation_name`, `is_deleted`)

### 5.2 Coding Skills Table (`coding_coding`)
* **Purpose:** Stores coding languages (e.g., Python, JavaScript).
* **Columns:**
  * `id`: BIGINT (Primary Key, Auto Increment)
  * `coding_name`: VARCHAR(100) (Unique, Not Null)
  * `description`: TEXT (Nullable)
  * `status`: VARCHAR(8) (Default: 'active')
  * `is_deleted`: BOOLEAN (Default: False)
  * `created_at`: DATETIME
  * `updated_at`: DATETIME
  * `created_by_id`: INT (Foreign Key -> auth_user.id)
  * `updated_by_id`: INT (Foreign Key -> auth_user.id)
* **Indexes:** `idx_coding_active` (`coding_name`, `is_deleted`)

### 5.3 Tools Table (`tools_tool`)
* **Purpose:** Stores developer tools (e.g., VSCode, Git).
* **Columns:**
  * `id`: BIGINT (Primary key)
  * `tool_name`: VARCHAR(100) (Unique, Not Null)
  * `description`: TEXT (Nullable)
  * `status`: VARCHAR(8) (Default: 'active')
  * `is_deleted`: BOOLEAN (Default: False)
  * `created_at`: DATETIME
  * `updated_at`: DATETIME
  * `created_by_id`: INT (Foreign Key -> auth_user.id)
  * `updated_by_id`: INT (Foreign Key -> auth_user.id)
* **Indexes:** `idx_tool_active` (`tool_name`, `is_deleted`)

### 5.4 Projects Table (`projects_project`)
* **Purpose:** Contains all corporate project records.
* **Columns:**
  * `id`: BIGINT (Primary Key)
  * `project_name`: VARCHAR(100) (Unique, Not Null)
  * `description`: TEXT (Not Null)
  * `role_responsibilities`: TEXT (Not Null - stored as line-separated bullet points)
  * `start_date`: DATE (Not Null)
  * `end_date`: DATE (Nullable, for active ongoing projects)
  * `status`: VARCHAR(8) (Default: 'active', Choices: 'active', 'closed')
  * `is_deleted`: BOOLEAN (Default: False)
  * `created_at`: DATETIME
  * `updated_at`: DATETIME
  * `created_by_id`: INT (Foreign Key -> auth_user.id)
  * `updated_by_id`: INT (Foreign Key -> auth_user.id)
* **Indexes:** `idx_project_timeline` (`start_date`, `is_deleted`)

### 5.5 Employees Table (`employees_employee`)
* **Purpose:** Stores employee personal profiles.
* **Columns:**
  * `id`: BIGINT (Primary Key)
  * `first_name`: VARCHAR(50) (Not Null)
  * `last_name`: VARCHAR(50) (Not Null)
  * `email`: VARCHAR(254) (Not Null)
  * `phone`: VARCHAR(20) (Nullable)
  * `designation_id`: BIGINT (Foreign Key -> designations_designation.id, SET_NULL on delete)
  * `professional_summary`: TEXT (Not Null - stored as line-separated bullet points)
  * `status`: VARCHAR(8) (Default: 'active', Choices: 'active', 'inactive')
  * `is_deleted`: BOOLEAN (Default: False)
  * `created_at`: DATETIME
  * `updated_at`: DATETIME
  * `created_by_id`: INT (Foreign Key -> auth_user.id)
  * `updated_by_id`: INT (Foreign Key -> auth_user.id)
* **Indexes:** `idx_employee_email` (`email`, `is_deleted`)

### 5.6 Employee Project Mapping Table (`employees_employeeproject`)
* **Purpose:** Links employees to their project histories.
* **Columns:**
  * `id`: BIGINT (Primary Key)
  * `employee_id`: BIGINT (Foreign Key -> employees_employee.id, CASCADE on delete)
  * `project_id`: BIGINT (Foreign Key -> projects_project.id, CASCADE on delete)
  * `role`: VARCHAR(100) (Not Null)
  * `is_deleted`: BOOLEAN (Default: False)
  * `created_at`: DATETIME
  * `updated_at`: DATETIME
  * `created_by_id`: INT (Foreign Key -> auth_user.id)
  * `updated_by_id`: INT (Foreign Key -> auth_user.id)
* **Indexes:** `idx_emp_proj` (`employee_id`, `project_id`, `is_deleted`)

---

## 6. Entity Relationship (ER) Diagram

```
 +------------------------+             +---------------------------+
 |      DESIGNATION       |             |         EMPLOYEE          |
 +------------------------+             +---------------------------+
 | PK  id                 |             | PK  id                    |
 |     designation_name   |---(1:N)---->| FK  designation_id        |
 |     is_deleted         |             |     first_name            |
 +------------------------+             |     last_name             |
                                        |     email                 |
 +------------------------+             |     professional_summary  |
 |        CODING          |             |     is_deleted            |
 +------------------------+             +---------------------------+
 | PK  id                 |                       |
 |     coding_name        |                       | (1:N)
 |     is_deleted         |                       v
 +------------------------+             +---------------------------+
             |                          |     EMPLOYEE_PROJECT      |
             | (ManyToMany)             +---------------------------+
             v                          | PK  id                    |
 +------------------------+             | FK  employee_id           |
 |    EMPLOYEE_CODING     |<---(N:1)----| FK  project_id            |
 +------------------------+             |     role                  |
 | FK  employee_id        |             |     is_deleted            |
 | FK  coding_id          |             +---------------------------+
 +------------------------+                       ^
                                                  | (N:1)
 +------------------------+                       |
 |         TOOL           |             +---------------------------+
 | +--------------------+ |             |          PROJECT          |
 | | PK  id             | |             +---------------------------+
 | |     tool_name      | |             | PK  id                    |
 | |     is_deleted     | |             |     project_name          |
 | +--------------------+ |             |     description           |
 +------------------------+             |     role_responsibilities |
             |                          |     start_date            |
             | (ManyToMany)             |     end_date              |
             v                          |     is_deleted            |
 +------------------------+             +---------------------------+
 |     EMPLOYEE_TOOLS     |<---(N:1)----+             |
 +------------------------+                           | (ManyToMany)
 | FK  employee_id        |                           v
 | FK  tool_id            |             +---------------------------+
 +------------------------+             |      PROJECT_TECHNOLOGY   |
                                        +---------------------------+
                                        | FK  project_id            |
                                        | FK  coding_id (Nullable)  |
                                        | FK  tool_id (Nullable)    |
                                        +---------------------------+
```

### 6.1 Relationship Descriptions
1. **Designation to Employee (1:N):** An employee can only have a single designation. A designation can belong to multiple employees.
2. **Employee to Project Mapping (N:M):** An employee can participate in multiple projects over time, and each project features multiple assigned employees. This is handled by the intermediary mapping table (`EmployeeProject`).
3. **Employee to Coding & Tools (N:M):** Employees map to multiple programming languages and development utilities.
4. **Project to Coding & Tools (N:M):** Each project defines its technology stack via master collections.

---

## 7. Django Application Structure

The codebase is organized into cleanly separated applications containing self-contained business logic:

```
ResumeForge/
│
├── ResumeForge/             # Main settings, routing configuration
│   ├── settings.py          # Environment configuration & app registration
│   ├── urls.py              # Main URL route mapping
│   └── wsgi.py              # Web Server Gateway Interface entry point
│
├── accounts/                # Authentication, authorization, and HR users
├── dashboard/               # HR Admin statistics dashboard
├── designations/            # Designation management app
├── employees/               # Employee registry, profiles, and project assignments
├── projects/                # Project register management
├── coding/                  # Programming languages master registry
├── tools/                   # Developer tools master registry
├── resume_generator/        # Engine coordinating Word and PDF compiling
│
├── static/                  # Shared stylesheet files, scripts, images
└── templates/               # Global directory for layout markup
```

### 7.1 Common Module Pattern (Service Layer & Abstract Models)
All models inherit from an abstract `TimeStampedModel` that contains standard audit attributes. Data operations are delegated to custom Service layers (e.g., `EmployeeService`), isolating business logic from Django Views.

---

## 8. URL Design

All endpoints require authentication (enforced by `LoginRequiredMiddleware` except for accounts/login/).

### 8.1 Accounts App
* `/accounts/login/` [GET, POST]: Renders/Processes user logins. No Auth required.
* `/accounts/logout/` [POST]: Invalidates sessions and redirects to login.

### 8.2 Dashboard App
* `/` or `/dashboard/` [GET]: Serves statistics overview.

### 8.3 Designations App
* `/designations/` [GET]: Renders list.
* `/designations/create/` [GET, POST]: Create new designations.
* `/designations/edit/<id>/` [GET, POST]: Update designations.
* `/designations/delete/<id>/` [POST]: Soft-deletes designations.

### 8.4 Coding App
* `/coding/` [GET]: Lists coding entries.
* `/coding/create/` [GET, POST]: Adds a new language.
* `/coding/edit/<id>/` [GET, POST]: Updates languages.
* `/coding/delete/<id>/` [POST]: Soft-deletes languages.

### 8.5 Tools App
* `/tools/` [GET]: Lists developer tools.
* `/tools/create/` [GET, POST]: Adds a new tool.
* `/tools/edit/<id>/` [GET, POST]: Updates tools.
* `/tools/delete/<id>/` [POST]: Soft-deletes tools.

### 8.6 Projects App
* `/projects/` [GET]: Lists corporate projects.
* `/projects/create/` [GET, POST]: Create a new project.
* `/projects/edit/<id>/` [GET, POST]: Update a project.
* `/projects/delete/<id>/` [POST]: Soft-deletes projects.

### 8.7 Employees App
* `/employees/` [GET]: Lists employees.
* `/employees/create/` [GET, POST]: Create employee record.
* `/employees/edit/<id>/` [GET, POST]: Update profile.
* `/employees/delete/<id>/` [POST]: Soft-deletes employees.
* `/employees/<id>/assign-project/` [GET, POST]: Assigns employees to projects.

### 8.8 Resume Generator App
* `/resume/<id>/preview/` [GET]: HTML preview of the generated resume.
* `/resume/<id>/download/pdf/` [GET]: Compiles and returns standard PDF download.
* `/resume/<id>/download/word/` [GET]: Compiles and returns standard Word download.

---

## 9. Screen Design

The design of the screens prioritizes a clean, modern, and highly usable interface built using a sleek slate-gray and corporate-blue design palette. 

### 9.1 Global Sidebar UI Design
Every page after login features a left navigation sidebar with a dark theme (deep navy `#0B132B` background, teal hover colors, and clear icon sets).

### 9.2 Screen Inventory

#### 1. Login Screen
* **Fields:** Username/Email input, Password input.
* **Buttons:** Login button (primary blue).
* **Validation:** Custom alerts for missing fields or incorrect credentials.

#### 2. Dashboard Screen
* **Metrics:** 4 display cards with counts of Employees, Projects, Languages, and Tools.
* **Actions:** Quick links to "Add Employee" and "Add Project".

#### 3. Coding List Screen
* **Table Columns:** Language Name, Description, Status (Active/Inactive), Actions (Edit, Delete).
* **Actions:** "Create Coding Skill" button at top right.

#### 4. Coding Create / Edit Screen
* **Fields:** Skill Name (input text), Description (textarea), Status (dropdown: Active/Inactive).
* **Actions:** Save, Cancel.

#### 5. Tools List Screen
* **Table Columns:** Tool Name, Description, Status, Actions.
* **Actions:** "Create Tool" button.

#### 6. Projects List Screen
* **Table Columns:** Project Name, Tech Stack (joined string of coding & tools), Timeline (Start/End Date), Status, Actions.
* **Actions:** "Create Project" button. Search bar filtering by project name.

#### 7. Projects Create / Edit Screen
* **Fields:** Name (text), Start Date (date-picker), End Date (date-picker), Status (dropdown), Description (textarea), Role & Responsibilities (textarea), Coding Tech (multi-select), Tools Tech (multi-select).
* **Actions:** Save, Cancel.

#### 8. Employees List Screen
* **Table Columns:** Name, Email, Designation, Project Count, Status, Actions (Edit, Project Mapping, Resume Download Dropdown, Delete).
* **Search:** Filter by employee name.

#### 9. Employees Create / Edit Screen
* **Fields:** First Name, Last Name, Email, Phone, Designation (dropdown), Professional Summary (textarea), Coding Languages (multi-select), Tools (multi-select), Status (dropdown).
* **Actions:** Save, Cancel.

#### 10. Project Assignment Screen
* **Fields:** Employee (static text), Project (dropdown), Role (text input).
* **Actions:** Map Project, Back to Employee List.

#### 11. Resume Preview Screen
* **Description:** An inline HTML render matching `SAMPLE - Resume.pdf` layout.
* **Actions:** Download Word, Download PDF, Close Preview.

---

## 10. Menu Structure

The left sidebar layout contains the following structure:

```
[Dashboard]
  ├── [Employees] 
  │     └── [Add Employee]
  ├── [Projects]
  │     └── [Add Project]
  ├── [Master Data]
  │     ├── [Designations]
  │     ├── [Coding Skills]
  │     └── [Tools]
  └── [Logout]
```

### 10.1 Access Rules
All logged-in users belong to the HR team. Super-admins have full permissions to add users and delete master items, while staff accounts can view, create, and update records.

---

## 11. Workflow Diagrams

### 11.1 Employee Creation Flow
```
HR Staff -> Input Details (Form) -> POST /employees/create/ 
   -> Form Valid?
        ├── YES -> Save to DB (Status Active) -> Redirect list
        └── NO  -> Render form with validation errors
```

### 11.2 Resume Generation Flow
```
HR clicks "Download" -> Request Route -> Get Employee Data 
   -> Query active mapped projects (sorted DESC by start_date)
   -> Aggregate technical skills (Languages & Tools)
   -> Run rendering engine (WeasyPrint / python-docx)
   -> Return file binary stream to user browser
```

---

## 12. Form Design

All user input forms enforce strict sanitization rules:

| Form Name | Field Name | Input Type | Validation Rules | Dropdown Source |
| :--- | :--- | :--- | :--- | :--- |
| **LoginForm** | username | Text | Required | None |
| | password | Password | Required | None |
| **EmployeeForm**| first_name | Text | Max 50 chars, Required | None |
| | last_name | Text | Max 50 chars, Required | None |
| | email | Email | Valid Email Format, Active Unique Check | None |
| | designation| Select | Required | `designations_designation` |
| | coding_skills| Multi-Select | Minimum 1 select, Optional | `coding_coding` |
| | tools | Multi-Select | Optional | `tools_tool` |
| | summary | Textarea | Required, min length 50 | None |
| **ProjectForm** | project_name | Text | Max 100 chars, Active Unique Check | None |
| | start_date | Date | Required | None |
| | end_date | Date | Optional, Must be >= start_date | None |
| | description | Textarea | Required | None |
| | responsibilities| Textarea | Required | None |

---

## 13. Validation Matrix

```
       +--------------------------------------------------------+
       |                  Validation Layers                     |
       +--------------------------------------------------------+
       | 1. UI Level:                                           |
       |    - Required fields check                             |
       |    - Client-side email format regex check              |
       |    - End Date >= Start Date checks                     |
       +--------------------------------------------------------+
                                    |
                                    v
       +--------------------------------------------------------+
       | 2. Business Logic Level (Services):                    |
       |    - Duplicate active email check                      |
       |    - Prevent assigning duplicate active projects       |
       |    - Validate foreign key references                   |
       +--------------------------------------------------------+
                                    |
                                    v
       +--------------------------------------------------------+
       | 3. Database Layer:                                     |
       |    - Unique constraints (filtered on is_deleted=False) |
       |    - Null check constraints                            |
       +--------------------------------------------------------+
```

---

## 14. Resume Generation Design

This section defines the extraction, structuring, and conversion of database records into exports that match `SAMPLE - Resume.pdf`.

```
 +----------------------------------------------------------------------------+
 |                      SAMPLE RESUME STRUCTURE LAYOUT                        |
 +----------------------------------------------------------------------------+
 |  [NAME]                                                      [DESIGNATION] |
 |  (Large, bold, 18pt)                                 (Italic, normal, 11pt)|
 |                                                                            |
 |  Professional Summary:                                                     |
 |  - Bullet point 1... (Having X years and Y months of total experience...)   |
 |  - Bullet point 2...                                                       |
 |                                                                            |
 |  Technical Skill Set:                                                      |
 |  - Coding: Javascript, Python, HTML 5, CSS 3, Vue js, Django               |
 |  - Tools: VsCode, Postman, Github, Gitlab, Bitbucket                       |
 |                                                                            |
 |  Professional Projects:                                                    |
 |  - Project 1: Time tag                                                     |
 |    - Technology used: Laravel, Mysql, Javascript, Jquery, Ajax, Html...    |
 |    - Description: Time tag is a website used to fill employee timesheets...|
 |    - Role and Responsibilities:                                            |
 |      - Bullet 1...                                                         |
 |      - Bullet 2...                                                         |
 |                                                                            |
 |  - Project 2: OurShopping                                                  |
 |    ...                                                                     |
 +----------------------------------------------------------------------------+
```

### 14.1 Top Header
* **Layout:** A two-column top border section.
* **Left:** Employee’s full name (`first_name` + `last_name`) in bold, dark slate color, size 18pt.
* **Right:** Mapped Designation Name in italicized charcoal color, size 11pt, right-aligned.
* **Divider:** A solid light gray line separating the header from the content.

### 14.2 Professional Summary Section
* **Title:** "Professional Summary:" (12pt, bold).
* **Generation:** Split the `professional_summary` text by newlines. Render each line as a clean bullet point.

### 14.3 Technical Skill Set Section
* **Title:** "Technical Skill Set:" (12pt, bold).
* **Layout:** Indented block.
* **Line 1 (Coding):** Prefix `Coding:` (bold), followed by a comma-separated string of the employee’s active mapped `Coding` names.
* **Line 2 (Tools):** Prefix `Tools:` (bold), followed by a comma-separated string of the employee’s active mapped `Tools` names.

### 14.4 Professional Projects Section
* **Title:** "Professional Projects" (12pt, bold).
* **Ordering Algorithm:** 
  1. Retrieve all mapped project records for the target employee via `EmployeeProject`.
  2. Order the collection by `project.start_date` descending (newest first).
  3. Loop through and print each project card.
* **Project Card Layout:**
  * **Line 1 (Project Title):** `Project X: [Project Name]` (bold, where X is an incrementing index starting from 1).
  * **Line 2 (Technology Used):** Prefix `Technology used:` (bold), followed by a list of mapped coding skills and tools.
  * **Line 3 (Description):** Prefix `Description:` (bold), followed by the project description.
  * **Line 4 (Role and Responsibilities):** Prefix `Role and Responsibilities:` (bold). The responsibilities text is split by newlines, and each line is rendered as a sub-bullet.

### 14.5 Word Generation Algorithm (`python-docx`)
```python
# Programmatic compilation overview:
doc = Document()
# Set Margins to 1 inch globally
# Set standard styling font to 'Calibri' or 'Arial'
# Construct tables with hidden borders for the Header to align Name left and Designation right.
# Iterate and write text runs, applying bold styling where required.
```

### 14.6 PDF Generation Algorithm (`WeasyPrint`)
Write a custom HTML resume template styling layout details in CSS. Use `@page` margin rules to define standard printer formats.
```css
@page {
    size: A4;
    margin: 1.2cm;
}
body {
    font-family: 'Calibri', sans-serif;
    color: #2b2b2b;
}
```
Render the template using Django’s context engine, and pass the resulting string directly into the WeasyPrint client to stream back a clean PDF.

---

## 15. Service Layer Design

ResumeForge decouples business rule logic from views by using dedicated Service classes.

### 15.1 AuthService
* **Function:** Validates credentials, creates user accounts, and handles logins/logouts.

### 15.2 DashboardService
* **Function:** Queries database tables to aggregate analytics data.

### 15.3 EmployeeService
* **Function:** Handles employee creation and updates, mapping of skill fields, and email verification check.

### 15.4 ProjectService
* **Function:** Saves projects, maps tech stacks, and checks end-date parameters.

### 15.5 ResumeBuilderService
* **Function:** Queries employee records, aggregates technologies, and returns a formatted JSON schema ready for export.

### 15.6 PDFService & WordService
* **Function:** Converts raw resume schemas into PDF and Word streams respectively.

### 15.7 SoftDeleteService
* **Function:** Sets `is_deleted=True` for target rows and updates corresponding dependent entries.

### 15.8 AuditService
* **Function:** Automatically populates `created_by` and `updated_by` columns using the request user context.

---

## 16. Security Design

* **Authentication Guard:** Every endpoint (except `/accounts/login/`) is protected by `LoginRequiredMiddleware` to prevent anonymous access.
* **CSRF Protection:** Django’s CSRF protection middleware is enabled globally.
* **SQL Injection Prevention:** Enforce using Django’s standard ORM API queries (`filter()`, `exclude()`, `save()`). Avoid writing raw SQL queries.
* **XSS Prevention:** Ensure Django template auto-escaping is active. Use HTML-safe encoding when rendering text areas.
* **Safe Session Management:**
  * `SESSION_COOKIE_AGE = 1209600` (14 days session expiry)
  * `SESSION_COOKIE_SECURE = True` (Transmitted only over HTTPS in production)
  * `SESSION_COOKIE_HTTPONLY = True` (Blocks access via JavaScript)

---

## 17. Testing Design

A complete suite of tests must be maintained:

### 17.1 Test Categories

#### Unit Tests
* Validate database level constraints.
* Test soft-deletion logic to ensure deleted records are omitted from default queries.
* Verify unique constraint limits on active entries.

#### Integration Tests
* Test employee project mappings.
* Test that project technology stack associations merge properly.

#### Functional Tests
* Simulate a user logging in and generating a resume.
* Verify that the exported PDF and Word files contain all of the employee's project details.

### 17.2 Sample Test Cases
1. **Soft Delete Check:** Assert that deleting an Employee record toggles `is_deleted=True` and does not delete the row.
2. **Project Date Validation:** Assert that creating a project with `end_date` < `start_date` raises a validation error.
3. **Email Constraint Check:** Assert that saving two active employees with duplicate emails raises an Integrity Error.

---

## 18. Deployment Design

```
                     +---------------------------------------+
                     |            Client Request             |
                     +-------------------+-------------------+
                                         | HTTPS (Port 443)
                                         v
                     +---------------------------------------+
                     |           Cloud Load Balancer         |
                     |             (SSL Offloading)          |
                     +-------------------+-------------------+
                                         | HTTP (Port 80)
                                         v
                     +---------------------------------------+
                     |            Web Application            |
                     |         (WSGI / Gunicorn Host)        |
                     +-------------------+-------------------+
                                         |
                        +----------------+----------------+
                        |                                 |
                        v                                 v
        +-------------------------------+  +-------------------------------+
        |         MySQL Database        |  |         Static Assets         |
        |       (Amazon RDS / Host)     |  |       (AWS S3 / CDN Cloud)    |
        +-------------------------------+  +-------------------------------+
```

* **Application Hosting:** Django app deployed to a cloud server using a WSGI server (e.g., Gunicorn).
* **Database Engine:** Managed MySQL database instance.
* **Environment Configuration:** Store all credentials (database password, secret keys, debug flags) securely inside a `.env` file.
* **Static Assets:** Collect and serve static files using WhiteNoise or AWS S3.

---

## 19. Implementation Roadmap

### Milestone 1: Core System & DB Setup (Estimated: 2 days)
* Setup base models (`SoftDeleteModel`, `TimeStampedModel`).
* Configure user authentication and session middleware.
* Run initial database migrations.

### Milestone 2: Master Data Entries (Estimated: 3 days)
* Build CRUD pages for Designations, Coding Skills, and Tools.
* Create tests for constraints and soft-delete features.

### Milestone 3: Project & Employee Registry (Estimated: 4 days)
* Build Projects CRUD and Multi-select tech stack mapping.
* Build Employees CRUD and Project Mapping screens.
* Test dates and email validation constraints.

### Milestone 4: Resume Generation & Exports (Estimated: 5 days)
* Code the resume rendering service.
* Implement PDF compilation using WeasyPrint.
* Implement Word document generation using `python-docx`.
* Write tests to verify layout formatting and project ordering.

---

## 20. Self Audit

We performed a thorough self-audit to verify that this Software Design Specification matches 100% of the project requirements and the sample resume layout.

| Requirement Source | Requirement / Layout Feature | Covered | Comments |
| :--- | :--- | :---: | :--- |
| **Project Instructions** | HR Registration & Login | Yes | Outlined in Sections 4.1, 8.1, and 9.2.1. |
| **Project Instructions** | Dashboard Count Statistics | Yes | Covered in Sections 4.2 and 9.2.2. |
| **Project Instructions** | Designations from database | Yes | Covered in Sections 4.5 and 5.1. |
| **Project Instructions** | Projects CRUD | Yes | Covered in Sections 4.6 and 5.4. |
| **Project Instructions** | Technology combination of Coding & Tools | Yes | Covered in Sections 4.6 and 14.4. |
| **Project Instructions** | Employee to Project Mapping | Yes | Covered in Sections 4.8 and 5.6. |
| **Project Instructions** | Soft Delete Only (No Hard Delete) | Yes | Addressed in Sections 5.0 and 15.9. |
| **Project Instructions** | Date Timeline order descending | Yes | Enforced in Sections 1.6 and 14.4. |
| **Project Instructions** | Word & PDF Format Exports | Yes | Outlined in Sections 14.5 and 14.6. |
| **Project Instructions** | No watermark in the background | Yes | Enforced in Section 1.6. |
| **SAMPLE - Resume.pdf** | Header structure and fonts | Yes | Covered in Section 14.1. |
| **SAMPLE - Resume.pdf** | Professional Summary Bullets | Yes | Covered in Section 14.2. |
| **SAMPLE - Resume.pdf** | Skill lines for Coding and Tools | Yes | Covered in Section 14.3. |
| **SAMPLE - Resume.pdf** | Project Cards: Technology, Description, Role | Yes | Covered in Section 14.4. |
