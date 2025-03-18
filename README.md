# Sales_Analyse
# Sales Workflow Optimization Platform

A comprehensive sales workflow platform built with Flask that includes:
- Lead management system
- AI-powered analytics
- Custom reporting
- Email integration
- User authentication

## Core Components

### Main Application Files
- `app.py`: Main Flask application setup and configuration
- `models.py`: Database models for Users, Leads, Reports, and Activities
- `routes.py`: Application routes and API endpoints
- `main.py`: Application entry point

### Utility Modules
- `ai_utils.py`: AI integration for lead scoring and analytics
- `email_utils.py`: Email templating and sending functionality

### Frontend
- Templates in `/templates`
- Static assets in `/static`
- Custom styling in `/static/css`
- JavaScript utilities in `/static/js`

## Setup Instructions

1. Environment Variables Required:
   - `DATABASE_URL`: PostgreSQL database URL
   - `SESSION_SECRET`: Secret key for session management
   - `OPENAI_API_KEY`: For AI features
   - Mail server configuration (in development mode, emails are logged instead of sent)

2. Database Setup:
   The application will automatically create necessary tables on first run.

3. Running the Application:
   ```bash
   python main.py
   ```
   The application will be available at `http://localhost:5000`

## Features

1. User Authentication
   - Registration and login system
   - Secure password handling

2. Lead Management
   - Create and track leads
   - Automated lead scoring
   - Status updates
   - Email notifications

3. Analytics and Reporting
   - Custom report creation
   - Multiple metrics tracking
   - Data visualization
   - CSV export functionality

4. AI Integration
   - Lead scoring
   - Conversion prediction
   - Sales insights
   - Revenue forecasting

## Development Guidelines

- Flask application structure follows best practices
- Bootstrap for responsive design
- Chart.js for data visualization
- AI-powered features using OpenAI's GPT-4o model
