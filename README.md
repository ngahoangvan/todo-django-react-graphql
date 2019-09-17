# Django + ReactJS + GraphQL

## Prerequisites

- Python3.6
- NPM 6.9.0
- Node 10.16.2

## Start Project

### Backend: Django Server

```bash
cd backend
python3 -m venv venv                    \\ In ubuntu
source venv/bin/activate                \\ In ubuntu
pip3 install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend: ReactJS

```bash
cd frontend
npm install
npm start
```

## Start Project with Docker

```bash
git clone https://github.com/vanngaCNTT/todo-django-react-graphql.git
cd todo-django-react-graphql
docker-compose build
docker-compose up
```