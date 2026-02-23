# Patients_Registration_System

## Please check the functionalities of this code via https://youtu.be/yP_tJxVfS2c

## Description:
The APL Hospital Management System is a desktop application built using Python, Tkinter, and MySQL used for the backend. It allows patients to register and log in to the hospital system. 

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
