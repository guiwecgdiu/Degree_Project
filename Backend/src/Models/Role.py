from src.extension import db


role_permissions= db.Table('roles_permissions',
                db.Column('role_id',db.Integer,db.ForeignKey('role.id')),
                db.Column('permission_id',db.Integer,db.ForeignKey('permission.id'))
                        )
class Permission(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),unique=True)
    roles=db.relationship('Role',secondary=role_permissions,back_populates='permissions')

    def __repr__(self):
        return "u<Permission %s>"% self.name


class Role(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),unique=True)
    permissions=db.relationship('Permission',secondary=role_permissions,back_populates='roles')
    users=db.relationship('User',back_populates='role')

    @staticmethod
    def init_role():
        role_permissions_map = {
            'USER': ['RESERVE', 'UPLOAD'],
            'DOCTOR': ['CHANGE', 'ORDER']
        }
        for role_name in role_permissions_map:
            role=Role.query.filter_by(name=role_name).first()
            if role is None:
                role=Role(name=role_name)
                db.session.add(role)
            role.permissions=[]
            for permission_name in role_permissions_map[role_name]:
                permission=None
                permission=Permission.query.filter_by(name=permission).first()
                if permission is None:
                    permission = Permission(name=permission_name)
                    db.session.add(permission)
                role.permissions.append(permission)
        db.session.commit()



