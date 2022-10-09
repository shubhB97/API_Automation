import requests
import json
import jsonpath

base_url = "http://127.0.0.1:8000/"

def test_userDetails():
    res = userData = requests.get(base_url+"user")
    print(userData.content.count)
    assert res.status_code == 200 

def test_readQuestion():
    position = "3"
    res = requests.get(base_url+"question/"+position)
    assert res.status_code == 200

def test_readAlternatives():
    question_id = "3"
    res = requests.get(base_url+"alternatives/"+question_id)
    assert res.status_code == 200

def test_create_answer():
    answer = {
        "user_id": 2,
        "answers": [
            {
            "question_id": 3,
            "alternative_id": 8
            }
        ]
    }
    res = requests.post(base_url+"answer",data=answer, headers={'Content-Type':'application/json'})
    assert res.status_code == 201

def test_result():
    res = requests.get(base_url+"result/2")
    assert res.status_code == 200

