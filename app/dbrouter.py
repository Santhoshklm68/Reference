from typing import Union


class BaseRouter:
    router_app_labels = []
    db_name = ''

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return self.db_name
        return None


    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return self.db_name
        return None


    def allow_relation(self, obj1, obj2, **hints):
        
        if (
            obj1._meta.app_label in self.router_app_labels
            or obj2._meta.app_label in self.router_app_labels
        ):
            return True
        return None


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # print(model_name,app_label)
        if app_label in self.router_app_labels:
            return db == self.db_name
        return None  # Return False instead of None


class DefaultRouter(BaseRouter):
    router_app_labels = ['auth', 'admin', 'sessions', 'contenttypes']
    db_name = "default"


class AppRouter(BaseRouter):
    router_app_labels = ['app']  # Replace with the actual app label of your library app
    db_name = "custom_db"
