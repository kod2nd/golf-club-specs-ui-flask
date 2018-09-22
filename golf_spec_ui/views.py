from flask import render_template
import requests
import json


from golf_spec_ui import app

BASE_URL = 'https://golf-specs-api.herokuapp.com/'


def filterClubCategory(club, nameOfCategory):
    if club['category'] == nameOfCategory:
        return True
    else:
        return False


def filterClub(category, clubs):
    filteredLists = list(filter(lambda club: filterClubCategory(club, category), clubs))
    sortedList = sorted(filteredLists, key=lambda club: (club['model'], club['loft']) )
    return sortedList


def displayIndex():
    response = requests.get(BASE_URL + 'users')
    users = response.json()
    return render_template('index.html', users=users)


def displayUser(user_id):
    response = requests.get(BASE_URL + 'users/{}'.format(user_id))
    user = response.json()
    clubs = user['clubs']
    drivers = filterClub('driver', clubs)
    wedges = filterClub('wedge', clubs)
    return render_template('user.html', user_id=user_id, drivers=drivers, wedges=wedges)


@app.route('/', methods=['GET'])
def index():
    return displayIndex()


@app.route('/users', methods=['GET'])
@app.route('/users/<user_id>')
def user(user_id):
    return displayUser(user_id)
