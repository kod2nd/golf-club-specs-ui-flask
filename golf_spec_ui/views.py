from flask import render_template
import requests
import json
import os


from golf_spec_ui import app

BASE_URL = os.getenv('API_URL')


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
    response = requests.get(str(BASE_URL) + 'users')
    users = response.json()
    return render_template('index.html', users=users)


def displayUser(user_id):
    response = requests.get(str(BASE_URL) + 'users/{}'.format(user_id))
    user = response.json()
    name = user['name']
    clubs = user['clubs']
    
    clubCategories = {}
    clubCategories['drivers'] = filterClub('driver', clubs)
    clubCategories['woods'] = filterClub('wood', clubs)
    clubCategories['hybrids'] = filterClub('hybrid', clubs)
    clubCategories['irons'] = filterClub('iron', clubs)
    clubCategories['wedges'] = filterClub('wedge', clubs)
    clubCategories['putters'] = filterClub('putter', clubs)
    
    return render_template('user.html', name=name, user_id=user_id, clubCategories=clubCategories)


@app.route('/', methods=['GET'])
def index():
    return displayIndex()


@app.route('/users', methods=['GET'])
@app.route('/users/<user_id>')
def user(user_id):
    return displayUser(user_id)
