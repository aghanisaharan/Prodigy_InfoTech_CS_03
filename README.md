# Password Complexity Checker

This repository contains my Python program for Task 03 of the Cyber Security Internship at **Prodigy InfoTech**.

The objective of this project is to build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. It is designed to provide feedback to users on the password's strength.

## Features
* **Strength Assessment:** Evaluates passwords strictly based on length, presence of uppercase and lowercase letters, numbers, and special characters.
* **User Feedback:** Provides direct and actionable feedback to users on the password's strength.
* **Advanced Metrics:** Calculates password entropy and estimates potential crack times against various simulated attack vectors.
* **Common Password Detection:** Cross-references inputs against a blacklist of common passwords.
* **Password Generation:** Includes a built-in secure password generator to output strong, customized alternatives.

## Requirements
* Python 3.x
* A text file named `common_passwords.txt` in the same directory (optional, for blacklist feature).
