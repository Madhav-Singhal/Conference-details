from django.shortcuts import render
import requests

# Create your views here.
def home(request):

    url='https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences'
    r = requests.get(url).json()
    x = r['paid']
    
    meeting=[]

    for i in range(len(x)):
        
        if x[i] not in meeting:
            meeting.append(x[i])
       
 
    array = [] 
    k=[]
    for i in range(len(meeting)):
      

        index = -1
        for j, obj in enumerate(k):
            if obj['venue'] == meeting[i]['venue'] and obj['city'] == meeting[i]['city'] :
                index = 1
                break
        if index == -1:
            detail={
            'confName': meeting[i]['confName'],
            'confStartDate': meeting[i]['confStartDate'],
            'city': meeting[i]['city'],
            'state': meeting[i]['state'],
            'country': meeting[i]['country'],
            'entryType': meeting[i]['entryType'],
            'confRegUrl': meeting[i]['confRegUrl'],
            
            }
            array.append(detail)
            k.append(meeting[i])
    
    return render(request, 'schedule.html', {'array':array})

   
    

   