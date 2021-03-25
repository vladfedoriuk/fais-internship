The repository for the parameters parsing/extracting scripts. 
- *parser.py* is meant to parse and convert a configuration file into the database tables records
- *extractor.py* is meant to extract the configurations into a single text file

- To use the scripts, you need to get **pyenv**: https://realpython.com/intro-to-pyenv/
- Nextly, create and activate virtual environment:
    
    1. `pyenv install 3.9.1` - install python 3.9.1

    2. `pyenv virtualenv 3.9.1 <environment name>` - create a virtual environment

    3. `pyenv local <environment name>` - activate it

    4. `pip install -r requirements.txt` - install the requirements

- The scripts use SQLAlchemy to communicate with a database. The scripts **require from you** to set some environment variables:
    `export username=<your mysql username>`
    `export password=<your mysql password>`

- To know more about the functionalities of the scripts:
    `python3 scripts/parser.py -h`
    `python3 scripts/extractor.py -h`
