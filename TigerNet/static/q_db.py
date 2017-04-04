from TigerNet.static import models

userd = models.User.query.all()
for u in userd:
    print(u.id, u.nickname)
