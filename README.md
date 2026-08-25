# Project Design Document

### Document Revision History

| Name | Date | Changes | Version |
| :---- | :---- | :---- | :---- |
| Revision 1 | 2026-3-31 | Initial draft | 0.1 |

# 1. Introduction
This project is meant to help keep track of tasks and projects.


# 2. Software Design

## 2.1 Database Model

**Project:** Stores project information including a title, description, start date, end date, and tasks.

**Task:** Stores task information, including a title, description, due date, completion, progress, and the project it is a part of.

<!-- <kbd>  
      <img src=images/uml_diagram.png  border=2>  
</kbd> -->

## 2.2 Routes

|  | Methods | URL Path | Description |
| :---- | :---- | :---- | :---- |
| 1. | GET | /index | Displays the main page   |
| 2. | GET, POST | /addtask | Displays the main page   |
| 2. | GET, POST | /addproject | Displays the main page   |
| 2. | GET, POST | /viewproject | Displays the main page   |

### 2.3 User Interface Design
