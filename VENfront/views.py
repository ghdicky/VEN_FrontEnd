# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from mysqldb import*

from django.http import JsonResponse # for JsonResponse
from django.views.decorators.csrf import csrf_exempt # to disable csrf (cross domain security check) of Django

import json

testdata = [1, 5, 7, 3, 5, 6, 6, 8, 9,7]
# Create your views here.
def index(request):
    return HttpResponse('cool! but why it is directed here?')
def loggedin(request):
    return HttpResponse('good! you have loggedin')
def loggedout(request):
    return HttpResponse('you logged out, we will miss you')
def invalid(request):
    return HttpResponse('the user name is invalid')
    #return render(request,'test.html')
def googleview(request):
    venpower = get_ven_power('test')
    venusage = get_ven_energy('test')
    eventinfo = get_events('test')
    venlog = get_ven_log('test')
    veninfo = get_ven_info('test')
    vendefaultoptmode = get_ven_defaultoptmode('test')
    #return HttpResponse('the d3 view page is here')
    venevent = get_ven_event('test')
    veneventsignal = get_ven_event_signal_by_eventID('test', venevent[0][0])
    veneventactiveperiod = get_ven_event_active_period_by_eventID('test', venevent[0][0])

    vengtnet1allhousesrecord = get_gtnet_record_allhouses('test')


    #if the data for the context is a single element with u lable
    #then need to use json.dumps to remove the u label and the comma and make the array with single element from [(u'OptOut',)] to [['OptOut']]
    return render( request, 'd3view.html',context={'venpower': venpower, 'venusage': venusage, 'eventinfo': eventinfo, 'venlog': venlog, 'veninfo': veninfo, 'vendefaultoptmode': json.dumps(vendefaultoptmode), 'venevent': venevent, 'veneventsignal': veneventsignal, 'veneventactiveperiod': veneventactiveperiod, 'vengtnet1allhousesrecord': vengtnet1allhousesrecord} )


@csrf_exempt
def ajax_get_ven_info(request):
    veninfo = get_ven_info('test')

    #venname = [];
    #vtnurl = [];

    #for i in range(0, 10, 4):
    #    venname.append(veninfo[0][0])
    #    vtnurl.append(veninfo[0][1])

    json_content = {
        "venName": veninfo[0][0],
        "venID": veninfo[0][1],
        "vtnID": veninfo[0][2],
        "vtnURL": veninfo[0][3],
        "pollFrequency": veninfo[0][4]
    }

    #return JsonResponse({"venName": veninfo[0][0], "vtnURL": veninfo[0][1]}, safe=False)
    return JsonResponse(json_content, safe=False)
    #return HttpResponse(veninfo)


@csrf_exempt
def ajax_get_defaultoptmode(request):
    defaultoptmode = get_ven_defaultoptmode('test')
    json_content = {"defaultOptMode": defaultoptmode}

    return JsonResponse(json_content, safe=False)


@csrf_exempt
def ajax_get_ven_log(request):
    venlog = get_ven_log('test')

    json_records_full=[]
    record_single = {}

    #return JsonResponse(venlog, safe=False)

    #construct the json_record_full using for loop
    #the json_record_full is indeed json_record_full = { ["time": 1, "responseTime": 1, "venRequest": 1, "vtnResponse": 1, "responseCode": 1, "responseDescription": 1],
    #                                                    ["time": 2, "responseTime": 2, "venRequest": 2, "vtnResponse": 2, "responseCode": 2, "responseDescription": 2] }
    #                                                = {json_record_full[0],
    #                                                   json_record_full[1],
    #                                                   json_record_full[2], }
    for i in range(0, len(venlog)):
        record_single = {
                         "time": venlog[i][0],
                         "responseTime": venlog[i][1],
                         "venRequest": venlog[i][2],
                         "vtnResponse": venlog[i][3],
                         "responseCode": venlog[i][4],
                         "responseDescription": venlog[i][5],
                         }
        json_records_full.append(record_single) #append a new element to the python array

    #print(json_records_full)

    return JsonResponse(json_records_full, safe=False)


