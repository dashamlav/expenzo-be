from accounts.models import AuthToken

class TokenRepo():
    
    def _base_query(self):
        return AuthToken.objects.select_related('user').all()

    def getToken(self, user):
        try:
            return self._base_query().get(user=user)
        except AuthToken.DoesNotExist:
            return None

    def createToken(self, user):
        token, _ = AuthToken.objects.get_or_create(user=user)
        return token

    def replaceExistingToken(self, user):
        existingToken = self.getToken(user)
        if not existingToken:
            new_token, _ = AuthToken.objects.get_or_create(user=user)
            return new_token
        existingToken.delete()
        return self.createToken(user)

tokenRepo = TokenRepo()