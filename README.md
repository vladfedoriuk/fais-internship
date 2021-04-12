The repository for the parameters parsing/extracting scripts and webgui. 
## Scripts
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
- Web interface basically consists of three services: an administration page available via accessing `/admin` url, a page for retrieveing the arguments from the database: `/interact/retrieve` and a page for adding the configurations to the database: `/interact/add`.
- Those are corresponding screenshots of the pages mentioned above:
    ![admin](https://user-images.githubusercontent.com/51965488/114301545-02738e00-9ace-11eb-82d5-2840d758df48.png)
    
    ![retrieve](https://user-images.githubusercontent.com/51965488/114301602-42d30c00-9ace-11eb-820a-bcd0974d659b.png)
    
    ![add](https://user-images.githubusercontent.com/51965488/114301655-83328a00-9ace-11eb-9075-c618d4783622.png)

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
  - The extracted configurations are written down in form of a table with columns (*VALID_FROM, VALID_TO, VERSION, REMARKS*), where *VALID_FROM* is a date and a time a configuration is valid from, *VALID_TO* is a date and a time a configuration is valid to, *VERSION* is a version of a configuration and *REMARS* are the comments optionally provided by the one who added a configuration version to the database.
  - The rows with the details of the configuration versions also comprise a button that allows the user to download the desired version of the configuration.
  - If the version a user is looking for does not exist, or there are no configurations matched to the parameters a user has provided, a corresponding alert will be displayed. 
![alert](https://user-images.githubusercontent.com/51965488/114308542-06fb6f00-9aed-11eb-940c-4345b07f55d4.png)

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
  configuration file | A file containing the configuration.  
  remarks | The optional remarks about the configuration.
  
  - **Note: If any of the validity dates are specified, then another one must be given too.**
  - **Note: Either run id's or run file names must be provided if validity dates are omitted, otherwise form will be invalid.**
  - **Note: If any of the run-id\'s are specified, another one must be provided too.**
  - **Note: If any of the run filenames are specified, another one must be provided too.**
  - If the form is filled correctly and the configuration have sucessfuly been added to the database, a sucess alert will get displayed:
       ![success-alert](https://user-images.githubusercontent.com/51965488/114310302-154c8980-9af3-11eb-8415-33216a324b41.png)
  - Otherwise the corresponding error messages will pop up above the form.
### Set up
- First of all, you need to create the database as described in the `praktyki.sql` file.
- Secondly, follow the instruction to set up an environment for the `parser.py` and `extractor.py` script
- To set up a webgui service you need to follow the instrictions:
    - Set the database configurations. By default configuration look like this:
         ```
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'praktyki',
                    'USER': os.environ.get('username'),
                    'PASSWORD': os.environ.get('password'),
                    'HOST': '127.0.0.1',
                    'PORT': 3306
                }
            }
          ```
    They can be found in the `settings.py` file in the webgui derictory. One might need to change the 'NAME', 'HOST' and 'PORT' parameters to the ones corresponding to the one's database configurations. The username and password must be provided beforehand as the environmental variables: `export username=<your mysql username> && export password=<your mysql password>`
   - perform `python manage.py migrate`
   - create a superuser in order to use the admin pannel: ` python manage.py createsuperuser` provide the admin username and the password (e.g admin / pass4admin)
   - to run the server in development just perform the command: `python manage.py runserver`
   - to run the server in production, in the `settings.py` change the `DEBUG` variable to `False` and then perform the command as above.
 
              
