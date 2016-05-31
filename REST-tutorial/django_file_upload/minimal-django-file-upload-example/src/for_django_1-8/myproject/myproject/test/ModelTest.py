from src.model.CandidateMovementModel import CandidateMovementModel
from src.predict.CandidateMovementPrediction import CandidateMovementPrediction
import src.const.TemplateData as templData
# Create Model
loc_training_data = '../data/trainingdata/dataset_07_Apr.csv'

can = CandidateMovementModel(loc_training_data)
model = can.createCandidateMovementModel()
#print model
#print type(model)

# test

test_data = "../data/test/sample_test_2.csv"
file_save= "../data/result_prediction.csv"
predict = CandidateMovementPrediction(model,test_data,file_save)
data = predict.calProbMovementPrediction()
#print type(data)



