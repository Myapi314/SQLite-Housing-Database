# Found from resource about having multiple databases in a Django project

class HousingDbRouter(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on housingapi models to 'housingdb'"
        if model._meta.app_label == 'housingapi':
            return 'housingdb'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on housingapi models to 'housingdb'"
        if model._meta.app_label == 'housingapi':
            return 'housingdb'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in housingapi app"
        if obj1._meta.app_label == 'housingapi' and obj2._meta.app_label == 'housingapi':
            return True
        # Allow if neither is housingapi app
        elif 'housingapi' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'housingdb' or model._meta.app_label == "housingapi":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True