import SimpleITK as sitk
import numpy as np

def transform(src,outpath):
    array = np.load(src)
    image = sitk.GetImageFromArray(array)
    sitk.WriteImage(image, outpath)
    return

def combination(prediction, truth):
    pred_array=np.load(predction)
    tru_array=np.load(truth)
    ground_one=np.argmax(tru_array)
    predict_one=np.argmax(pred_array)
    

if __name__ == '__main__':
    i = 200
    src = "predict_" + str(i) +".npy"
    truthsrc = "truth_" + str(i) +".npy"

    outpath = "predict_" + str(i) +".mha"
    truthoutpath = "truth_" + str(i) + ".mha"
   
    transform(src,outpath)
    transform(truthsrc, truthoutpath)