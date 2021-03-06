
from opentrons import robot, containers, instruments
import utilities

def getEquipment():
        equipment={}
        ############## DECK LAYOUT BEGINS HERE
        #CONTAINER DEFINITIONS:
        TransposeTipBox=True

        #DECK:
        # col A = left-hand side when viewed from front
        # row 1 = first row viewed from front
        equipment['trash']=containers.load('point', "D1","trash")
        equipment['p200rack'] = containers.load('tiprack-200ul', 'E2', 'tiprack200')
        if TransposeTipBox:
            equipment['p1000rack']  = utilities.create_container_instance("TR1000-Transposed",slot="A1",grid=(8,12),spacing=(9.02,-9.02),diameter=5,depth=85,Transposed=True)
        else:
            equipment['p1000rack']  = utilities.create_container_instance("TR1000-Normal",slot="A1",grid=(8,12),spacing=(9.02,9.02),diameter=5,depth=85)
        equipment['CulturePlate96']  = containers.load('96-flat', 'D2')

        # create_container_instance in utilities.py does an ad-hoc creation of a custom
        # container without the need to save to JSON file. There is a bug in Opentrons code
        # that randomises order of wells in JSON definition files for custom containers as 
        # soon as more than one container is used, which is why containers.create is not an
        # option for 2 containers.
        equipment['CulturePlate']=utilities.create_container_instance("CulturePlate24",slot="D2",grid=(4,6),spacing=(19.304,19.304),diameter=16.26,depth=18)
        equipment['CulturePlate2']=utilities.create_container_instance("CulturePlate242",slot="C2",grid=(4,6),spacing=(19.304,19.304),diameter=16.26,depth=18)
        equipment['CulturePlate6well']=utilities.create_container_instance("CulturePlate6",slot="D2",grid=(2,3),spacing=(39.12,39.12),diameter=34.80,depth=11.27)

        equipment['AliquotPlate']  = containers.load('96-flat', 'B2', 'AliquotPlate')
        equipment['TubBlood']=utilities.create_container_instance("TubBlood",slot="C1",grid=(8,1),spacing=(9.02,9.02),diameter=0,depth=55)
        equipment['TubMedia']=utilities.create_container_instance("TubMedia",slot="C1",grid=(8,1),spacing=(9.02,9.02),diameter=0,depth=55)
        equipment['TubSybr']=utilities.create_container_instance("TubSybr",slot="C1",grid=(8,1),spacing=(9.02,9.02),diameter=0,depth=55)

        #PIPETTE(S)
        equipment['p1000'] = instruments.Pipette(
            name="P1000",
            axis="b",
            min_volume=20,
            max_volume=1000,
            tip_racks=[equipment['p1000rack']],
            trash_container=equipment['trash']
        )


        equipment['p200x8'] = instruments.Pipette(
            name="p200x8",
            axis="a",
            min_volume=20,
            max_volume=300,
            trash_container=equipment['trash'],
            channels=8
        )
        return(equipment)
