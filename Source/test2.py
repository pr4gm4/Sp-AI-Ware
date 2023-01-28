import apiml as ml
import glob as gl
import numpy as np

def showResults(model,xinput):
    for estimator in model.estimators_:
        print(estimator.__class__.__name__)
        print(estimator.predict(np.array([xinput,])))



model = ml.loadModel(gl.MODELPATH)

showResults(model)