@csrf_exempt
def ajax_get_ven_event(request):
    venevent = get_ven_event('test')

    json_records_full=[]
    record_single = {}

    #return JsonResponse(venlog, safe=False)

    #construct the json_record_full using for loop
    #the json_record_full is indeed json_record_full = { ["time": 1, "responseTime": 1, "venRequest": 1, "vtnResponse": 1, "responseCode": 1, "responseDescription": 1],
    #                                                    ["time": 2, "responseTime": 2, "venRequest": 2, "vtnResponse": 2, "responseCode": 2, "responseDescription": 2] }
    #                                                = {json_record_full[0],
    #                                                   json_record_full[1],
    #                                                   json_record_full[2], }
    for i in range(0, len(venevent)):
        record_single = {
                         "eventID": venevent[i][0],
                         "eventTime": venevent[i][1],
                         "eventDuration": venevent[i][2],
                         "eventStatus": venevent[i][3],
                         "optState": venevent[i][4],
                         "marketContext": venevent[i][5],
                         #"signalType": venevent[i][6],
                         #"currentValue": venevent[i][7],
                         "vtnComment": venevent[i][6],
                         "testEvent": venevent[i][7],
                         "responseRequired": venevent[i][8],
                         "modificationNumber": venevent[i][9]
                         }
        json_records_full.append(record_single) #append a new element to the python array

    #print(json_records_full)

    return JsonResponse(json_records_full, safe=False)


@csrf_exempt
def ajax_get_ven_event_active_period(request):
    veneventactiveperiod = get_ven_event_active_period_by_eventID('test', request.body)

    json_records_full=[]
    record_single = {}

    #return JsonResponse(venlog, safe=False)

    #construct the json_record_full using for loop
    #the json_record_full is indeed json_record_full = { ["time": 1, "responseTime": 1, "venRequest": 1, "vtnResponse": 1, "responseCode": 1, "responseDescription": 1],
    #                                                    ["time": 2, "responseTime": 2, "venRequest": 2, "vtnResponse": 2, "responseCode": 2, "responseDescription": 2] }
    #                                                = {json_record_full[0],
    #                                                   json_record_full[1],
    #                                                   json_record_full[2], }
    for i in range(0, len(veneventactiveperiod)):
        record_single = {
                         "startTime": veneventactiveperiod[i][0],
                         "duration": veneventactiveperiod[i][1],
                         "startAfter": veneventactiveperiod[i][2],
                         "eiNotification": veneventactiveperiod[i][3],
                         "eiRampUp": veneventactiveperiod[i][4],
                         "eiRecovery": veneventactiveperiod[i][5],
                         #"optState": venevent[i][4],
                         #"marketContext": venevent[i][5],
                         #"signalType": venevent[i][6],
                         #"currentValue": venevent[i][7],
                         #"vtnComment": venevent[i][6],
                         #"testEvent": venevent[i][7],
                         #"responseRequired": venevent[i][8],
                         #"modificationNumber": venevent[i][9]
                         }
        json_records_full.append(record_single) #append a new element to the python array

    #print(json_records_full)

    return JsonResponse(json_records_full, safe=False)


@csrf_exempt
def ajax_get_ven_event_signal(request):
    veneventsignal = get_ven_event_signal_by_eventID('test', request.body)

    json_records_full=[]
    record_single = {}

    #return JsonResponse(venlog, safe=False)

    #construct the json_record_full using for loop
    #the json_record_full is indeed json_record_full = { ["time": 1, "responseTime": 1, "venRequest": 1, "vtnResponse": 1, "responseCode": 1, "responseDescription": 1],
    #                                                    ["time": 2, "responseTime": 2, "venRequest": 2, "vtnResponse": 2, "responseCode": 2, "responseDescription": 2] }
    #                                                = {json_record_full[0],
    #                                                   json_record_full[1],
    #                                                   json_record_full[2], }
    for i in range(0, len(veneventsignal)):
        record_single = {
                         "eventID": veneventsignal[i][0],
                         "signalID": veneventsignal[i][1],
                         "signalName": veneventsignal[i][2],
                         "signalType": veneventsignal[i][3],
                         "signalInterval": veneventsignal[i][4],
                         "UID": veneventsignal[i][5],
                         "targetValue": veneventsignal[i][6],
                         "currentValue": veneventsignal[i][7],
                         "modificationNumber": veneventsignal[i][8],
                         #"currentValue": venevent[i][7],
                         #"vtnComment": venevent[i][6],
                         #"testEvent": venevent[i][7],
                         #"responseRequired": venevent[i][8],
                         #"modificationNumber": venevent[i][9]
                         }
        json_records_full.append(record_single) #append a new element to the python array

    #print(json_records_full)

    return JsonResponse(json_records_full, safe=False)


