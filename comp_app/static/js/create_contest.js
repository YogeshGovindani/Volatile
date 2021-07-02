const createContestApp = angular.module('createContestApp', []);
createContestApp.controller('createContestController', function ($scope) {
    $scope.questions = [{
        statement: "",
        input_cases: "",
        output_cases: ""
    }]
    $scope.add_question = () => {
        $scope.questions.push({
            statement: "",
            input_cases: "",
            output_cases: ""
        })
    }

    $scope.create_contest = () => {
        const body = JSON.stringify({
            name: $scope.name,
            start_time: $scope.start_time,
            duration: $scope.duration,
            questions: $scope.questions
        });
        let csrftoken;
        document.cookie.split(" ").forEach(cookie => {
            if (cookie.split("=")[0] == "csrftoken") {
                csrftoken = cookie.split("=")[1]
            }
        })
        console.log(body, csrftoken);
        fetch("", {
            method: "POST",
            headers: {"X-CSRFToken": csrftoken},
            body: body
        }).then(response => (
            window.location.replace("/")
        ))
    }
})