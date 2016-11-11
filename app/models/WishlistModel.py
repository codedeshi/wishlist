from system.core.model import Model

class WishlistModel(Model):
    def __init__(self):
        super(WishlistModel, self).__init__()

    def add2wishlist(self,user_id,item_id):
        data = {
            'user_id':user_id,
            'item_id':item_id
        }
        query = "insert into wishlist (user_id,item_id) values (:user_id,:item_id)"
        return self.db.query_db(query,data)

    def get_wishlist(self,user_id):
        data = {'user_id':user_id}
        query = "select i.id, i.name, u.name as uname, i.user_id as added, i.created_at from items i join wishlist w on i.id = w.item_id join users u on u.id = i.user_id where w.user_id =:user_id"
        return self.db.query_db(query,data)

    def get_users(self,id):
        data = {'id':id}
        query = "select u.name from users u join wishlist w on u.id = w.user_id where w.item_id =:id"
        data = {'id':id}
        return  self.db.query_db(query, data)

    def remove(self,id,user_id):
        data = {'id':id}
        query = "delete from wishlist where item_id =:id and user_id =:user_id"
        data = {'id':id, 'user_id': user_id}
        return  self.db.query_db(query, data)
    def delete(self,id):
        data = {'id':id}
        query = "delete from wishlist where item_id =:id"
        data = {'id':id}
        return  self.db.query_db(query, data)