@csrf_exempt
def ajax_get_gtnet1_record_substation(request):
    gtnet1record_substation = get_gtnet1_record_substation('test')

    json_records_full=[]
    record_single = {}

    #return JsonResponse(venlog, safe=False)

    #construct the json_record_full using for loop
    #the json_record_full is indeed json_record_full = { ["time": 1, "responseTime": 1, "venRequest": 1, "vtnResponse": 1, "responseCode": 1, "responseDescription": 1],
    #                                                    ["time": 2, "responseTime": 2, "venRequest": 2, "vtnResponse": 2, "responseCode": 2, "responseDescription": 2] }
    #                                                = {json_record_full[0],
    #                                                   json_record_full[1],
    #                                                   json_record_full[2], }
    for i in range(0, len(gtnet1record_substation)):
        record_single = {
                         "timestamp": gtnet1record_substation[i][0],
                         "P": gtnet1record_substation[i][1],
                         "Q": gtnet1record_substation[i][2],
                         }
        json_records_full.append(record_single) #append a new element to the python array

    #print(json_records_full)

    return JsonResponse(json_records_full, safe=False)


@csrf_exempt
def ajax_get_gtnet1_record_house21(request):
    gtnet1record_house21 = get_gtnet1_record_house21('test')

    json_records_full=[]
    record_single = {}

    #return JsonResponse(venlog, safe=False)

    #construct the json_record_full using for loop
    #the json_record_full is indeed json_record_full = { ["time": 1, "responseTime": 1, "venRequest": 1, "vtnResponse": 1, "responseCode": 1, "responseDescription": 1],
    #                                                    ["time": 2, "responseTime": 2, "venRequest": 2, "vtnResponse": 2, "responseCode": 2, "responseDescription": 2] }
    #                                                = {json_record_full[0],
    #                                                   json_record_full[1],
    #                                                   json_record_full[2], }
    for i in range(0, len(gtnet1record_house21)):
        record_single = {
                         "timestamp": gtnet1record_house21[i][0],
                         "P": gtnet1record_house21[i][1],
                         "Q": gtnet1record_house21[i][2],
                         }
        json_records_full.append(record_single) #append a new element to the python array

    #print(json_records_full)

    return JsonResponse(json_records_full, safe=False)


@csrf_exempt
def ajax_get_gtnet_record_all_houses(request):
    gtnetrecord_allhouses = get_gtnet_record_allhouses('test')

    json_records_full=[]
    record_single = {}

    #return JsonResponse(venlog, safe=False)

    #construct the json_record_full using for loop
    #the json_record_full is indeed json_record_full = { ["time": 1, "responseTime": 1, "venRequest": 1, "vtnResponse": 1, "responseCode": 1, "responseDescription": 1],
    #                                                    ["time": 2, "responseTime": 2, "venRequest": 2, "vtnResponse": 2, "responseCode": 2, "responseDescription": 2] }
    #                                                = {json_record_full[0],
    #                                                   json_record_full[1],
    #                                                   json_record_full[2], }
    for i in range(0, len(gtnetrecord_allhouses)):
        record_single = {
                         "locationID": gtnetrecord_allhouses[i][0],
                         "timestamp": gtnetrecord_allhouses[i][1],
                         "P": gtnetrecord_allhouses[i][2],
                         "Q": gtnetrecord_allhouses[i][3],
                         "temperature": gtnetrecord_allhouses[i][4],
                         "opt": gtnetrecord_allhouses[i][5],
                         }
        json_records_full.append(record_single) #append a new element to the python array

    #print(json_records_full)

    return JsonResponse(json_records_full, safe=False)