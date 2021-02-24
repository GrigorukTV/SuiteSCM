pipeline {
    agent {
        docker { image 'node:14-alpine' }
    }
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
//                 sh './env/bin/pytest --url ${APP_URL} --executor ${EXECUTOR} --browser ${BROWSER} --alluredir allure-results'
                sh 'docker run --name my_run my_test --browser chrome'
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
                        results: [[path: 'allure-results']]
                ])
            }

            cleanWs()
        }
    }
}