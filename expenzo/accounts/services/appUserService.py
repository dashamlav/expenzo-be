from accounts.repos.appUserRepo import appUserRepo


class AppUserService():

    def getById(self, id):
        return appUserRepo.getById(id)

    def getByEmail(self, email):
        return appUserRepo.getByEmail(email)

    def createUser(self, name, email, password):
        return appUserRepo.createUser(name, email, password)

    def doesUserExist(self, email):
        return appUserRepo.doesUserExist(email)
        
appUserService = AppUserService()