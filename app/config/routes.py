
from system.core.router import routes

routes['default_controller'] = 'Welcome'
routes['POST']['/registration'] = 'Welcome#registration'
routes['POST']['/login'] = 'Welcome#login'
routes['/dashboard'] = 'Welcome#dashboard'
routes['/wish_items/create'] = "Items#addpage"
routes['POST']['/additem'] = "Items#create"
routes["/add/<user_id>/<item_id>"] = "Wishlist#add"
routes['/delete/<id>'] = 'Items#delete'
routes['/remove/<id>'] = 'Wishlist#remove'
routes['/wish_item/<id>'] = 'Welcome#itempage'