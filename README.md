The repository for the parameters parsing/extracting scripts and webgui. 
## Scripts

*Note that the scripts are no longer supported. Use web gui instead.*

- *parser.py* is meant to parse and convert a configuration file into the database tables records
- *extractor.py* is meant to extract the configurations into a single text file

- To use the scripts, you need to get **pyenv** installed on your local machine: https://realpython.com/intro-to-pyenv/
- When done, create and activate virtual environment:
    
    1. `pyenv install 3.9.1` - install python 3.9.1

    2. `pyenv virtualenv 3.9.1 <environment name>` - create a virtual environment

    3. `pyenv local <environment name>` - activate it

    4. `pip install -r requirements.txt` - install the requirements

- The scripts use SQLAlchemy to communicate with a database. They **require from you** to set some environment variables:
    `export username=<your mysql username>`
    `export password=<your mysql password>`

- To know more about the functionalities of the scripts:
    `python3 scripts/parser.py -h`
    `python3 scripts/extractor.py -h`
    
- The output of the preceding commands should look as follows:
    ```
    python scripts/parser.py -h
    usage: parser.py [-h] [-rf RUNFROM] [-rt RUNTO] [-ff FILEFROM] [-ft FILETO]
                 [-vf VALIDFROM] [-vt VALIDTO] [--remarks REMARKS]
                 conf version

    positional arguments:
    conf                  The name of the configuration file
    version               The version of the configuration

    optional arguments:
    -h, --help            show this help message and exit
    -rf RUNFROM, --runfrom RUNFROM
                        The run from which the configuration is valid
    -rt RUNTO, --runto RUNTO
                        The run up to which the configuration is valid
    -ff FILEFROM, --filefrom FILEFROM
                        The run file from which the configuration is valid
    -ft FILETO, --fileto FILETO
                        The run file up to which the configuration is valid
    -vf VALIDFROM, --validfrom VALIDFROM
                        The datetime from which the configuration is valid
                        Accepted patterns:
                        ['[yyyy]-[mm]-[dd]T[HH]:[MM]:[+-][HHMM]',
                        '[yyyy]-[mm]-[dd]', '[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS][+-][HHMM]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]']
    -vt VALIDTO, --validto VALIDTO
                        The datetime up to which the configuration is valid
                        Accepted patterns:
                        ['[yyyy]-[mm]-[dd]T[HH]:[MM]:[+-][HHMM]',
                        '[yyyy]-[mm]-[dd]', '[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS][+-][HHMM]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]']
    --remarks REMARKS, -r REMARKS
                        The optional remarks about the configuration version
    ```
    ```
    python scripts/extractor.py -h
    usage: extractor.py [-h] [--validfrom VALIDFROM] [--validto VALIDTO]
                    [-v VERSION] [-n NAME] [-r RUN] [-f FILE]

    optional arguments:
    -h, --help            show this help message and exit
    --validfrom VALIDFROM, -vf VALIDFROM
                        The date the configuration is valid from
                        ['[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS]',
                        '[yyyy]-[mm]-[dd]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]:[+-][HHMM]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS][+-][HHMM]']
    --validto VALIDTO, -vt VALIDTO
                        The date the configuration is valid to
                        ['[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS]',
                        '[yyyy]-[mm]-[dd]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]:[+-][HHMM]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]',
                        '[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS][+-][HHMM]']
    -v VERSION, --version VERSION
                        The version of the configurations
    -n NAME, --name NAME  The name of the output file
    -r RUN, --run RUN     The run id to extract datetimes from
    -f FILE, --file FILE  The run file name to extract datetimes from
    ```
## WEB GUI
- Web interface basically consists of  services: 
    - an administration page available via accessing `/admin` url
    - a page for retrieving the arguments from the database: `/interact/retrieve`
    - a page for adding the configurations to the database: `/interact/add`
    - a page for viewing the existing files in the database: `/interact/files`
    - a page for adding and viewing the releases present in the database: `/interact/release`
    - a page to log in: `/interact/login`
