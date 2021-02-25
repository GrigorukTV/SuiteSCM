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
//                 sh 'docker run my_test1 --browser chrome'
                sh 'docker run --name my_test_13 my_test1 --browser chrome'
                sh 'ls -la'
                sh 'docker cp my_test_13:/app/allure-result ./allure-report'
                sh 'ls -la'
                sh 'PWD'
            }
        }
    }

    post {
        always {

            script {
                allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: '../allure-report']]
                ])
            }

            cleanWs()
        }
    }
}