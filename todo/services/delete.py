from cement import Controller, ex
class Delete(Controller):
    class Meta:
        label = 'items'
        stacked_type = 'embedded'
        stacked_on = 'base'
    
    # update by index
    def delete(self):        
        self.app.log.info('delete working') 
        
  
# clear all index items
        def delete_index(_index):
            res = self.app.db.indices.delete(index=_index, ignore=[400, 404])
            return res


# delete content but empty item exist
        def delete_by_query(_index, query):
            res = self.app.delete_by_query(
                index=_index,
                body={"query": {"match": query}},
                _source=True
            )
            return res


# delet all item
        def delete_one(_index, _id):
            res = self.app.delete(index=_index, id=_id)
            return res

        _index = "test-index"
        res = delete_index(_index)
        
        #query = {"author": "Ken"}
        #res = delete_by_query(_index, query)
        #_id = "1"
        #res = delete_one(_index, _id)