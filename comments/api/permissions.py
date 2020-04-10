from generic.permissions import IsAuthorizedAndOwner

class IsAuthorizaedAndAuthor(IsAuthorizedAndOwner):

    def is_owner(self, obj, request):
        return obj.author == request.auth.get('uuid')