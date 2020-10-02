#HU_dir = dicom folder directory
#output_dir = Where Material Number converted csv file will be generated

def HU_MN_conv(HU_dir = '/Users/nyh/Documents/RP_Lab/ct2mc/phantom/HU_converted/', output_dir = "/Users/nyh/Documents/RP_Lab/ct2mc/phantom/"):
    import os
    from numpy import savetxt
    import numpy as np
    import pydicom
    import natural_keys

    out = output_dir +'MaterialNumber_converted/'
    if not os.path.exists(out):
        os.mkdir(out)

    print("Material_Number_conversion START")

    for (path, dir, files) in os.walk(HU_dir):
        files = sorted(files, key = natural_keys.natural_keys)
        i = 0

        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.csv':
                file_dir = path + filename
                loader = np.loadtxt(file_dir, delimiter=",", dtype=np.float32)
                x, y = loader.shape
                loader = loader.tolist()
                for a in range(x):
                    for b in range(y):
                        if loader[a][b] < -900:
                            loader[a][b] = "m1"
                        elif -900 <= loader[a][b] < -100:
                            loader[a][b] = "m2"
                        elif -100 <= loader[a][b] < 20:
                            loader[a][b] = "m3"
                        elif 20 <= loader[a][b] < 100:
                            loader[a][b] = "m4"
                        elif 100 <= loader[a][b] < 250:
                            loader[a][b] = "m5"
                        elif 250 <= loader[a][b] < 400:
                            loader[a][b] = "m6"
                        elif 400 <= loader[a][b] < 550:
                            loader[a][b] = "m7"
                        elif 550 <= loader[a][b] < 700:
                            loader[a][b] = "m8"
                        elif 700 <= loader[a][b] < 850:
                            loader[a][b] = "m9"
                        elif 850 <= loader[a][b] < 1000:
                            loader[a][b] = "m10"
                        elif 1000 <= loader[a][b] < 1150:
                            loader[a][b] = "m11"
                        elif 1150 <= loader[a][b] < 1300:
                            loader[a][b] = "m12"
                        elif 1300 <= loader[a][b] < 1450:
                            loader[a][b] = "m13"
                        elif 1450 <= loader[a][b]:
                            loader[a][b] = "m14"


                savetxt(out+str(i)+ '_HU2MN_conv.csv', loader, delimiter=',', fmt="%s")
                i += 1                        
    
    print("Material_Number_conversion COMPLETED")

HU_MN_conv()
