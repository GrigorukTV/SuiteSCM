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
                sh 'docker run --name my_test_98 my_test1 --url ${URL} --executor ${EXECUTOR} --browser ${BROWSER}'

//                 sh 'docker cp my_test_18:/app/allure-result /var/jenkins_home/workspace/test2/allure-report'
                sh 'docker cp my_test_98:/app/allure-result /var/jenkins_home/workspace/test2/allure-results'
                sh 'ls -la'
//                 sh 'ls -la /var/jenkins_home/workspace/test2/allure-report'
//                 sh 'ls -la /var/jenkins_home/workspace/test2/allure-results'
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