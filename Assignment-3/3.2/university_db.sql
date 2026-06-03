-- ============================================================
--  UNIVERSITY REGISTRAR DATABASE
-- ============================================================
CREATE DATABASE IF NOT EXISTS university_db;
USE university_db;

-- COURSE table
CREATE TABLE IF NOT EXISTS Course (
    course_no   VARCHAR(20)  NOT NULL,
    title       VARCHAR(200) NOT NULL,
    credits     INT          NOT NULL CHECK (credits > 0),
    syllabus    TEXT,
    PRIMARY KEY (course_no)
);

-- PREREQUISITE (recursive / self-referential relationship on Course)
CREATE TABLE IF NOT EXISTS Prerequisite (
    course_no   VARCHAR(20) NOT NULL,
    prereq_no   VARCHAR(20) NOT NULL,
    PRIMARY KEY (course_no, prereq_no),
    CONSTRAINT fk_prereq_course
        FOREIGN KEY (course_no) REFERENCES Course(course_no)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_prereq_prereq
        FOREIGN KEY (prereq_no) REFERENCES Course(course_no)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- INSTRUCTOR table
CREATE TABLE IF NOT EXISTS Instructor (
    instr_id    INT          NOT NULL AUTO_INCREMENT,
    name        VARCHAR(100) NOT NULL,
    department  VARCHAR(100) NOT NULL,
    title       VARCHAR(50),
    PRIMARY KEY (instr_id)
);

-- COURSE_OFFERING weak entity (identified by course_no + year + semester + section_no)
CREATE TABLE IF NOT EXISTS Course_Offering (
    offering_id  INT         NOT NULL AUTO_INCREMENT,
    course_no    VARCHAR(20) NOT NULL,
    year         YEAR        NOT NULL,
    semester     ENUM('Fall','Spring','Summer') NOT NULL,
    section_no   VARCHAR(10) NOT NULL,
    timings      VARCHAR(100),
    classroom    VARCHAR(50),
    PRIMARY KEY (offering_id),
    UNIQUE KEY uq_offering (course_no, year, semester, section_no),
    CONSTRAINT fk_offering_course
        FOREIGN KEY (course_no) REFERENCES Course(course_no)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

-- TEACHES (M:N between Instructor and Course_Offering)
CREATE TABLE IF NOT EXISTS Teaches (
    instr_id    INT NOT NULL,
    offering_id INT NOT NULL,
    PRIMARY KEY (instr_id, offering_id),
    CONSTRAINT fk_teaches_instr
        FOREIGN KEY (instr_id)    REFERENCES Instructor(instr_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_teaches_offering
        FOREIGN KEY (offering_id) REFERENCES Course_Offering(offering_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- STUDENT table
CREATE TABLE IF NOT EXISTS Student (
    student_id  INT          NOT NULL AUTO_INCREMENT,
    name        VARCHAR(100) NOT NULL,
    program     VARCHAR(100) NOT NULL,
    PRIMARY KEY (student_id)
);

-- ENROLLMENT (M:N between Student and Course_Offering, with grade attribute)
CREATE TABLE IF NOT EXISTS Enrollment (
    student_id  INT         NOT NULL,
    offering_id INT         NOT NULL,
    grade       VARCHAR(5)  NULL,          -- NULL until grade is awarded
    PRIMARY KEY (student_id, offering_id),
    CONSTRAINT fk_enroll_student
        FOREIGN KEY (student_id)  REFERENCES Student(student_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_enroll_offering
        FOREIGN KEY (offering_id) REFERENCES Course_Offering(offering_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);