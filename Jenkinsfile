pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'chmod +x install.sh'
                sh './install.sh'
            }
        }
        stage('Test') {
            steps {
                catchError {
                    sh 'docker run --name my_test_54 my_test44 --url ${URL} --executor ${EXECUTOR} --browser ${BROWSER} --bversion ${BVERSION} -n ${NODES}'
                }
            }
         }
        stage('Copy_allure') {
            steps {
                   sh 'docker cp my_test_54:/app/allure-result /var/jenkins_home/workspace/test2/allure-results'
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

            sh 'docker rm my_test_54'

            cleanWs()
        }
    }
}