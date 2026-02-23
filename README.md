# Patients_Registration_System

## Please check the functionalities of this code via https://youtu.be/yP_tJxVfS2c

## Description:
This is my final Python project for the Advanced Python Certification course in SLIPD. The APL Hospital Management System is a desktop application built using Python, Tkinter, and MySQL used for the backend. It allows patients to register and log in to the hospital system. 

## Features

### Patient Registration

Enter name, email, date of birth, phone number, and password
Password confirmation ensures data accuracy

### Patient Login

Authenticate using name and password
Error messages for invalid credentials

### Password Security

Password hashing with hashlib for secure storage

### Tech Stack

Python 3.x
Tkinter – GUI development
MySQL – Database
PyWinStyles – Dark theme support
hashlib - Password hashing to enhance security

## Database Set-up

### Create Database

CREATE DATABASE hospital_management_syste;

### Create table

CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    dob DATE NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    password VARCHAR(64) NOT NULL);

## Installing required package

pip install tkinter
pip install mysql-connector-python
pip install pywinstyles

## User Guideline

### Registration

Username: Enter your full name

Email address: Provide a valid email

Date of Birth: Format YYYY/MM/DD (e.g., 1990/01/15)

Contact number: Enter your phone number

Password: Create a secure password

Re-enter password: Confirm your password

### Login

Enter your registered username

Enter your password

Click "Login" to access the system

### UI Features

Clean teal color scheme (#009688)

Dark theme support for Windows

Responsive frame switching between registration and login

Centered form layout

Professional font styling (Times New Roman)

## Author

G G Nishan Harsha Maduranga

Student - BCAS Campus


## Screenshots of the project

### Registration Page

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/9d0a93dc-c342-4e7f-9fcd-94421e7b289b" />

### Error Message

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/d5df0771-2795-4c00-8cb7-867dea222f64" />

### Login Success page

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/21186f0b-e29f-4289-8cdd-0439b6ef0ede" />

### Login Page

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/7ba722a8-d069-4555-9830-01d5731b09fd" />

### Login Error

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/96e986b5-6fc8-42e0-aae5-4972a7557502" />

### Login Success

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/ec829460-be22-4f5d-b94b-df4c5a21b572" />
