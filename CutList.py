#Author-JSIOBJ
#Description-Generate a simple "cut list" from components in a design

import adsk.core, adsk.fusion, adsk.cam, traceback
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class CutListItem:
    """Cut list item (component)"""
    component: adsk.fusion.Component
    component_name: str
    component_material: str
    occurence_count: int
    thickness: float
    lengh: float
    width: float

    def __init__(self, component: adsk.fusion.Component):
        
        self.occurence_count = 1
        self.component = component
        self.component_name = component.name
        self.component_material = component.material.name

        # Computing dimensions from component bounding box sorted from smallest to biggest
        dims = sorted( [ (component.boundingBox.maxPoint.x - component.boundingBox.minPoint.x)*10,
                         (component.boundingBox.maxPoint.y - component.boundingBox.minPoint.y)*10,
                         (component.boundingBox.maxPoint.z - component.boundingBox.minPoint.z)*10
                       ]
               )

        self.thickness = dims[0]   # Assuming thickness is the smaller value
        self.length = dims[1]
        self.width = dims[2]

    def to_string(self,sep=','):
        return f"{self.component_name}{sep}{self.component_material}{sep}{self.occurence_count}{sep}{self.thickness : >5.1f}{sep}{self.l : >5.1f}{sep}{self.L : >5.1f}" 

@dataclass
class CutList:
    """Cut list (dict of cust list items)"""
    item_list: dict 

    def __init__(self, design: adsk.fusion.Design):

        self.item_list = {}

        # Getting all component occurences (each component may have one or more "occurence")
        occ_list = design.rootComponent.allOccurrences

        # Gather information about each unique component's occurence
        for occ in occ_list:
            
            # If not a "leaf", ignoring
            # TODO : Add hierarchy management
            if occ.childOccurrences:
                continue

            # if an occurence has already been added for this occurence's component, incr count
            if occ.component.name in self.item_list:
                self.item_list[occ.component.name].occurence_count += 1
            # If not, creating a new entry
            else:
                self.item_list[occ.component.name] = CutListItem(occ.component)

    def display(self,ui: adsk.core.UserInterface,sep=','):

        #item: CutListItem

        item_list_str = f"Name{sep}Material{sep}Qty{sep}Thickness{sep}Length{sep}Width" 

        for item in self.item_list.values():
            item_list_str += "\n" + item.to_string(',')

        ui.messageBox(item_list_str,"Cut List")

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        if not design:
            ui.messageBox('No active design', "Cut list")
            return

        cutList = CutList(design)
        cutList.display(ui)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
