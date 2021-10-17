from cement import Controller, ex
class Insert(Controller):
    class Meta:
        label = 'items'
        stacked_type = 'embedded'
        stacked_on = 'base'
    
    
    def insert(self,data):        
        self.app.log.info('insertion working') 
        def create_index(index):
            self.app.db.create(index=index, ignore=400,id = 1, body = 'string')
        
        def insert_one_data(_index, data):
    
            res = self.app.db.index(index=_index, doc_type='authors', id=5, body=data)
    # index will return insert info: like as created is True or False
            print(res)
            self.app.log.info(res) 
        index = "test-index"
        create_index(index)
        insert_one_data(index, data)
