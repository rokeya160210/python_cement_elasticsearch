from cement import Controller, ex
class Update(Controller):
    class Meta:
        label = 'items'
        stacked_type = 'embedded'
        stacked_on = 'base'
    
    # update by index
    def update(self):        
        self.app.log.info('Update working') 
        
        def update_data_by_index(_index, _doc_type, _id, update_data):
            res = self.app.db.update(
            index=_index,
            doc_type=_doc_type,
            id=_id,
            body=update_data )
    
            return res
        index = "test-index"
        _id = 5
        _doc_type = "authors"
        update_data = {
        "doc": {"age": 26}
        }

        res = update_data_by_index(index, _doc_type, _id, update_data)
        self.app.log.info( res)

            
   
            
        
    
