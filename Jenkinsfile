pipeline {
    agent any
    stages {
        stage('git checkout') {
            steps {
                sh "git clone https://github.com/eldo26/tc-demo.git"
            }
        }
        stage('Ansible') {
            steps {
                sh "ansible-playbook site.yaml -v"
            }
        }
    }
}