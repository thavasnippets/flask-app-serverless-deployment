## Flask application
This sample application built using 
- Flask-RESTPlus
- Flask-Marshmallow
- Flask-SQLAlchemy

## Setup
### Install Virtual Environment 
```
pip install virtualenv
```

### Configure and Activate the virtualenv
```
C:\...\Falsk-api-aws-lambda\SampleApp>virtualenv venv

C:\...\Github\Falsk-api-aws-lambda\SampleApp>venv\Scripts\activate.bat
```

### Install the Dependencies
```
pip install -r requirements.txt 
```

### Setup and Create Mysql Database and Table

```sql
CREATE DATABASE `flask_app` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE flask_app;

CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `position` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `employee_id_UNIQUE` (`employee_id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

```
Update database connection string in app.py

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<<USERNAME>>:<<PASSWORD>>@<<HOST_NAME>>/<<DATABASENAME>>'
```


### Run the Application

```
python app.py
```

This will start the application on port 5000

### Done!
## Happy Coding!
