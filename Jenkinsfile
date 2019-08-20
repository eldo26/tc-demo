pipeline {
    agent any
    parameters {
    choice choices: ['NCIT', 'NCIT2', 'NCQA4'], description: 'Choose an Environment', name: 'Environment'
    choice choices: ['Add', 'Delete', 'Update'], description: 'Choose an Action', name: 'Action'
    password defaultValue: '', description: 'Enter Ansible vault password', name: 'vault-password'
    }
    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'master',
                url: 'https://github.com/eldo26/tc-demo.git'
            }
        }
        stage('Run Script') {
            steps {
            sh "python modify-ds-private.py"
            }
        }
    }
}
