from django.shortcuts import render

# Create your views here.
def quality(request):
    if(request.method=="POST"):
        data = request.POST 
        fixedacidity= float(data.get('textfixedacidity'))         
        volatileacidity=float(data.get('textvolatileacidity'))        
        citricacid=float(data.get('textcitricacid'))             
        residualsugar=float(data.get('textresidualsugar'))          
        chlorides=float(data.get('textchlorides'))               
        freesulfurdioxide=float(data.get('textfreesulfurdioxide'))     
        totalsulfurdioxide=float(data.get('texttotalsulfurdioxide'))    
        density=float(data.get('textdensity'))                 
        ph=float(data.get('textph'))                      
        sulphates=float(data.get('textsulphates'))               
        alcohol=float(data.get('textalcohol')) 
        if('buttonsubmit' in request.POST):
            import pandas as pd
            path="C:/Users/Harsha C/Desktop/intern/Data/Data/wine.csv"
            data=pd.read_csv(path)

            import sklearn
            from sklearn.preprocessing import LabelEncoder
            le_quality=LabelEncoder()

            data['quality_n']=le_quality.fit_transform(data['quality'])

            inputs=data.drop(['quality','quality_n'],axis=1)
            outputs=data['quality_n']

            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,outputs,test_size=0.3)

            from sklearn.naive_bayes import GaussianNB
            model=GaussianNB()
            model.fit(x_train,y_train)
 
            y_pred=model.predict([[fixedacidity,volatileacidity,citricacid,residualsugar,chlorides,freesulfurdioxide,totalsulfurdioxide,density,ph,sulphates,alcohol]])
            # result=(y_pred)
            if y_pred==1: 
                result=("Good Quality")  
            else:
                result=("Bad Quality")     
                    
        return render(request,'quality.html',context={'result':result})
   
    return render(request,'quality.html')

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')