from cement import Controller, ex
from time import strftime
from ..services.insert import Insert
from ..services.update import Update
from ..services.delete import Delete
from ..services.read import Read
from ..services.complete import Complete
class Items(Controller):
    class Meta:
        label = 'items'
        stacked_type = 'embedded'
        stacked_on = 'base'

    data = {
        "author": "Chestermo",
        "gender": "male",
        "age": "24",
        "body_fat": "15%",
        "interest": ["couch potato", "eat and sleep"]
    }    
    @ex(help = 'insert an item') 
    def create(self):
        Insert.insert(self,self.data)  

    @ex(help = 'update item')     
    def update(self):        
        Update.update(self)

    @ex(help = 'Delete item')     
    def delete(self):        
        Delete.delete(self) 

    @ex(help = 'List of items')     
    def list(self):
        data = {}        
        data = Read.read(self)
        self.app.render(data, 'items/list.jinja2')        
        
    
    @ex(help = 'Complete item')     
    def complete(self):        
        Complete.complete(self,5) 

    
    
    
    
    
   
    
   