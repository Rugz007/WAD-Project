
# Wikipedia Translator Platform
Platform for helping people make datasets for NLP translation by using Wikipedia summaries from it's API.

## Features

 - Buillt a REST API using Django REST Framework.
 - Swagger implemented for API documentation.
 - Containerized application using Docker.
 - Implement frontend using ReactJS with ChakraUI.
 - Create Projects and import summary from WikipediaAPI.
 - Add Languages on the fly which are supported by React transliterate.
 - Update and save sentence translations.
 - Ability to create multiple projects.
 - Implemented React-Transliterate.

## Built With

- [Django REST Framework](https://www.django-rest-framework.org)

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/)

- [docker-compose](https://docs.docker.com/compose/install/)

## Installation and Usage

1. Clone this repository and change directory.

```bash
git clone https://github.com/Rugz007/WikipediaPlatform.git
cd WikipediaPlatform
```
2. Run the following command to **build** all the containers
```bash
docker-compose build
```
4. Run the following command to **run** all the containers

```bash
docker-compose up
```

5. Visit django-admin at ```localhost:8000/admin/```
6. Visit frontend at ```localhost:3000```
7. Visit API documentation at ```localhost:8000/swagger```

## Known Issues
1. React-transliterate drop-down does not work well in dark mode. Possible solution is by using custom CSS for the drop-down.

## Note
- Admin user with username as *admin* and password as *admin* is created.
