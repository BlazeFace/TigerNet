from TigerNet.static import db, models


u = models.User(nickname='Nate', email='nate@tn.com')
k = models.User(nickname='Lucia', email='lucia@tn.com')
g = models.User(nickname='Nic', email='nic@tn.com')
db.session.add(u)
db.session.add(k)
db.session.add(g)
db.session.commit()
