# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponse
from django.http import Http404
import os.path
from models import Document
from forms import DocumentForm
import csv
import json

from ..src.model.CandidateMovementModel import CandidateMovementModel
from ..src.predict.CandidateMovementPrediction import CandidateMovementPrediction
from ..src.const import TemplateData as templData



def list(request):
    # Handle file upload
    Data=[]
    if request.method == 'POST':
        #docId = request.POST.get('id', None)
        #print docId
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            #print newdoc.
            newdoc.save()
            #Check if file is the same
             #toDo
            # documents = Document.objects.all()
            # file_len=len(documents)
            # file_path=documents[file_len-1].docfile.path
            # Data=modeltest(file_path)

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
            #return HttpResponse('Success')
    else:
        docId = Document.objects.all()
        # delete file is not exist


        for id in docId:
            if not os.path.isfile(id.docfile.path):
                id.delete()

            if len(docId)>5:
                id.delete()

        # check file if not updated
        form = DocumentForm()  # A empty, unbound form
    documents = Document.objects.all()

    if len(documents)!=0:
        file_path=documents[len(documents)-1].docfile.path
        Data=modeltest(file_path)
        #print Data

    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form,'data':Data},
        context_instance=RequestContext(request)
    )


def modeltest(test_data):
    Data_pre=[]
    loc_training_data = 'data/trainingdata/dataset_07_Apr.csv'
        #print loc_training_data
    can = CandidateMovementModel(loc_training_data)
        #print can
    model = can.createCandidateMovementModel()
    #print model
    #print type(model)

    # test

        #test_data = "data/test/sample_test_2.csv"
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

    #form = DocumentForm()
    return Data_pre

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
