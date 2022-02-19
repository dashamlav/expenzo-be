from accounts.repos.tokenRepo import tokenRepo

class TokenService():

    def getToken(self, user):
        return tokenRepo.getToken(user)

    def createToken(self, user):
        return tokenRepo.createToken(user)

    def replaceExistingToken(self, user):
        return tokenRepo.replaceExistingToken(user)

tokenService = TokenService()