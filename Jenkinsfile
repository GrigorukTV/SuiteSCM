pipeline {
    agent any
//     agent {
//         docker: {image: 'python:3.7'}
//     }

    stages {
        stage('Build') {
            steps {
                sh 'chmod +x install.sh'
                sh './install.sh'
            }
        }
        stage('Test') {
            steps {
//                 sh './env/bin/pytest --url ${APP_URL} --executor ${EXECUTOR} --browser ${BROWSER} --alluredir allure-report'
                //sh 'docker --name my_test2_name run my_test1 --browser chrome --alluredir allure-report'
                sh 'docker run my_test1 --browser chrome --alluredir allure-report'
            }
        }
    }

    post {
        always {
            script {
                allure([reportBuildPolicy: 'ALWAYS', results: [[path: 'allure-results/allure_results_chrome'], [path: 'allure-results/allure_results_firefox']]])
            }

//         always {
//
//             script {
//                 allure([
//                         includeProperties: false,
//                         jdk: '',
//                         properties: [],
//                         reportBuildPolicy: 'ALWAYS',
//                         results: [[path: '/allure-report']]
//                 ])
//             }

//             cleanWs()
        }
    }
}