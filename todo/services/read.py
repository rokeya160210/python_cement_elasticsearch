from cement import Controller, ex
class Read(Controller):
    class Meta:
        label = 'items'
        stacked_type = 'embedded'
        stacked_on = 'base'
    
    # update by index
    def read(self):        
        self.app.log.info('Read working') 
        
        def search_by_index_and_id(_index, _id):
            res = self.app.db.get(
            index=_index,
            id=_id
            )
            return res


        def search_by_index_and_query(_index, _doc_type, query):
            res = self.app.db.search(
                index=_index,
                body=query
            )
            return query



        index = "test-index"
        _id = 5
        res = search_by_index_and_id(index, _id)
        self.app.log.info(res) 
        
        return res