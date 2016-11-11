from system.core.controller import *

class Items(Controller):
    def __init__(self, action):
        super(Items, self).__init__(action)
        self.load_model('ItemModel')
        self.load_model('WishlistModel')
        self.db = self._app.db

    def addpage(self):
        if session['user'] != None:
            return self.load_view('createItem.html')
        else:
            return self.load_view("index.html")

    def create(self):
        data = {
            'name': request.form['name'],
            "user_id": session['user']            
        }
        if len(data['name'])<3:
            flash("Item name should be atleast 3 characters")
            return redirect("/wish_items/create")
        item = self.models['ItemModel'].createItem(data)
        if not item:
            flash('Item already Exists')
            return redirect("/wish_items/create")
        self.models['WishlistModel'].add2wishlist(session['user'],item)
        print item        
        return redirect('/dashboard')
    
    def delete(self,id):
        self.models['WishlistModel'].delete(id)
        self.models['ItemModel'].delete(id)
        return redirect("/dashboard")
