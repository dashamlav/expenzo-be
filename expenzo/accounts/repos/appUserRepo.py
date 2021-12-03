from accounts.models import AppUser


class AppUserRepo():

    def _base_query(self):
        return AppUser.objects.all()

    def getById(self, id):
        return self._base_query().filter(id=id, is_active=True)

    def getByEmail(self, email):
        return self._base_query().filter(email=email, is_active=True)

    def createUser(self, name, email, password):
        return AppUser.objects.create(
            first_name = name, 
            email = email, 
            password = password, 
            username = email
            )

    def doesUserExist(self, email):
        return bool(self.getByEmail(email))

appUserRepo = AppUserRepo()


