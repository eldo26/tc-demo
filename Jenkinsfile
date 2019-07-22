pipeline {
    agent any
    stages {
        stage('Ansible') {
            steps {
                sh "ansible-playbook site.yaml -v"
            }
        }
    }
}