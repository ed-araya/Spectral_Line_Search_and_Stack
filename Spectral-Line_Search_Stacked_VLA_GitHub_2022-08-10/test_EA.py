tc_path = '/Users/earaya/INVESTIGACION/CH3OH_19GHz_GBT_IR18566_NGC7538_VLA_W3OH/DATA/W3OH_Cont_Mode_2014_Rodriguez/'
images_cube = ['W3OH_19GHz_CH3OH_cube.image.pbcor', 'W3OH_19GHz_CH3OH_cube.image.pbcor']

temp=[]
temp2=[]
for cube in images_cube:
    stats=imstat(imagename=tc_path+cube,  box='50,50,300,300', axes=[0,1])
    if len(stats['rms'])>256:
        images_cube.remove(cube)
        print('Removed from the stacking %s' %cube)
    else: 
        temp.append(cube[cube.find('(')+1:cube.find(')')])
        #temp.append(int(filter(str.isdigit,cube))) 
    temp.sort(reverse=True)
    temp=[str(x) for x in temp]
    for n in temp:
        for name in images_cube:
            if n in name:
                temp2.append(name)
    images_cube=temp2
    print( images_cube)
    images_cube.append(tc_path)
            
    #Stacking Cubes
    execfile("stacking_module.py",globals())
    #print images_cube
    stack(images_cube)
