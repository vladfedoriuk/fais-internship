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
- "Retrieve the configurations" page is a form that makes it possible to extract the configurations from all the tables in the database for given parameters. The parameters here are similar to those used in the scripts. 
- Here are the meanings of the parameters used in the form:
- Parameter     |                 Meaning
  ------------- | ------------------------------------------
  date from     | The date configuration is valid from. 
  time from     | The time configuration is valid from. **Note: If the time from is provided, the date from must be provided as well.**
  date to       | The date configuration is valid to. 
  time to       | The time configuration is valid to. **Note: If the time to is provided, the date to must be provided as well.**
  run id        | The run id to extract valididy dates from. 
  run file name | The name of run file to extract valididy dates from. **Note: Either run id or run file name must be provided if validity dates are omitted, otherwise form will be invalid.**
  version       | The version of the configuration. **Note: if not provided, all the configurations that satisfy the parameters will be returned.**
  - If the form is filled correctly, the ouput will look like the one in the following screenshot:
        ![output](https://user-images.githubusercontent.com/51965488/114308052-2d200f80-9aeb-11eb-9fa4-945a07d3a32f.png)
  - The extracted configurations are written down in form of a table with columns (*VALID_FROM, VALID_TO, VERSION, REMARKS*), where *VALID_FROM* is a date and a time a configuration is valid from, *VALID_TO* is a date and a time a configuration is valid to, *VERSION* is a version of a configuration and REMARS are the comments optionally provided by the one who added a configuration version to the database.
  - The rows with the details of the configuration versions also comprise a button that allows the user to download the desired version of the configuration.
  - If the version a user is looking for does not exist, or there are no configurations matched to the parameters a user has provided, a corresponding alert will be displayed. 
![alert](https://user-images.githubusercontent.com/51965488/114308542-06fb6f00-9aed-11eb-940c-4345b07f55d4.png)

              
