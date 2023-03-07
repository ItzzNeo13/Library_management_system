-- Member database:

-- Creating Table:
CREATE TABLE Member(
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    member_age INT NOT NULL,
    email_id VARCHAR(255) NOT NULL UNIQUE,
    member_since DATE NOT NULL
);

-- Inserting member data:
INSERT INTO Member (first_name, last_name, member_age, email_id, member_since)

-- Staff Databse:
CREATE TABLE library_staff(
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(255) NOT NULL,
    emp_email VARCHAR(255) NOT NULL UNIQUE,
    emp_salary INT NOT NULL,
    emp_gender VARCHAR(255),
    emp_age INT NOT NULL,
    emp_status VARCHAR(255)
);

-- Inserting staff data:
INSERT INTO library_staff(emp_name,emp_email,emp_salary,emp_gender,emp_age,emp_status)

-- Book_log Database:
CREATE TABLE Book_log(
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    book_title VARCHAR(255) NOT NULL,
    book_author CHAR(255) NOT NULL,
    book_genre CHAR(255) NOT NULL,
    book_condition CHAR(255) NOT NULL
);

-- Inserting book data
INSERT INTO Book_log(book_title, book_author, book_genre,book_condition);

-- Showing Data:
SELECT * FROM member