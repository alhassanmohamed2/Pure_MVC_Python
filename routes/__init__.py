from controllers import *

routes = {

    '/':{ 'method':'get', 'action': index()}, 
    "/home":{'action': home(),'method':'get'}, 
    "/test":{'action': [test(), home()],'method':['pOsT','get']}
   
}