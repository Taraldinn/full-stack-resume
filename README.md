# Personal Portfolio

A full-stack personal portfolio application built with Django REST Framework backend and Nuxt.js frontend.

## Project Structure

```
personal-portfolio/
├── backend/          # Django REST API
├── frontend/         # Nuxt.js application
└── README.md        # This file
```

## Features

### Backend (Django REST Framework)
- User authentication and profiles
- Comprehensive portfolio data models:
  - Personal information and bio
  - Education history
  - Work experience
  - Skills and certifications
  - Projects showcase
  - Awards and achievements
  - Testimonials
  - Publications
  - Social media links
  - Extracurricular activities
- RESTful API endpoints
- Admin interface for content management

### Frontend (Nuxt.js)
- Modern Vue.js-based frontend
- Server-side rendering (SSR)
- Responsive design with Nuxt UI
- Content management integration
- Image optimization
- SEO-friendly

## Quick Start

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## API Endpoints

- `GET /api/users/` - Get user profiles
- `POST /api/users/` - Create user profile
- `PUT /api/users/{id}/` - Update user profile
- `DELETE /api/users/{id}/` - Delete user profile

## Technologies Used

### Backend
- Django 5.2+
- Django REST Framework
- SQLite (development)
- Python 3.8+

### Frontend
- Nuxt.js 4.0+
- Vue.js 3.5+
- TypeScript
- Nuxt UI
- Nuxt Content
- Nuxt Image

## Development

### Backend Development
The Django backend provides a comprehensive API for managing portfolio data. Models include:
- Profile: Basic user information
- Education: Academic background
- WorkExperience: Professional history
- Skills: Technical and soft skills
- Projects: Portfolio projects
- Awards: Achievements and recognition
- Testimonials: Client/colleague feedback
- Publications: Articles and papers
- And more...

### Frontend Development
The Nuxt.js frontend is configured with:
- TypeScript support
- ESLint for code quality
- Nuxt UI for components
- Content management
- Image optimization
- Testing utilities

## Deployment

### Backend Deployment
- Configure production database (PostgreSQL recommended)
- Set up environment variables
- Configure static files serving
- Set up CORS for frontend communication

### Frontend Deployment
- Build for production: `npm run build`
- Deploy to Vercel, Netlify, or similar platforms
- Configure API base URL for production

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
