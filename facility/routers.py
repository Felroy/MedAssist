from django.conf import settings 
class dbRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'facility':
            return 'geospatial'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'facility':
            return 'geospatial'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'facility' or obj2._meta.app_label == 'facility':
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == 'geospatial':
            return model._meta.app_label == 'facility'
        elif model._meta.app_label == 'facility':
            return False
        return None