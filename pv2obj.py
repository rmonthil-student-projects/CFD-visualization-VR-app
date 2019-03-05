#### import os to launch external programs
import os
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

renderView = GetActiveViewOrCreate('RenderView')

print "Sources : "
print GetSources()

i = 1 
for s in GetSources():
    print 'Managing : ' + s[0]
    extractSurface = ExtractSurface(Input=FindSource(s[0]))
    SaveData('./objs/' + s[0] + "t" + '.obj', proxy=extractSurface)
    i += 1
