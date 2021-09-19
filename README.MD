# Cut list script
This is a simple Fusion 360 script for building a "cut list" from a design. It is mainly intended for woodworking

It takes any "leaf" component (that is a component with no sub component) and add it to the cut list with its name, material, thickness, length and width.
As a rule of thumb, thickness is the smallest dimensions, width the greatest, length being the one in between
It display the results in a message box which content could be copy/paste.

# Output Example 

Name,Material,Qty,Thickness,L,l
Salle de bain,Steel,1,2220.8,2342.3,2725.0
Lavabo,Steel,1,595.0,755.0,897.0
Chaudière,Steel,1,340.0,408.0,843.0
Radiateur,Steel,1, 70.0,520.0,602.0
Planche A1,MDF Medium Density Fiberboard,1, 10.0,440.0,1236.0
Planche A2,MDF Medium Density Fiberboard,1, 10.0,100.0,1321.0
Planche A3,MDF Medium Density Fiberboard,1, 10.0,455.0,887.0
Planche A4,MDF Medium Density Fiberboard,1, 10.0,100.0,455.0
Planche B1,MDF Medium Density Fiberboard,1, 10.0,302.0,887.0
Planche B2,MDF Medium Density Fiberboard,1, 10.0,100.0,302.0
Planche B3,MDF Medium Density Fiberboard,1, 10.0,541.0,715.0
Planche B4,MDF Medium Density Fiberboard,1, 10.0, 70.0,541.0
Planche C1,MDF Medium Density Fiberboard,1, 10.0,440.0,1488.0
Planche C2,MDF Medium Density Fiberboard,1, 10.0,340.0,645.0
Planche D1,MDF Medium Density Fiberboard,1, 10.0,150.0,640.0
Planche D2,MDF Medium Density Fiberboard,1, 10.0, 40.0,640.0
Planche D3,MDF Medium Density Fiberboard,1, 10.0, 40.0,160.0

# TODO
* Add hierachy management
* improve units management (as of today, using mm for output)
* Add filtering capabilities