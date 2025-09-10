Installation
============

Follow these steps to install and run **OC_lettings** locally.

Prerequisites
-------------

- Python 3.10 or higher
- Git
- A virtual environment (venv recommended)

Steps
-----

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/Mikael2983/P13_Python-OC-Lettings-FR.git
      cd P13_Python-OC-Lettings-FR

2. Create and activate a virtual environment:

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # Linux / macOS
      venv\Scripts\activate     # Windows

3. Install dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

4. Run migrations:

   .. code-block:: bash

      python manage.py migrate

5. Start the local server:

   .. code-block:: bash

      python manage.py runserver

6. Access the application at:

   http://127.0.0.1:8000/