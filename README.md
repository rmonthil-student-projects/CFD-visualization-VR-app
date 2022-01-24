# CFD Visualization VR App
Scripts and app that let you export Paraview data and view them with an HMD.
This repository aims to have few dependencies : The [Paraview](https://www.paraview.org/) software and [Python 2.7](https://www.python.org/). For now, this will only work on Linux.

## Instructions

Download or clone this project :

```user
git clone https://github.com/LeDernier/CFD_Visualization_VR_App.git
```

In the just created folder, create a folder **objs** and run **Paraview** :

```user
cd CFD-visualisation-VR-app
mkdir objs
paraview
```

Open the data you want to visualize and applie all the filters you need. When finished, just run the script **pv2obj.py** using the python scripting window in the paraview GUI.
This will export all you data as obj files in the objs folder.
Then you just have to run the **VR_Visualisation.x86_64 app**.

```user
./VR_Visualisation.x86_64
```

You will be able to choose the color of each object and the global scene scale. Then wait until its all loaded and enjoy.
