# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.12-1 replay file
# Internal Version: 2012_03_13-20.44.39 119612
# Run by Anzong on Sun Jan 18 10:13:01 2015
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=189.999997615814, 
    height=126.824998408556)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('test.cae')
#: The model database "C:\Users\Anzong\Desktop\test.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Frame']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Steel')
mdb.models['Model-1'].materials['Steel'].Elastic(table=((200000000000.0, 0.3), 
    ))
mdb.models['Model-1'].TrussSection(name='FrameSection', material='Steel', 
    area=1.96349540849362e-05)
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
p = mdb.models['Model-1'].parts['Frame']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#7f ]', ), )
region = p.Set(edges=edges, name='Set-1')
p = mdb.models['Model-1'].parts['Frame']
p.SectionAssignment(region=region, sectionName='FrameSection', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
mdb.models['Model-1'].StaticLinearPerturbationStep(name='Apply load', 
    previous='Initial', description='10 kN central load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Apply load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.50669, 
    farPlane=5.49331, width=2.90668, height=1.43737, viewOffsetX=-0.0428107, 
    viewOffsetY=0.00856215)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['Model-1'].parts['Frame']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['Model-1'].parts['Frame']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Frame']
a.Instance(name='Frame-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['Frame-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#4 ]', ), )
region = a.Set(vertices=verts1, name='Set-1')
mdb.models['Model-1'].DisplacementBC(name='Fixed', createStepName='Initial', 
    region=region, u1=SET, u2=SET, ur3=UNSET, amplitude=UNSET, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['Frame-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#10 ]', ), )
region = a.Set(vertices=verts1, name='Set-2')
mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Initial', 
    region=region, u1=UNSET, u2=SET, ur3=UNSET, amplitude=UNSET, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Apply load')
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['Frame-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#8 ]', ), )
region = a.Set(vertices=verts1, name='Set-3')
mdb.models['Model-1'].ConcentratedForce(name='Force', 
    createStepName='Apply load', region=region, cf2=-10000.0, 
    distributionType=UNIFORM, field='', localCsys=None)
p1 = mdb.models['Model-1'].parts['Frame']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
mdb.meshEditOptions.setValues(enableUndo=True, maxUndoCacheElements=0.5)
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
elemType1 = mesh.ElemType(elemCode=T2D2, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['Frame']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#7f ]', ), )
pickedRegions =(edges, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.06172, 
    farPlane=4.65608, width=1.95683, height=0.971544, viewOffsetX=-0.00133005, 
    viewOffsetY=-0.00199512)
p = mdb.models['Model-1'].parts['Frame']
p.seedPart(size=1.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Frame']
p.generateMesh()
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Frame', model='Model-1', 
    description='Two-dimensional overhead hoist frame', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=50, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Frame'].submit(consistencyChecking=OFF, datacheckJob=True)
#: The job input file "Frame.inp" has been submitted for analysis.
#: Error in job Frame: Unable to change the current working directory to C:\Users\Anzong\AppData\Local\Temp\Anzong_Frame_6708. 
#: Job Frame aborted due to errors.
mdb.save()
#: The model database has been saved to "C:\Users\Anzong\Desktop\test.cae".
