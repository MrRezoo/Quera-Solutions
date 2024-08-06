class HospRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'hospital':
            return 'hospitals'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'hospital':
            return 'hospitals'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'hospital' or obj2._meta.app_label == 'hospital':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'hospital':
            return db == 'hospitals'
        return None


class CompRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'company':
            return 'companies'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'company':
            return 'companies'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'company' or obj2._meta.app_label == 'company':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'company':
            return db == 'companies'
        return None
