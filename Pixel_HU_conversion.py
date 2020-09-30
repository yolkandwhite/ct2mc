#dicom_dir = dicom folder directory
#output_dir = Where HU converted csv file will be generated

def Pix_HU_conv(dicom_dir = '/Users/nyh/Documents/RP_Lab/ct2mc/phantom/metal_omar/', output_dir = "/Users/nyh/Documents/RP_Lab/ct2mc/phantom/", slope = 1, intercept = -1024):
    import os
    from numpy import savetxt
    import pydicom
    import natural_keys

    out = output_dir +'HU_converted/'
    if not os.path.exists(out):
        os.mkdir(out)

    print("HU_conversion START")
    slope = slope
    intercept = intercept

    for (path, dir, files) in os.walk(dicom_dir):
        files = sorted(files, key = natural_keys.natural_keys)
        i = 0

        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.DCM':
                file_dir = path + filename
                dataset = pydicom.dcmread(file_dir)
                pixel = dataset.pixel_array
                #print(i)
                #print(file_dir)
                Phantom_HU_array = pixel * slope + intercept
                #print(Phantom_HU_array)
                savetxt(out+str(i)+ '_Pix2HU_conv.csv', Phantom_HU_array, delimiter=',')
                i += 1
    
    print("HU_conversion COMPLETED")

Pix_HU_conv()