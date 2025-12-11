 <div id="top" align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

</div>

<br />
<h3 align="center"> 🔥 CollaboKit 🔥 </h3>

  <p align="center">

    Your all in one collaboration and asset management tool!

  </p>
    <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/SharleneNdinda/collabo-kit/issues">Report Bug</a>
    ·
    <a href="https://github.com/SharleneNdinda/collabo-kit/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## 🚀 About The Project

CollaboKit is a robust, scalable service. It is meant to deliver the following:

    ✅ Be able to create personal accounts and teams for collaboration.

### Built With

[![Django][Django]][Django-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🚀 Getting Started

1. Clone this repository and setup virtual environment. Install all project requirements before proceeding.

```sh
  $ pip install -r requirements/base.txt
```

2. Setup your local `Postgres` database, update database configs and run migrations.

```sh
  $ python manage.py migrate
```

3. Run development server.

```sh
  $ python manage.py runserver
```

## 🚀 Usage

### 🔥 API Endpoints

| Endpoint | URL                 | Description               |
| -------- | ------------------- | ------------------------- |
| Login    | /api/auth/login/    | Sign in a user            |
| Register | /api/auth/register/ | Create a new user account |

### 🔒 Authentication

1. This API uses `Basic Token authentication` to authenticate users. After successful local setup copy the given payload to create a test user via register endpoint.

```json
{
  "username": "test",
  "email": "test@gmail.com",
  "password1": "OEOGu9OfSuwSZ4",
  "password2": "OEOGu9OfSuwSZ4"
}
```

[contributors-shield]: https://img.shields.io/github/contributors/SharleneNdinda/collabo-kit?style=for-the-badge
[contributors-url]: https://github.com/SharleneNdinda/collabo-kit/contributors
[forks-shield]: https://img.shields.io/github/forks/SharleneNdinda/collabo-kit?style=for-the-badge
[forks-url]: https://github.com/SharleneNdinda/collabo-kit/forks
[stars-shield]: https://img.shields.io/github/stars/SharleneNdinda/collabo-kit?style=for-the-badge
[stars-url]: https://github.com/SharleneNdinda/collabo-kit/stargazers
[issues-shield]: https://img.shields.io/github/issues/SharleneNdinda/collabo-kit?style=for-the-badge
[issues-url]: https://github.com/SharleneNdinda/collabo-kit/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: in/sharlene-mutuku-86571518b
[product-screenshot]: images/architecture.png
[x-ray-trace]: images/trace.png
[Django]: https://img.shields.io/badge/Django-35495E?style=for-the-badge&logo=django&logoColor=4FC08D
[Django-url]: https://www.djangoproject.com/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
