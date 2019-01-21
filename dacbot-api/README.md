# Dacbot API

Application designed to deal with database operations. Receiving HTTP requests and performing these DB operations to compose its response.

-----

## Dependencies 
- Java 8.X 
- Spring Framework 2.1.0
- Gradle 5.0 
- Eclipse (or other compatible IDE)

-----

## Setting project

After navigating to the root folder, prepared project to be imported to Eclipse:
````
./gradlew eclipse
````

-----

## Building project
````
./gradlew clean build
````

#### Note: if you want to run the project with a local database, you should pass the profile parameter in the boot run: ```-Dsprinf.active.profile=local```

-----

## Requests

#### GET /calendar/{id}
- The call is responsible for getting a calendar registry base on a received database ID.
- Example:
    - Request: **GET** ```http://dacbot.sa-east-1.elasticbeanstalk.com/calendar/5```
    - Response:
```json
{
    "id": 5,
    "entity": "ferias_verao",
    "year": 2018,
    "semester": 1,
    "initDate": "2018-01-04",
    "endDate": "2018-01-04",
    "uri": "https://www.dac.unicamp.br/portal/calendario/2018/graduacao",
    "description": "DAC divulga na WEB relatórios de matrículas do período de Férias de Verão - 2018.",
}
```

#### GET /calendar?entity=ferias_verao
- Method responsible for getting a list of calendar registries, searching by its name (entity name).
- Example:
    - Request: **GET** ```http://dacbot.sa-east-1.elasticbeanstalk.com/calendar?entity=ferias_verao```
    - Response:
```json
[
    {
        "id": 2,
        "entity": "ferias_verao",
        "year": 2018,
        "semester": 1,
        "initDate": "2018-01-02",
        "endDate": "2018-01-03",
        "uri": "https://www.dac.unicamp.br/portal/calendario/2018/graduacao",
        "description": "Coordenadorias de Cursos adequam matrículas do período de  Férias de Verão - 2018."
    },
    {
        "id": 5,
        "entity": "ferias_verao",
        "year": 2018,
        "semester": 1,
        "initDate": "2018-01-04",
        "endDate": "2018-01-04",
        "uri": "https://www.dac.unicamp.br/portal/calendario/2018/graduacao",
        "description": "DAC divulga na WEB relatórios de matrículas do período de Férias de Verão - 2018."
    },
    {
        "id": 6,
        "entity": "ferias_verao",
        "year": 2018,
        "semester": 1,
        "initDate": "2018-01-04",
        "endDate": "2018-02-21",
        "uri": "https://www.dac.unicamp.br/portal/calendario/2018/graduacao",
        "description": "Prazo para entrada de Médias e Frequências do período de Férias de Verão - 2018, na WEB."
    },
    {...}
]
```