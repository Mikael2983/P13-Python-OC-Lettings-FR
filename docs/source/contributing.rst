Contributing
============

Thank you for your interest in contributing to **OC_lettings** 🎉

Guidelines
----------

1. Fork the repository and create a feature branch:

   .. code-block:: bash

      git checkout -b feature/my-feature

2. Follow PEP8 code style (you can use `flake8` or `black`).

3. Add tests for any new functionality:

   .. code-block:: bash

      pytest

4. Update the documentation if needed.

5. Push your changes and open a Pull Request on GitHub.

Continuous Integration (CI)
---------------------------

The project uses **GitHub Actions** to automate tests and validate contributions.

- On every **push** or **Pull Request**, the CI executes:
  - Dependency installation
  - Unit tests with `pytest`
  - Code quality checks

Check workflow status in the **Actions** tab on GitHub.

Best Practices
--------------

- Write clear and descriptive commits
- One commit = one feature/fix
- Before submitting a Pull Request, ensure all tests pass:

   .. code-block:: bash

      pytest && flake8

Code of Conduct
---------------

Please maintain respectful and constructive communication in issues,
Pull Requests, and all project interactions.