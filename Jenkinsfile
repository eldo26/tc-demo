pipeline {
    agent any
    stages {
        stage('Ansible Provisioning') {
            steps {
                sh "ansible-playbook site.yaml -v"
            }
        }
    }
}