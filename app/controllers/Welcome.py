from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        self.load_model('ItemModel')
        self.load_model('WishlistModel')
        self.db = self._app.db

    def index(self):
        session['user'] = None
        return self.load_view('index.html')
    
    def registration(self):
        data = {
            'name': request.form['name'],
            'uname': request.form['uname'],
            'password': request.form['password'],
            'confirm': request.form['confirm'],
            'date_hired': request.form['date']
        }        
        reg_status = self.models['WelcomeModel'].register(data)
        if reg_status['status'] == True:
            session['user']= reg_status['user_id']
            return redirect("/dashboard")
        else:
            print reg_status['error']
            for messages in reg_status['error']:
                flash(messages)
            return redirect("/")

    def login(self):
        data = {
            'uname': request.form['uname'],
            'password': request.form['password']
        }
        for i in data:
            if len(data[i])<1:
                flash("Please put a valid username and password")
                return redirect('/')
                
        log_status = self.models['WelcomeModel'].login(data)        
        if log_status == False:
            flash("Please put a valid username and password")
            return redirect('/')
        else:            
            session['user'] = log_status['id']
            return redirect('/dashboard')

    def dashboard(self):
        if session['user'] != None:
            itemlist = self.models['ItemModel'].get_itemlist(session['user'])
            wishlist = self.models['WishlistModel'].get_wishlist(session['user'])
            return self.load_view("myWishList.html",itemlist=itemlist,user_id =session['user'], wishlist=wishlist)
        else:
            return redirect('/')

    def itempage(self,id):
        if session['user'] != None:
            item_data = self.models['ItemModel'].get_item(id)
            user_list = self.models['WishlistModel'].get_users(id)
            return self.load_view("itempage.html", item_data=item_data,user_list = user_list)
        else:
            return redirect('/')
