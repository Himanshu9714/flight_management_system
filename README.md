# Flight Booking System

- A Simple Django-based web application for managing flight bookings.
- This application allows users to search for book tickets, and view their bookings.
- Admins can manage flights and view all bookings.
- The app is containerized using Docker for easy deployment and setup.

## Getting Started

These instructions will help you set up and run the project on your local machine using Docker.

### Prerequisites

- Docker
- Docker Compose

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Himanshu9714/flight_management_system.git
    cd flight_management_system
    ```

2. **Create and configure the `.env` file:**

    Create a `.env` file in the root directory of the project and add the following content:

    ```env
    DB_NAME='your-db-name'
    DB_USER='your-db-user'
    DB_PASSWORD='your-db-password'
    DB_HOST='your-db-host'
    DB_PORT='your-db-port'
    ```

    Replace `your_db_name`, `your_db_user`, `your_db_password`, `admin@example.com`, and `your_password` with your actual database credentials and superuser details.

    For default values, set them to following
    ```env
    SECRET_KEY='23h65398gbrihf4r8fh4bfuy8r39473gr4y4hf94ug904'
    DEBUG=1
    DB_NAME=postgres
    DB_USER=postgres
    DB_PASSWORD=postgres
    DB_HOST=db
    DB_PORT=5432
    ```

3. **Build and run the Docker containers:**

    ```sh
    docker-compose up --build -d
    ```

    This command will build the Docker images, apply migrations, create a superuser (if specified), and start the application.

4. **Access the application:**

    - Open your web browser and go to `http://localhost:8000` to access the application.
    - User credentials:
        - Admin: sa@gmail.com, Password: Admin@123
        - Normal User: ram@gmail.com, Password: Hanuman@123

### Useful Docker Commands

- **Stop the application:**

    ```sh
    docker-compose down
    ```

- **Rebuild the application:**

    ```sh
    docker-compose up --build
    ```

- **View logs:**

    ```sh
    docker-compose logs -f
    ```

### Running Commands in the Docker Container

If you need to run Django management commands, you can do so within the running web container. For example:

- **Running migrations:**

    ```sh
    docker-compose exec web python manage.py migrate
    ```

- **Creating a new superuser:**

    ```sh
    docker-compose exec web python manage.py createsuperuser
    ```

### File Structure

