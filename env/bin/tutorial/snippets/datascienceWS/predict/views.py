# views.py 
from django.shortcuts import render_to_response
from django.shortcuts import render, HttpResponse
import requests
from src.model.CandidateMovementModel import CandidateMovementModel
from src.predict.CandidateMovementPrediction import CandidateMovementPrediction
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Document
from forms import DocumentForm
import src.const.TemplateData as templData
import csv
import json
from django.http import HttpResponseRedirect

# Create your views here.
global Data
def index(request):
    return HttpResponse('Hello World!')

def test(request):
    return HttpResponse('My second view!')

# def profile(request):
#     parsedData = []
#     if request.method == 'POST':
#         username = request.POST.get('user')
#         req = requests.get('https://api.github.com/users/' + username)
#         jsonList = []
#
#         jsonList.append(req.json())
#         #print jsonList
#         userData = {}
#         for data in jsonList:
#             userData['name'] = data['name']
#             userData['blog'] = data['blog']
#             userData['email'] = data['email']
#             userData['public_gists'] = data['public_gists']
#             userData['public_repos'] = data['public_repos']
#             userData['avatar_url'] = data['avatar_url']
#             userData['followers'] = data['followers']
#             userData['following'] = data['following']
#         parsedData.append(userData)
#     return render(request, 'app/profile.html', {'data': parsedData})

def movement(request):
    Data_pre=[]
    documents=[]
    form=[]

    if request.method=='POST':
        # Create Model
        #file = request.FILES['fileUpload']
        loc_training_data = 'data/trainingdata/dataset_07_Apr.csv'
        #print loc_training_data
        can = CandidateMovementModel(loc_training_data)
        print can
        model = can.createCandidateMovementModel()

    # test

        test_data = "data/test/sample_test_2.csv"
        file_save= "data/result_prediction.csv"
        predict = CandidateMovementPrediction(model,test_data,file_save)
        data, parsedData = predict.calProbMovementPrediction()

        Data_prediction=json.loads(parsedData)

        for data in Data_prediction:
            userData={}
            userData['candidate_id'] = data['candidate_id']
            userData['Employer'] = data['Employer']
            # userData['Moving'] = data['Moving']
            userData['Predicted'] = data['Predicted']
            Data_pre.append(userData)

    form = DocumentForm()
    return render(request, 'predict/profile.html', {'data':Data_pre, 'form': form},context_instance=RequestContext(request))

def Convert_csv_json(_file_name,format):
        csv_rows=[]
        file_csv=_file_name
        reader=csv.DictReader(file_csv)

        title=reader.fieldnames
        #print title
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        if format=='pretty':
            file_json=json.dumps(csv_rows, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False)
        else:
            file_json=json.dumps(csv_rows)
        return file_json

def list(request):
    Data_pre=[]
    form=[]
    # Handle file upload
    #file_name='heocon'
    if request.method == 'POST':
        file=request.FILES['docfile']
        newdoc = Document(docfile=file.read())
        #print file
        newdoc.save()

            # Redirect to the document list after POST
    else:
        form=DocumentForm()


    can = CandidateMovementModel(file)
    model = can.createCandidateMovementModel()


    test_data = "data/test/sample_test_2.csv"
    file_save= "data/result_prediction.csv"
    predict = CandidateMovementPrediction(model,test_data,file_save)
    data,data_csv = predict.calProbMovementPrediction()
    #
    parsedData=Convert_csv_json(data_csv,'pretty')
    Data_prediction=json.loads(parsedData)
    #
    #
    #
    #
    for data in Data_prediction:
        userData={}
        userData['candidate_id'] = data['candidate_id']
        userData['Employer'] = data['Employer']
        userData['Moving'] = data['Moving']
        userData['Predicted'] = data['Predicted']
        Data_pre.append(userData)

    # Load documents for the list page
    documents = Document.objects.all()
    return render(request, 'predict/profile.html', {'data':Data_pre, 'form': form},context_instance=RequestContext(request))





