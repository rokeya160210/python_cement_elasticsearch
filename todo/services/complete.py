from cement import Controller, ex
from time import strftime
class Complete(Controller):
    class Meta:
        label = 'items'
        stacked_type = 'embedded'
        stacked_on = 'base'
    
    # update by index
    def complete(self,_id):        
        self.app.log.info('Read working') 
        _index = "test-index"  
        now = strftime("%Y-%m-%d %H:%M:%S")
        item = self.app.db.get(id=_id,index=_index)
        item['timestamp'] = now
        item['state'] = 'complete'

        self.app.log.info('completing todo item: %s - %s' % (_id, item['state']))
       
        ### send an email message
        
        msg = """
        Congratulations! The following item has been completed:

       Item Number: %s                                     Date: %s    

                     Ordhek Nari Ordhek Ishori ---Ahmed Sofa
       """ % (_id, item['timestamp'])
        
        self.app.mail.send(msg,
                      subject='TODO Item Complete',
                      to=[self.app.config.get('todo', 'email')],
                      from_addr='noreply@localhost',
                      )
        

       