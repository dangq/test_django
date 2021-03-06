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

def profile(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []

        jsonList.append(req.json())
        #print jsonList
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        parsedData.append(userData)
    return render(request, 'app/profile.html', {'data': parsedData})
def model(request):
    Data_pre=[]
    documents=[]
    form=[]

    if request.method=='POST':
        # Create Model
        #file = request.FILES['fileUpload']
        loc_training_data = 'data/trainingdata/dataset_07_Apr.csv'
        #print loc_training_data
        can = CandidateMovementModel(loc_training_data)
        #print can
        model = can.createCandidateMovementModel()
    #print model
    #print type(model)

    # test

        test_data = "data/test/sample_test_2.csv"
        file_save= "data/result_prediction.csv"
        predict = CandidateMovementPrediction(model,test_data,file_save)
        data,data_csv = predict.calProbMovementPrediction()
        #print data_csv
        parsedData=Convert_csv_json(data_csv,'pretty')
        Data_prediction=json.loads(parsedData)
        #print Data_prediction




        for data in Data_prediction:
            userData={}
            userData['candidate_id'] = data['candidate_id']
            userData['Employer'] = data['Employer']
            userData['Moving'] = data['Moving']
            userData['Predicted'] = data['Predicted']
            Data_pre.append(userData)

    form = DocumentForm()
    return render(request, 'app/profile.html', {'data':Data_pre, 'form': form},context_instance=RequestContext(request))

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
    #print 111
    # Handle file upload
    #file_name='heocon'
    if request.method == 'POST':
        loc_training_data = 'data/trainingdata/dataset_07_Apr.csv'
        file_save= "data/result_prediction.csv"
        can = CandidateMovementModel(loc_training_data)
        model = can.createCandidateMovementModel()

        predict = CandidateMovementPrediction(model,request.FILES['docfile'],file_save)

        data,data_csv = predict.calProbMovementPrediction()
        print data
        #print '111'
        #print request.FILES['docfile'].read()
        #file=request.FILES['docfile']
        #newdoc = Document(docfile=file.read())
        #print file
        #newdoc.save()

         # Redirect to the document list after POST
        #file=with
    else:
         form = DocumentForm()
    #print file
    # can = CandidateMovementModel(file)
    # model = can.createCandidateMovementModel()
    #
    #
    # test_data = "data/test/sample_test_2.csv"
    # file_save= "data/result_prediction.csv"
    # #
    # parsedData=Convert_csv_json(data_csv,'pretty')
    # Data_prediction=json.loads(parsedData)
    # #
    # #
    # #
    # #
    # for data in Data_prediction:
    #     userData={}
    #     userData['candidate_id'] = data['candidate_id']
    #     userData['Employer'] = data['Employer']
    #     userData['Moving'] = data['Moving']
    #     userData['Predicted'] = data['Predicted']
    #     Data_pre.append(userData)

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    #return documents,form
    # return render_to_response(
    #     'list.html',
    #     {'documents': documents, 'form': form},
    #     context_instance=RequestContext(request)
    # )
    #return HttpResponse('Success!')
    #return HttpResponseRedirect('/app/model/?a='+file_name)
    # else:
    #      form=DocumentForm()

    return render(request, 'app/profile.html', {'data':Data_pre, 'form': form},context_instance=RequestContext(request))
    #return HttpResponse('Running')


# def list(request):
#     # Handle file upload
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = Document(docfile=request.FILES['docfile'])
#             newdoc.save()
#
#             # Redirect to the document list after POST
#             return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
#     else:
#         form = DocumentForm()  # A empty, unbound form
#
#     # Load documents for the list page
#     documents = Document.objects.all()
#
#     # Render list page with the documents and the form
#     return render_to_response(
#         'list.html',
#         {'documents': documents, 'form': form},
#         context_instance=RequestContext(request)
#     )



