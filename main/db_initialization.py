from main import db
from main.models import BanCard, Domain, Event, Notice, Team, User


user_list = {   'A1085551': 1,
                'A1085552': 2,
                'A1085553': 3,
                'A1085554': 4,
                'A1085503': 5,
                'A1085505': 5,
                'A1085507': 5,
                'A1085510': 5,
                'A1085511': 5,
                'A1085512': 5,
                'A1085513': 5,
                'A1085516': 5,
                'A1085518': 5,
                'A1085520': 5,
                'A1085521': 5,
                'A1085523': 5,
                'A1085524': 5,
                'A1085527': 5,
                'A1085528': 5,
                'A1085529': 5,
                'A1085530': 5,
                'A1085534': 5,
                'A1085536': 5,
                'A1085537': 5,
                'A1085538': 5,
                'A1085539': 5,
                'A1085541': 5,
                                }


def db_init():
    # 建立小組
    for i in range(5):
        team = Team()
        db.session.add(team)
        db.session.commit()

    # 建立使用者
    for key, value in user_list.items():
        user = User(nickname=key, account=key, password=key, team_id=value)
        db.session.add(user)
        db.session.commit()

    # 建立 BanCard 資料
    for i in range(4):
        ban_card = BanCard()
        db.session.add(ban_card)
        db.session.commit()

    # 建立 Domain 資料
    for i in range(8):
        domain = Domain()
        db.session.add(domain)
        db.session.commit()


def db_create():
    db.create_all()


def db_drop():
    db.drop_all()