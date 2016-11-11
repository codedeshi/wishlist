from system.core.controller import *

class Wishlist(Controller):
    def __init__(self, action):
        super(Wishlist, self).__init__(action)
        self.load_model('WelcomeModel')
        self.load_model('ItemModel')
        self.load_model('WishlistModel')
        self.db = self._app.db

    def add(self,user_id,item_id):
        try:
            self.models['WishlistModel'].add2wishlist(user_id,item_id)
            return redirect('/dashboard')
        except:
            return redirect('/dashboard')

    def remove(self,id):
        self.models['WishlistModel'].remove(id,session['user'])
        return redirect("/dashboard")