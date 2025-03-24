# Django Movies API

Django Movies API is a backend application built with Django and Django REST Framework (DRF) to manage movies, reviews, and user authentication. It includes features like OAuth2 authentication with Google, JWT-based authentication, and integration with third-party libraries like Djoser and CKEditor.

---

## **Features**

- **Movies Management**: CRUD operations for movies and reviews.
- **Authentication**:
  - OAuth2 authentication with Google.
  - JWT-based authentication.
  - Token-based authentication.
- **Pagination**: Limit-offset pagination for API responses.
- **Filtering**: Support for filtering using Django Filters.
- **Rich Text Editor**: CKEditor integration for managing rich text content.
- **Email Support**: SMTP configuration for sending emails (e.g., password reset, activation).
- **CORS Support**: Configured for cross-origin requests.
- **Swagger Documentation**: API documentation using DRF-YASG.

---

## **Technologies Used**

- **Backend**: Django 5.1, Django REST Framework
- **Authentication**: OAuth2, JWT, Djoser
- **Database**: PostgreSQL
- **Rich Text Editor**: CKEditor
- **API Documentation**: DRF-YASG
- **Environment Variables**: Python `dotenv`

---

## **API Endpoints**

### **Authentication**
- `POST /auth/login/` - Login with credentials.
- `POST /auth/register/` - Register a new user.
- `POST /auth/logout/` - Logout the current user.
- `POST /auth/token/refresh/` - Refresh JWT token.
- `POST /auth/password/reset/` - Request a password reset email.
- `POST /auth/password/reset/confirm/` - Confirm password reset with token.
- `POST /auth/activate/` - Activate a user account with token.
- `POST /auth/google/` - Login or register using Google OAuth2.

### **Movies**
- `GET /api/movies/` - Retrieve a list of all movies.
- `POST /api/movies/` - Create a new movie (admin only).
- `GET /api/movies/<id>/` - Retrieve details of a specific movie.
- `PUT /api/movies/<id>/` - Update a specific movie (admin only).
- `DELETE /api/movies/<id>/` - Delete a specific movie (admin only).

### **Reviews**
- `GET /api/reviews/` - Retrieve a list of all reviews.
- `POST /api/reviews/` - Create a new review for a movie.
- `GET /api/reviews/<id>/` - Retrieve details of a specific review.
- `PUT /api/reviews/<id>/` - Update a specific review (author only).
- `DELETE /api/reviews/<id>/` - Delete a specific review (author or admin).

### **Users**
- `GET /api/users/` - Retrieve a list of all users (admin only).
- `GET /api/users/<id>/` - Retrieve details of a specific user (admin only).
- `PUT /api/users/<id>/` - Update user details (admin or user themselves).
- `DELETE /api/users/<id>/` - Delete a user (admin only).

### **Other**
- `GET /api/docs/` - Swagger API documentation.
- `GET /api/schema/` - OpenAPI schema for the API.
