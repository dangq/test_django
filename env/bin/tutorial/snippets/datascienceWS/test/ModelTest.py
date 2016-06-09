from src.model.CandidateMovementModel import CandidateMovementModel
from src.predict.CandidateMovementPrediction import CandidateMovementPrediction
import src.const.TemplateData as templData
import src.util.DataProcessing as dp
import pandas as pd
# from src.model.CandidateMovementModel import CandidateMovementModel
# from src.predict.CandidateMovementPrediction import CandidateMovementPrediction
# import src.const.TemplateData as templData
# Create Model
loc_training_data = '../data/trainingdata/dataset_07_Apr.csv'

can = CandidateMovementModel(loc_training_data)
model = can.createCandidateMovementModel()

# test

test_data = "../data/test/sample_test_2.csv"
predict = CandidateMovementPrediction(model,test_data, "test.csv")
data = predict.calProbMovementPrediction()
print data
# data = pd.read_csv(test_data, sep=',')
# # a = dp.convertDataFrameIntoLists(data)
# a = map(list, data.values)
# print a[0][1]



