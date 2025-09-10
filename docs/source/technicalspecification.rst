Technical Specifications
========================

Technologies
---------------

- **Frameworks and Libraries**: Django, pytest, flake8, Sentry
- **Programming Language**: Python 3.x
- **Other Tools**: Docker, Git, Render (deployment)

Database & Models
---------------------

The project uses **SQLite** in development and can be configured with other databases in production.

Main models:

- **Address**

  - Fields:
      - number,
      - street,
      - city,
      - state,
      - zip_code,
      - country_iso_code
  - Represents a physical address.

- **Letting**
   - Fields:
      - title,
      - address (ForeignKey to Address)
   - Represents a rental property.

- **Profile**
   - Fields:
      - user (OneToOneField to Django User),
      - favorite_city
   - Extends the built-in Django user model with additional attributes.

**Relationships**:

- Each `Letting` is linked to one `Address`.
- Each `Profile` is linked to one Django `User`.

APIs & Interfaces
--------------------

The project exposes a simple set of **views and URL patterns**.

- **oc_lettings_site**
    - `/` → Home page (index view)

- **lettings**
    - `/lettings/` → Lettings index
    - `/lettings/<int:letting_id>/` → Letting detail

- **profiles**
    - `/profiles/` → Profiles index
    - `/profiles/<str:username>/` → Profile detail

**Namespaces**:

- `lettings` and `profiles` apps are namespaced to ensure URL clarity and modularity.
