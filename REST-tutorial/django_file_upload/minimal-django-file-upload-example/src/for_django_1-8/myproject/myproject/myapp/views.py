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


from ..src.const.TemplateData import cols_dep_var_header
from ..src.model.CandidateMovementModel import CandidateMovementModel
from ..src.predict.CandidateMovementPrediction import CandidateMovementPrediction
from ..src.const import TemplateData as templData
import pandas as pd
import csv

# class View():
#     def __init__(self,Data,form,documents,request,test_data):
#         self.form=form
#         self.Data=Data
#         self.documents=documents
#         self.request=request
#         self.test_data=test_data
def list(request):
    # Handle file upload
    Data=[]
    temp_Data=[]
    if request.method == 'POST':
        #docId = request.POST.get('id', None)
        #print docId
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            file_save= request.FILES['docfile'].read()
            files=file_save.replace('\n',',')
            files_list= files.split(',')
            header=[]
            for i in range(0,len(cols_dep_var_header)):
                header.append(files_list[i])
            if set(header)==set(cols_dep_var_header):
                if ' ' not in files_list:
                    newdoc.save()
                    return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
            else:
                form=DocumentForm()
                documents=Document.objects.all()
                return render(request,'list.html',{'form':form,'documents':documents})


            # for h in cols_dep_var_header:
            #     if h in header:
            # #print cols_dep_var_header
            # for line in files._fieldnames:
            #     print line
            #     breakgi

            # if request.handelfailupload(newdoc):
            #     #print newdoc.
            # else:
            #newdoc.save()
            #Check if file is the same
             #toDo

            # Redirect to the document list after POST

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

def handelfailupload(file):
    #todo
    return 1