- Those are corresponding screenshots of the pages mentioned above:
    ![admin](https://user-images.githubusercontent.com/51965488/117056354-e5c12380-ad24-11eb-8525-6d1c5d8fc613.png)
    ![retrieve](https://user-images.githubusercontent.com/51965488/117056456-fe313e00-ad24-11eb-8652-3db6a51d8517.png)
    ![add](https://user-images.githubusercontent.com/51965488/117059264-49008500-ad28-11eb-8227-d529f2a52d9d.png)
    ![files](https://user-images.githubusercontent.com/51965488/117056499-08533c80-ad25-11eb-950a-a6d636be291d.png)
    ![release](https://user-images.githubusercontent.com/51965488/117056515-0ee1b400-ad25-11eb-8631-17ff97c91bf8.png)
    ![login](https://user-images.githubusercontent.com/51965488/117058731-a6480680-ad27-11eb-87ac-ba4e04cf9076.png)
    
- The administration service allows a user to perform direct CRUD operations on the database. It provides a wide range of functionalities, such as searching the database concerning provided parameters, as well as editing, deleting, or creating the records in the particular tables. What is more, the administrator is granted to create new users. 

### Retrieve the configurations
- "Retrieve the configurations" page is a form that makes it possible to extract the configurations from all the tables in the database for given parameters. The parameters here are similar to those used in the `extractor.py` script. 
- Here are the meanings of the parameters used in the form:
- Parameter     |                 Meaning
  ------------- | ------------------------------------------
  date from     | The date the configuration is valid from. 
  time from     | The time the configuration is valid from. **Note: If the "time from" is provided, the "date from" must be provided as well.**
  date to       | The date the configuration is valid to. 
  time to       | The time the configuration is valid to. **Note: If the "time to" is provided, the "date to" must be provided as well.**
  run id        | The run id to extract valididy dates from. 
  run file name | The name of a run file to extract valididy dates from. **Note: Either run id or run file name must be provided if validity dates are omitted, otherwise form will be invalid.**
  version       | The version of the configuration. **Note: if not provided, all the configurations that satisfy the parameters will be returned.**
  - **Note: If any of the validity dates are specified, then another one must be given too.**
  - If the form is filled correctly, the ouput will look like the one in the following screenshot:
        ![output](https://user-images.githubusercontent.com/51965488/114308052-2d200f80-9aeb-11eb-9fa4-945a07d3a32f.png)
  - The extracted configurations are written down in form of a table with columns (*VALID_FROM, VALID_TO, VERSION, REMARKS*), where *VALID_FROM* is a date and a time a configuration is valid from, *VALID_TO* is a date and a time a configuration is valid to, *VERSION* is a version of a configuration and *REMARKS* are the comments optionally provided by the one who added a configuration version to the database.
  - The rows with the details of the configuration versions also comprise a button that allows the user to download the desired version of the configuration.
  - If the version a user is looking for does not exist, or there are no configurations matched to the parameters a user has provided, a corresponding alert will be displayed. 
![alert](https://user-images.githubusercontent.com/51965488/114308542-06fb6f00-9aed-11eb-940c-4345b07f55d4.png)
- **Note: If the "time from" is not provided, it will be set to 00:00**
- **Note: If the "time to" is not provided, it will be set to 23:59**
### Add a Configuration 
- "Add a Configuration" page is a form that makes it possible to add the configurations to the database. The parameters here are similar to those used in the `parser.py` script. 
- Here are the meanings of the parameters used in the form:
- Parameter     |                 Meaning
  ------------- | ------------------------------------------
  date from     | The date the configuration is valid from. 
  time from     | The time the configuration is valid from. **Note: If the "time from" is provided, the "date from" must be provided as well.**
  date to       | The date the configuration is valid to. 
  time to       | The time the configuration is valid to. **Note: If the "time to" is provided, the "date to" must be provided as well.**
  run-from id   | The id of a run from which the configuration is valid. 
  run-to id     | The id of a run up to which the configuration is valid. 
  run-from file name | The name of a run file from which the configuration is valid. 
  run-to file name   | The name of a run file up to which the configuration is valid. 
  version            | The version of the configuration. 
  release            | The release the configuration will be assigned to. This is a selection input field, where the options are the releases present in the database.
  configuration file | A file containing the configuration.  
  remarks | The optional remarks about the configuration.
  
  - **Note: If any of the validity dates is specified, then another one must be given too.**
  - **Note: Either run id's or run file names must be provided if validity dates are omitted, otherwise form will be invalid.**
  - **Note: If any of the run-id\'s are specified, another one must be provided too.**
  - **Note: If any of the run filenames are specified, another one must be provided too.**
  - **Note: If the "time from" is not provided, it will be set to 00:00**
  - **Note: If the "time to" is not provided, it will be set to 23:59**
  - If the form is filled correctly and the configuration has sucessfuly been added to the database, a success alert will get displayed:
       ![success-alert](https://user-images.githubusercontent.com/51965488/114310302-154c8980-9af3-11eb-8415-33216a324b41.png)
  - Otherwise the corresponding error messages will pop up above the form.
### Add a Release
- "Add a Release" page is a form that allows a user to add a release to the database as well as review the existing ones.
- Here are the meanings of the parameters used in the form:
- Parameter     |                 Meaning
  ------------- | ------------------------------------------
  name          | The name of a releae. 
  comment       | The optional comment about a release. 
- If the form is filled correctly and the release has sucessfuly been added to the database, a success alert will get displayed.
- Otherwise the corresponding error messages will pop up above the form.
### Set up
- First of all, follow the instruction to set up an environment for the `parser.py` and `extractor.py` scripts
- To set up a webgui service you need to follow the instructions:
    - Set up the database configurations. By default, the configurations look like this:
         ```
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': os.environ.get('MYSQL_DATABASE', 'praktyki'),
                    'USER': os.environ.get('MYSQL_USER', 'praktyki'),
                    'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'pass4praktyki'),
                    'HOST': os.environ.get('MYSQL_HOST', '127.0.0.1'),
                    'PORT': os.environ.get('MYSQL_PORT', 3306)
                }
            }
          ```
    They can be found in the `settings.py` file in the webgui directory. One might need to change the 'NAME', 'HOST' and 'PORT' parameters to those relevant to the one's database configurations. The *USER* and *PASSWORD* variables must be provided beforehand as the environmental variables: `export MYSQL_USER=<your mysql username> && export MYSQL_PASSWORD=<your mysql password>`
   - perform `python manage.py migrate`
   - create a superuser in order to use the admin pannel: ` python manage.py createsuperuser` provide the admin username and the password (e.g admin / pass4admin)
   - to run the server in development just perform the command: `python manage.py runserver`
   - to run the server in production, in the `settings.py` change the `DEBUG` variable to `False` and then perform the command as above.
## Set up with docker-compose:
   - **Note: If you decide to set up the projects with docker and docker-compose, disregard the preceding instructions. Do not change any settings/configurations and do not perform any additional commands apart from those mentioned below!**
   - Alternatively, one can easily have the entire project up and running using docker and docker-compose. If you don't have this software installed on your local machine, you will need to get it installed. (An example of installation on ubuntu: https://phoenixnap.com/kb/install-docker-compose-on-ubuntu-20-04 ). Then the whole process of configuring and running the project will end up to be a single command: `docker-compose up` ( the preceding command should be executed within the directory which contains the `docker-compose.yml` file. )
   - In order to acces the terminal of the desired container, execute the following commands:
        - `docker container ps` - obtain the table of running containers
        - find the id of the container you look for and execute: `docker exec -it <container_id> /bin/bash`
   - Try to log in as admin (username: admin, password: pass4admin). If you were informed that there is no such user, open a terminal of `web_webui` container and create a superuser:
        - `docker exec -it <webgui container_id> /bin/bash`   
        - `python manage.py createsuperuser`
### Remarks:
- **It is not possible to have two runs in the `files` table with the same `run_id`,`start_time` and `stop_time`**.
- **It is not possible to have two configurations with the same `valid_from` and `version`**.
# CPP REST Client
- In the folder `rest_client_cpp` there is a source file `test.cpp` containing two functions: 
```
void getRunContainer(long runid, unsigned long version);
std::map<std::string, Parameter> getRunContainers(long min_runid, long max_runid);
```
- The first function accepts two parameters: 
    - `runid` - the id of the run to extract the valididty dates from
    - `version` - a version of the desired parameters.
    - It makes a request to the API. Currently, all it does is writing the parameters to the standart output stream.
- The second function accepts two parameters:
    - `min_runid` - the id of the run to extract the date the parameters are valid from
    - `max_runid` - the id of the run to extract the date the parameters are valid to.
    - This function makes a request to the API and returns a mapping from the name of the module to the structure containing the information about the parameters. It has been designed to return the parameters with the highest version. 
