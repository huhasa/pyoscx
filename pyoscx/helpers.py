import xml.etree.ElementTree as ET
import xml.dom.minidom as mini


import os

def esminiRunner(scenario,esminipath = 'esmini'):
    """ write a scenario and runs it in esmini
        Parameters
        ----------
            scenario (Scenario): the pypscx scenario to run

            esminipath (str): the path to esmini 
                Default: pyoscx

    """
    _scenariopath = os.path.join(esminipath,'resources','xosc')
    scenario.write_xml(os.path.join(_scenariopath,'pythonscenario2.xosc'),True)
    os.system('./esmini/bin/EnvironmentSimulator --osc esmini/resources/xosc/pythonscenario2.xosc --threads --window 50 50 800 400' )
    

def prettyprint(element):
    """ prints the element to the commandline

        Parameters
        ----------
            element (Element): element to print

    """
    rough = ET.tostring(element,'utf-8')
    reparsed = mini.parseString(rough)
    print(reparsed.toprettyxml(indent="\t"))

def printToFile(element,filename,prettyprint=True):
    """ prints the element to a xml file

        Parameters
        ----------
            element (Element): element to print

            filename (str): file to save to

            prettyprint (bool): pretty or "ugly" print

    """
    if prettyprint:    
        rough = ET.tostring(element,'utf-8')
        reparsed = mini.parseString(rough)
        towrite = reparsed.toprettyxml(indent="\t")
        with open(filename,"w") as file_handle:
            file_handle.write(towrite)
    else:
        tree = ET.ElementTree(element)
        with open(filename,"wb") as file_handle:
            tree.write(file_handle)