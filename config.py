import configparser

config = configparser.ConfigParser()
config["General"] = {
    "title": "Hangman",
    "version": "1.0",
    "debug" : "True"
}
