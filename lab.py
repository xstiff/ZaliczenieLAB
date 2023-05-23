import sys
import json
import yaml
import xmltodict
import subprocess

required_packages = [
    "xmltodict", 
]

for package in required_packages:
    try:
        subprocess.check_call(['pip', 'install', package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        input(f'Error while installing package: {package}.')
        exit()
    print('All packages installed successfully.')

allowed_extensions = [
    "json",
    "yaml",
    "yml",
    "xml",
]

def checkArgs():
    arguments = sys.argv[1:]
    if arguments:
        if len(arguments) != 2:
            input("\t\t[!!!] Wrong arguments. Enter to exit")
            exit()
        
        elif arguments[0] == arguments[1]:
            input("\t\t[!!!] Wrong arguments. Enter to exit")
            exit()

        else:
            inputFile = arguments[0].split('.')
            output = arguments[1].split('.')

            input_ext = inputFile[-1].lower()
            output_ext = output[-1].lower()

            input_filename = inputFile[0]
            output_filname = output[0]

            if (output_ext in allowed_extensions) and (input_ext in allowed_extensions):
                print("\tExpected result:\n\t", input_ext, " --> ", output_ext)
                return input_filename + "." + input_ext, output_filname + "." +  output_ext
            else:
                input("\t\t[!!!] Wrong arguments. Enter to exit")
                exit()
    else: 
        input("Wrong number of arguments. Enter to exit")
        exit()


# Imports

def importJson(filename):
    print("\n\t\tReading <-- ", filename)
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except Exception as e:
        input("\t\t[!!!] Error while reading JSON file. Enter to exit")
        exit()

def importYml(filename):
    print("\n\t\tReading <-- ", filename)
    try:
        with open(filename, "r") as file:
            data = yaml.safe_load(file)
            return data
    except Exception as e:
        input("\t\t[!!!] Error while reading YML/YAML file. Enter to exit")
        exit()
        
def importXml(filename):
    print("\n\t\tReading <-- ", filename)
    try:
        with open(filename, "r") as file:
            data = xmltodict.parse(file.read())
            return data
    except Exception as e:
        input("\t\t[!!!] Error while reading XML file. Enter to exit")
        exit()


# Exports

def exportJsonAsYml(data, filename):
    print("\n\t\tExporting --> ", filename)
    
    try:
        
        with open(filename, "w") as file:
            #json to yml
            yaml.dump(data, file, indent=4)

    except Exception as e:
        print("\t\tGot error: ", e)
        input("\t\t[!!!] Error while exporting JSON to YML/YAML file. Enter to exit")
        exit()

def exportJsonAsXml(data, filename):
    print("\n\t\tExporting --> ", filename)
    try:
        with open(filename, "w") as file:
            
            #json to xml
            xmltodict.unparse(data, file, pretty=True)

            #json string to xml syntax and save to file
            #file.write(xmltodict.unparse(data, pretty=True))

    except Exception as e:
        print("\t\tGot error: ", e)
        input("\t\t[!!!] Error while exporting JSON to XML file. Enter to exit")
        exit()



def exportYmlAsJson(data, filename):
    print("\n\t\tExporting --> ", filename)
    try:
        with open(filename, "w") as file:
            #yml to json
            json.dump(data, file, indent=4)
    except Exception as e:
        print("\t\tGot error: ", e)
        input("\t\t[!!!] Error while exporting YML/YAML to JSON file. Enter to exit")
        exit()

def exportYmlAsXml(data, filename):
    print("\n\t\tExporting --> ", filename)
    try:
        with open(filename, "w") as file:
            #yml to xml
            xmltodict.unparse(data, file, pretty=True)
    except Exception as e:
        print("\t\tGot error: ", e)
        input("\t\t[!!!] Error while exporting YML/YAML to XML file. Enter to exit")
        exit()



def exportXmlAsJson(data, filename):
    print("\n\t\tExporting --> ", filename)
    try:
        with open(filename, "w") as file:
            #xml to json
            json.dump(data, file, indent=4)
    except Exception as e:
        print("\t\tGot error: ", e)
        input("\t\t[!!!] Error while exporting XML to JSON file. Enter to exit")
        exit()

def exportXmlAsYml(data, filename):
    print("\n\t\tExporting --> ", filename)
    try:
        with open(filename, "w") as file:
            #xml to yml
            yaml.dump(data, file, indent=4)
    except Exception as e:
        print("\t\tGot error: ", e)
        input("\t\t[!!!] Error while exporting XML to YML/YAML file. Enter to exit")
        exit()

def main():
    arguments = checkArgs()

    print("\n\n\tLogs:")
    if arguments[0].split(".")[1] == "json":
        if arguments[1].split(".")[1] == "yaml" or arguments[1].split(".")[1] == "yml":
            data = importJson(arguments[0])
            exportJsonAsYml(data, arguments[1])
            
        elif arguments[1].split(".")[1] == "xml":
            data = importJson(arguments[0])
            exportJsonAsXml(data, arguments[1])

    elif arguments[0].split(".")[1] == "yaml" or arguments[0].split(".")[1] == "yml":
        if arguments[1].split(".")[1] == "json":
            data = importYml(arguments[0])
            exportYmlAsJson(data, arguments[1])
        elif arguments[1].split(".")[1] == "xml":
            data = importYml(arguments[0])
            exportYmlAsXml(data, arguments[1])

    elif arguments[0].split(".")[1] == "xml":
        if arguments[1].split(".")[1] == "json":
            data = importXml(arguments[0])
            exportXmlAsJson(data, arguments[1])
        elif arguments[1].split(".")[1] == "yaml" or arguments[1].split(".")[1] == "yml":
            
            data = importXml(arguments[0])
            
            exportXmlAsYml(data, arguments[1])

    else:
        input("Unknown error. Enter to exit")
        exit()
    
        




if __name__ == "__main__":
    main()