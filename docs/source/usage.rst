Usage
=====

The **OC_lettings** application offers the following features:

Main Features
-------------

- **Home page**: site overview
- **Profiles**: user profile management
- **Listings**: rental property management

Useful Commands
---------------

1. Run unit tests:

   .. code-block:: bash

      pytest

2. Build documentation:

   .. code-block:: bash

      sphinx-build -b html docs/ docs/_build/html

3. Start the local server:

   .. code-block:: bash

      python manage.py runserver

Deployment
----------

Two deployment options are available:

1. **Local deployment** (Render or classic server)

    For local development, environment variables are **not strictly required**.
    The application will run with default values if no `.env` file is present:

    - `DEBUG` → defaults to `False`
    - `SECRET_KEY` → automatically generated (different on each run, not stable, not production-ready)
    - `SENTRY_DSN_OC_LETTINGS` → empty (Sentry logging disabled in local development)

    This means that a developer can run the project without setting up a `.env` file.

    However, if you prefer a more stable development environment, you can simply **rename** the provided `.env.example` file to `.env`:

    .. code-block:: bash

        mv .env.example .env

    Notes:
    - This `.env` setup is **only for local use**.
    - It will not connect to Sentry (logs will not be sent).
    - The `SECRET_KEY` defined in `.env.example` is **not the production secret key**.


2. **DockerHub deployment**
   A ready-to-use Docker image is available:
   `mikael2983/python_lettings_fr:latest`

   Run the container locally:

   .. code-block:: bash

      docker pull mikael2983/python_lettings_fr:latest
      docker run -p 8000:8000 mikael2983/python_lettings_fr

   Access the application at:
   http://127.0.0.1:8000/