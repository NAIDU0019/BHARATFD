# BharatFD - FAQ Management

A Django REST API for managing multilingual FAQs.

## Features
- Supports WYSIWYG editor (`django-ckeditor`)
- Multi-language translation using `googletrans`
- Caching with Redis for better performance
- REST API with filtering, pagination, and language selection

## Installation

```bash
git clone https://github.com/NAIDU0019/BHARATFD.git
cd BHARATFD
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
