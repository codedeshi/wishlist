from system.core.model import Model

class ItemModel(Model):
    def __init__(self):
        super(ItemModel, self).__init__()

    def createItem(self,data):
        try:
            query = "INSERT into items (name,user_id) values (:name,:user_id)"
            return  self.db.query_db(query, data)
        except:
            return False
    
    def get_itemlist(self,user_id):
        query = "select i.id, i.name, u.name as added , i.created_at  from items i left join users u on i.user_id = u.id where i.id not in (select it.id from items it join wishlist w on it.id = w.item_id join users us on us.id = it.user_id where w.user_id =:user_id)"
        return self.db.query_db(query,{'user_id':user_id})

    def delete(self, id):
        query = "delete from items where id =:id"
        data = {'id':id}
        return  self.db.query_db(query, data)

    def get_item(self,id):
        query = "select * from items where id=:id"
        data = {'id':id}
        return  self.db.query_db(query, data)[0]



