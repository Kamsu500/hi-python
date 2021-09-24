import configparser
config = configparser.ConfigParser()
config['dylane'] ={'species': 'Dog',
                    'breed': 'Labrador Retriever',
                    'age': '6'}

with open('dylane.ini', 'w') as configfile:
    config.write(configfile)