from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import *
import json
import datetime
# Create your views here.


def login(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print(request.user.username)
            return redirect("/")
        else:
            message = "User doesnt exist"
            return render(request, "login.html", {
                "message": message
            })
    return render(request, "login.html", {
        "message": ""
    })


def signup(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        print(username, email, password)
        user = User.objects.create_user(
            username=username, email=email, password=password)
        return redirect("/login")
    return render(request, "signup.html")


@login_required(login_url="/login")
def home(request):
    contest_list = Contest.objects.all()
    return render(request, "home.html", {
        "contest_list": contest_list
    })


# Getting Error
def logout(reuest):
    auth_logout(request)
    return redirect("/login")


def create_contest(request):
    body = request.body.decode('utf-8')
    if body: 
        data = json.loads(body)
        [year, month, date] = data["start_time"].split("T")[0].split("-")
        [hour, minute, _] = data["start_time"].split("T")[1].split(":")
        contest = Contest()
        contest.creator = request.user
        contest.name = data["name"]
        contest.start_time = datetime.datetime(int(year), int(month), int(date), int(hour), int(minute))
        contest.duration = int(data["duration"])
        contest.save()
        for q in data["questions"]:
            question = Question()
            question.contest = contest
            question.name = q["name"]
            question.statement = q["statement"]
            question.input_cases = q["input_cases"]
            question.output_cases = q["output_cases"]
            question.save()
        return HttpResponse("success")
    return render(request, "create_contest.html")

def contest(request, contest_id): 
    contest = Contest.objects.get(id=contest_id)
    question_list = Question.objects.filter(contest=contest)
    return render(request, "contest.html", {
        "question_list": question_list, 
        "contest": contest
    })

def question(request, question_id):
    if request.POST:
        solution = Solution()
        question = Question.objects.get(id=question_id)
        solution.question = question
        solution.user = request.user
        solution.solution = request.POST.get("solution")
        solution.submitted_at = datetime.datetime.now()
        solution.verdict = solution.solution == question.output_cases
        if solution.verdict == True:
            message = "Right Answer"
        else: 
            message = "Wrong Answer"
        solution.save()
        return render(request, "question.html", {
            "question": question,
            "message": message,
            "submitted_solution": solution.solution
        })
    question = Question.objects.get(id=question_id)
    return render(request, "question.html", {
        "question": question,
        "message": "",
        "submitted_solution": ""
    })

def solutions(request, t, id):
    if t == "question":
        question = Question.objects.get(id=id)
        solutions = Solution.objects.filter(question=question).filter(user=request.user)
    else: 
        contest = Contest.objects.get(id=id)
        question_list = Question.objects.filter(contest=contest)
        solutions = []
        for question in question_list:
            t = Solution.objects.filter(question=question).filter(user=request.user)
            for t_ in t: solutions.append(t_)
    print(solutions)
    return render(request, "solutions.html", {
        "solutions": solutions
    })

def solution(request, solution_id): 
    solution = Solution.objects.get(id=solution_id)
    return render(request, "solution.html", {
        "solution": solution
    })