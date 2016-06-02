#!/usr/bin/env python
import shapefile_point
import sys
e=shapefile_point.Editor(sys.argv[1])
e.buildQuadTree()
output=open(sys.argv[2],'w')
e.printNode(e.root,output)
output.close()
