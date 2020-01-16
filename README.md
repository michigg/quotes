# Die Zitate App
Zitate Zitate Zitate


<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Quotes</h3>

  <p align="center">
    An app to save your quotes!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</p>


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.


### Installation
> ***WARNING!*** Current Installations before version v1.1.0 should follow this migration guide
> Cause: Introduction of quote deletion. All old quotes need now a creator. To migrate the old quotes
> 1. RUN the new image `michigg/quotes:1.1.0`
> 2. SELECT a new default creator (user) for all old quotes. Therefore go to the admin Web interface `Home › Authentication and Authorization › Users` and note the user id from the default user.
> 3. RUN `docker-compose exec <quote-service> sh`
> 4. RUN `python3 manage.py makemigrations`, select enter default value and enter your selected user id.
> 5. RUN `python3 manage.py migrate` and then your finished 

1. COPY the `docker-compose.prod.yml` and `docker.env`
2. CHANGE the docker-compose file and env file to fit your server config
3. Start the container
4. RUN `python3 manage.py makemigrations` and `python3 manage.py migrate`
5. RUN `python3 manage.py creatsuperuser` to generate an initial Admin Account




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/michigg/quotes.svg?style=flat-square
[contributors-url]: https://github.com/michigg/quotes/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/michigg/quotes.svg?style=flat-square
[forks-url]: https://github.com/michigg/quotes/network/members
[stars-shield]: https://img.shields.io/github/stars/michigg/quotes.svg?style=flat-square
[stars-url]: https://github.com/michigg/quotes/stargazers
[issues-shield]: https://img.shields.io/github/issues/michigg/quotes.svg?style=flat-square
[issues-url]: https://github.com/michigg/quotes/issues
[license-shield]: https://img.shields.io/github/license/michigg/quotes.svg?style=flat-square
[license-url]: https://github.com/michigg/lama/blob/master/LICENSE.md
[product-screenshot]: images/screenshot.png
