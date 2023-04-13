from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request):
    print("welcome/url is requeste and display() is executed")
    ss='''
          
                  <h1 style="color:Blue;background-color:yellow;">
                         ***Hello user,Welcome to Django First-Project First-App***
                                     QEdge technology
                  </h1>
                  <hr/>
                  <h2 style="color:yellow;background-color:green;">
                         I am SANJIT
                  </h2>
                  <br/>
                  <h4>
                       1. One who has become dependent on something or drugs – ……………………………………………..…Addict / - (SO (Audit), 1997)
                       <br/>
                       2. Fear of being enclosed in small closed space –…………………………………. Claustrophobia / - - (SO (Audit), 1997)
                       <br/>
                       3. Call upon God or any other power (like law) for help or protection –……….……………....Invocation / (SO (Audit), 1997)
                       <br/>
                       4. Severely abusive writing in journals –…………………………………………………………..…………Scurrilous / (SO (Audit), 1997)
                       <br/>
                        5. A person who opposes war or use of military force –…………………………………Pacifist / / (SO (Audit), 1997)
                        <br/>
                       6. One not concerned with right or wrong –……………………………………………………………………….Amoral / (SO (Audit), 1997)
                       <br/>
                       7. Something no longer in use – …………………………………………………………………………………..Obsolete / (SO (Audit), 1997)
                       <br/>
                       8. Stealthily done (something done in a quiet and secret way in order to avoid being noticed) –
                                        ……………………………………………………………………………………………………………………………………Surreptitious / (SO (Audit), 1997)
                       <br/>
                        9. Words written on a tomb – ………………………………………………………………………….Epitaph / - (SO (Audit), 1997)
                        <br/>
                       10. A person with a long experience of any occupation – ………………………………….Veteran / (SO (Audit), 1997)
                       <br/>
                  </h4>
                  <hr/>
                  
          
       ''';
    return HttpResponse(ss);
    
def show(request):
    ss='''
        <http>
	 <head>
	 	   <title>***welcome-page</title>
	 	   <style>
	 	   	      h1{
	 	   	      	  color:Blue;
	 	   	      }
	 	   	      h2{
	 	   	      	  color:Green;
	 	   	      }
	 	   	      h3{
	 	   	      	  color:Red;
	 	   	      }
	 	   	      h4{
	 	   	      	  color:Orange;
	 	   	      }
	 	   	      h5{
	 	   	      	  color:Yellow;
	 	   	      }
	 	   	      h6{
	 	   	      	  color:Black;
	 	   	      }
	 	   	      
	 	   </style>
	 </head>
	 <body>
	 	   <center>
	 	   	       <h1>welcome to django html</h1>
	 	   	       <hr color='brown' width='95%'/>
	 	   	       <h2>welcome to django html</h2>
	 	   	       <hr color='brown' width='85%'/>
	 	   	       <h3>welcome to django html</h3>
	 	   	       <hr color='brown' width='75%'/>
                   <h4>welcome to django html</h4>
                   <hr color='brown' width='65%'/>
                   <h5>welcome to django html</h5>
                   <hr color='brown' width='55%'/>
                   <h6>welcome to django html</h6>
                   <hr color='brown' width='45%'/>
	 	   </center>
	 </body>>
</htttp>
    ''';
    return HttpResponse(ss);
    
def hello(request):
    ss='''
 <http>
	 <head>
	 	   <title>***hello-page</title>
	 	   <style>
	 	   	      h1{
	 	   	      	  color:Blue;
                      width:30%;
	 	   	      }
	 	   	      h2{
	 	   	      	  color:Green;
                      width:30%;
	 	   	      }
	 	   	      h3{
	 	   	      	  color:Red;
                      width:30%;
	 	   	      }
                  h1,h2,h3{
                            background-color:lightblue;
                            border:4px solid Brown
                  }
                  
	 	   </style>
	 </head>
	 <body>
	 	   <center>
	 	   	       <h1>hello user....!!!</h1>
	 	   	       <hr color='black' width='40%'/>
	 	   	       <h2>welcome to django App</h2>
	 	   	       <hr color='black' width='40%'/>
	 	   	       <h3>have a nice day</h3>
	 	   	       <hr color='black' width='40%'/>
	 	   </center>
	 </body>>
</htttp>
    ''';
    return HttpResponse(ss);
    

    

                        
  
import time;
def senddatetime(request):
    ct=time.ctime()
    print("client Request Date & time on server :: ")
    ss='''
 <http>
	 <head>
	 	   <title>***hello-page</title>
	 	   <style>
	 	   	      h1{
	 	   	      	  color:Blue;
                      width:30%;
	 	   	      }
	 	   	      h2{
	 	   	      	  color:Green;
                      width:30%;
	 	   	      }
	 	   	      h3{
	 	   	      	  color:Red;
                      width:30%;
	 	   	      }
                  h1,h2,h3{
                            background-color:lightblue;
                            border:4px solid Brown
                  }
                  
	 	   </style>
	 </head>
	 <body>
	 	   <center>
	 	   	       <h1>hello user....!!!</h1>
	 	   	       <hr color='black' width='40%'/>
	 	   	       <h2>welcome to django App</h2>
	 	   	       <hr color='black' width='40%'/>
	 	   	       <h3>''',ct,'''</h3>
	 	   	       <hr color='black' width='40%'/>
	 	   </center>
	 </body>>
</htttp>
    ''';
    return HttpResponse(ss);
    
def demo(request):
    print("mulitiple-requests-URLs same response");
    htmldata='''<center>
             <h1>Welcome Demo user!!!</h1>
             <hr/>
             <h2>I think you are doing great!!!</h2>
             <hr/>
             <h3>this is same o/p for multiple response!!!</h3>
             <hr/>
             </center>''';
             
    return HttpResponse(htmldata);
    
def homepage(request):
    print("mulitiple-requests-URLs same response");
    htmldata='''<center>
             <h1>Welcome to default Home-page!!!</h1>
             <hr/>
             <h2>out of service!!!</h2>
             <hr/>
             <h3>try again!!!</h3>
             <hr/>
             </center>''';
             
    return HttpResponse(htmldata);